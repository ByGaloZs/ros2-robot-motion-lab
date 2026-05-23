# EXP-0001 — MoveJoint Service Validation

## Status

Validated

## Objective

Validate that the Doosan `m1013` can execute a joint motion command in virtual mode
using the official ROS 2 service:

```text
/dsr01/dsr_controller2/motion/move_joint
```

with service type:

```text
dsr_msgs2/srv/MoveJoint
```

## Context

This experiment verifies that the robot can be controlled directly through the official
Doosan ROS 2 service interface, without relying on high-level wrappers.

This is an important baseline for future work because the project aims to build a custom
ROS 2 motion client using:

- `dsr_msgs2`
- `dsr_controller2`
- official ROS 2 services
- Python / `rclpy`

## Environment

Validated environment:

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Doosan Robotics ROS 2
- Doosan `m1013`
- Docker Emulator `doosanrobot/dsr_emulator:3.0.1`
- RViz2
- Python / ROS 2 CLI

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

## Interface Under Test

### Service

```text
/dsr01/dsr_controller2/motion/move_joint
```

### Type

```text
dsr_msgs2/srv/MoveJoint
```

### Relevant Request Fields

```text
float64[6] pos
float64 vel
float64 acc
float64 time
float64 radius
int8 mode
int8 blend_type
int8 sync_type
```

### Relevant Response Field

```text
bool success
```

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

The terminal should remain active while the experiment is executed from another
terminal.

---

### Terminal B — Source Doosan workspace

```bash
source ~/doosan_ws/install/setup.bash
```

### Expected Result

The command should complete without errors.

---

### Terminal B — Verify Doosan services

```bash
ros2 service list | grep dsr
```

### Expected Result

The output should include Doosan-related services.

Expected service:

```text
/dsr01/dsr_controller2/motion/move_joint
```

---

### Terminal B — Verify MoveJoint service type

```bash
ros2 service type /dsr01/dsr_controller2/motion/move_joint
```

### Expected Result

```text
dsr_msgs2/srv/MoveJoint
```

---

### Terminal B — Inspect MoveJoint interface

```bash
ros2 interface show dsr_msgs2/srv/MoveJoint
```

### Expected Result

The command should print the `MoveJoint` service definition.

Expected fields include:

```text
float64[6] pos
float64 vel
float64 acc
float64 time
float64 radius
int8 mode
int8 blend_type
int8 sync_type
---
bool success
```

---

### Terminal B — Execute small relative joint motion

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_joint dsr_msgs2/srv/MoveJoint "{pos: [0.0, 0.0, 90.0, 0.0, 90.0, 0.0], vel: 10.0, acc: 10.0, time: 0.0, radius: 0.0, mode: 1, blend_type: 0, sync_type: 0}"
```

### Expected Result

The robot should execute a small relative joint movement in virtual mode.

Expected response:

```text
success: true
```

or an equivalent successful service response.

---

### Terminal B — Return from relative motion

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_joint dsr_msgs2/srv/MoveJoint "{pos: [0.0, 0.0, -90.0, 0.0, -90.0, 0.0], vel: 10.0, acc: 10.0, time: 0.0, radius: 0.0, mode: 1, blend_type: 0, sync_type: 0}"
```

### Expected Result

The robot should execute a small relative joint movement in the opposite direction.

Expected response:

```text
success: true
```

or an equivalent successful service response.

## Actual Result

The Doosan `m1013` successfully executed the joint motion command in virtual mode using
the official ROS 2 `MoveJoint` service.

The service was available under the expected namespace:

```text
/dsr01/dsr_controller2/motion/move_joint
```

The service type matched the expected interface:

```text
dsr_msgs2/srv/MoveJoint
```

The robot responded correctly to a small relative joint movement and to the reverse
movement.

## Evidence

Evidence can be stored in:

```text
notebooks/evidence/EXP-0001/
```

Suggested evidence:

- RViz2 screenshot showing the Doosan `m1013`.
- Terminal output of `ros2 service type`.
- Terminal output of `ros2 interface show`.
- Terminal output of the successful `ros2 service call`.
- Optional short screen recording of the robot movement in RViz2.

## Conclusion

The experiment validates that the Doosan `m1013` can be controlled directly through the
official ROS 2 `MoveJoint` service in virtual mode.

This confirms that future custom clients can communicate with Doosan ROS 2 services
directly, without depending on high-level wrappers such as `DSR_ROBOT2.py`.

## Next Step

The next recommended experiment is to validate robot state inspection.

Potential next experiment:

```text
EXP-0002-robot-state-inspection.md
```

The goal would be to inspect topics, services, or state interfaces that expose the
current robot state, joint positions, and transforms.
