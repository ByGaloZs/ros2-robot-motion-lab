# EXP-0008 — Python rclpy Service Client Prototype

## Status

Validated

## Objective

Validate that a minimal Python client can call the official Doosan ROS 2 `MoveJoint`
service using `rclpy`.

## Context

Previous experiments validated motion commands using the ROS 2 CLI.

This experiment creates the first bridge between command-line validation and custom
software development.

The goal is not to create the final ROS 2 package yet.

The goal is to validate that Python can:

- initialize a ROS 2 node;
- import the Doosan `MoveJoint` service type;
- create a service client;
- wait for the service;
- send a request;
- receive and inspect the response.

This experiment is the technical starting point for the future motion client and adapter
layers:

```text
robot_motion_client
doosan_motion_adapter
```

## Environment

Expected environment:

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Doosan Robotics ROS 2
- Doosan `m1013`
- Docker Emulator `doosanrobot/dsr_emulator:3.0.1`
- Python 3
- `rclpy`
- `dsr_msgs2`

Official Doosan workspace:

```text
~/doosan_ws
```

Lab repository:

```text
~/Documents/dev/ros2-robot-motion-lab
```

## Preconditions

Before running this experiment:

- ROS 2 Jazzy must be sourced.
- The Doosan ROS 2 workspace must be sourced.
- Docker must work without `sudo`.
- The Doosan virtual stack must be launched.
- The `move_joint` service must be visible in the ROS 2 graph.
- The `MoveJoint` interface must be available from Python.

## Interface Under Test

### Service

```text
/dsr01/dsr_controller2/motion/move_joint
```

### Type

```text
dsr_msgs2/srv/MoveJoint
```

## Prototype Location

Suggested prototype path:

```text
scripts/prototypes/move_joint_client.py
```

This script is a temporary prototype.

It is not the final ROS 2 package structure.

## Validation Steps

### Terminal A — Launch Doosan virtual stack

```bash
cd ~/doosan_ws
source ~/doosan_ws/install/setup.bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m1013
```

### Expected Result

The Doosan virtual stack should launch successfully with RViz2 and the Doosan `m1013`
model.

Keep this terminal open while the Python client is executed from another terminal.

---

### Terminal B — Source Doosan workspace

```bash
source ~/doosan_ws/install/setup.bash
```

### Expected Result

The command should complete without errors.

---

### Terminal B — Verify service availability

```bash
ros2 service type /dsr01/dsr_controller2/motion/move_joint
```

### Expected Result

```text
dsr_msgs2/srv/MoveJoint
```

---

### Terminal B — Create prototype directory

```bash
cd ~/Documents/dev/ros2-robot-motion-lab
mkdir -p scripts/prototypes
```

### Expected Result

The directory should be created if it does not already exist.

---

### Terminal B — Create prototype file

Create this file:

```text
scripts/prototypes/move_joint_client.py
```

with the following content:

```python
#!/usr/bin/env python3

from __future__ import annotations

import sys

import rclpy
from dsr_msgs2.srv import MoveJoint
from rclpy.node import Node


SERVICE_NAME = "/dsr01/dsr_controller2/motion/move_joint"


class MoveJointClient(Node):
    """Minimal client for the Doosan MoveJoint service."""

    def __init__(self) -> None:
        super().__init__("move_joint_client")
        self.client = self.create_client(MoveJoint, SERVICE_NAME)

    def wait_until_available(self, timeout_sec: float = 5.0) -> bool:
        return self.client.wait_for_service(timeout_sec=timeout_sec)

    def send_relative_motion(self) -> bool:
        request = MoveJoint.Request()
        request.pos = [0.0, 0.0, 90.0, 0.0, -90.0, 0.0]
        request.vel = 10.0
        request.acc = 10.0
        request.time = 0.0
        request.radius = 0.0
        request.mode = 1
        request.blend_type = 0
        request.sync_type = 0

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        response = future.result()

        if response is None:
            self.get_logger().error("MoveJoint service returned no response.")
            return False

        self.get_logger().info(f"MoveJoint success: {response.success}")
        return bool(response.success)


def main() -> int:
    rclpy.init()

    node = MoveJointClient()

    try:
        if not node.wait_until_available():
            node.get_logger().error(f"Service not available: {SERVICE_NAME}")
            return 1

        success = node.send_relative_motion()
        return 0 if success else 1

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    sys.exit(main())
```

### Expected Result

The file should be created successfully.

---

### Terminal B — Run the Python prototype

```bash
python3 scripts/prototypes/move_joint_client.py
```

### Expected Result

The robot should execute a small relative joint motion in virtual mode.

Expected log output:

```text
MoveJoint success: True
```

or equivalent.

---

### Terminal B — Verify that the robot can still be controlled from CLI

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_joint dsr_msgs2/srv/MoveJoint "{pos: [0.0, 0.0, -2.0, 0.0, 0.0, 0.0], vel: 10.0, acc: 10.0, time: 0.0, radius: 0.0, mode: 1, blend_type: 0, sync_type: 0}"
```

### Expected Result

The robot should execute a small relative movement in the opposite direction.

Expected response:

```text
success: true
```

or an equivalent successful response.

## Actual Result

The experiment was completed successfully.

The Python prototype was created under the lab repository and executed after sourcing
the ROS 2 Jazzy environment and the official Doosan workspace.

Validated observations:

- Python imported `rclpy` successfully after the ROS 2 environment was sourced.
- Python imported `MoveJoint` from `dsr_msgs2.srv` successfully after the Doosan
  workspace was sourced.
- The client node initialized correctly using `rclpy`.
- The client detected the `/dsr01/dsr_controller2/motion/move_joint` service.
- The prototype sent a `MoveJoint` request successfully.
- The service response returned a successful result.
- The robot executed the requested joint motion in virtual mode.

An initial import failure confirmed that the lab repository does not provide ROS 2 or
Doosan Python interfaces by itself. The script depends on the active terminal
environment being configured with `source /opt/ros/jazzy/setup.bash` and `source
/home/galozs-dev/doosan_ws/install/setup.bash`.

## Evidence

Evidence can be stored in:

```text
assets/evidence/EXP-0008/
```

Suggested evidence:

- terminal output running the Python script;
- RViz2 screenshot or short recording showing the motion;
- terminal output of the service availability check;
- optional screenshot of the prototype file.

## Conclusion

The experiment confirms that Python can directly communicate with the official Doosan
ROS 2 `MoveJoint` service using `rclpy`.

This validates the basic software pattern required for a future custom motion client:
source the ROS 2 and Doosan environments, initialize a Python ROS 2 node, import the
official service type, create a service client, send a request, and inspect the
response.

This provides the technical basis for creating future ROS 2 package layers such as:

```text
robot_motion_client
doosan_motion_adapter
```

## Next Step

After this experiment, the next phase is to create the initial ROS 2 package structure
under:

```text
ros2_packages/
```

Recommended future package layers:

```text
robot_motion_client
doosan_motion_adapter
```

The first implementation should keep general motion client logic separate from the
Doosan-specific adapter for:

```text
/dsr01/dsr_controller2/motion/move_joint
```

using:

```text
dsr_msgs2/srv/MoveJoint
```
