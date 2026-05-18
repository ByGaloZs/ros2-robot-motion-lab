# EXP-0003 — Doosan Services and Interfaces Mapping

## Status

Pending Validation

## Objective

Map the available Doosan ROS 2 packages, services, and interfaces exposed through `dsr_msgs2` and the active Doosan ROS 2 stack.

This experiment focuses on understanding what service interfaces are available before implementing a custom ROS 2 client.

## Context

The future package `doosan_motion_client` should communicate directly with official Doosan ROS 2 services.

Before designing that package, it is necessary to identify:

- available Doosan packages;
- available Doosan service interfaces;
- active Doosan services;
- relevant motion-related interfaces;
- service definitions required by future clients.

## Environment

Expected environment:

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Doosan Robotics ROS 2
- Doosan `m1013`
- Docker Emulator `doosanrobot/dsr_emulator:3.0.1`
- ROS 2 CLI

Official Doosan workspace:

```text
~/doosan_ws
```

Lab repository:

```text
~/Documents/dev/doosan-ros2-lab
```

## Preconditions

Before running this experiment:

- ROS 2 Jazzy must be sourced.
- The Doosan ROS 2 workspace must be sourced.
- The Doosan packages must be visible from the ROS 2 CLI.
- For active service inspection, the Doosan virtual stack must be running.

## Interfaces Under Inspection

Main package:

```text
dsr_msgs2
```

Relevant service interfaces:

```text
dsr_msgs2/srv/MoveJoint
dsr_msgs2/srv/MoveLine
```

Expected active service:

```text
/dsr01/dsr_controller2/motion/move_joint
```

## Validation Steps

### Terminal A — Source Doosan workspace

```bash
source ~/doosan_ws/install/setup.bash
```

### Expected Result

The command should complete without errors.

---

### Terminal A — Check Doosan package availability

```bash
ros2 pkg list | grep dsr
```

### Expected Result

The output should include Doosan-related packages.

Expected examples:

```text
dsr_bringup2
dsr_controller2
dsr_description2
dsr_gazebo2
dsr_hardware2
dsr_moveit2
dsr_msgs2
```

---

### Terminal A — Check `dsr_msgs2` package path

```bash
ros2 pkg prefix dsr_msgs2
```

### Expected Result

The output should point to the Doosan workspace install directory.

Expected example:

```text
/home/galozs/doosan_ws/install/dsr_msgs2
```

---

### Terminal A — List all Doosan interfaces

```bash
ros2 interface list | grep dsr_msgs2
```

### Expected Result

The output should include available Doosan message and service interfaces.

---

### Terminal A — List only Doosan service interfaces

```bash
ros2 interface list | grep "dsr_msgs2/srv"
```

### Expected Result

The output should include available Doosan service interfaces.

Expected examples:

```text
dsr_msgs2/srv/MoveJoint
dsr_msgs2/srv/MoveLine
```

---

### Terminal A — Inspect MoveJoint interface

```bash
ros2 interface show dsr_msgs2/srv/MoveJoint
```

### Expected Result

The command should print the `MoveJoint` service definition.

Expected request fields include:

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

### Terminal A — Inspect MoveLine interface

```bash
ros2 interface show dsr_msgs2/srv/MoveLine
```

### Expected Result

The command should print the `MoveLine` service definition.

Document the request and response fields after validation.

---

### Terminal B — Launch Doosan virtual stack

```bash
cd ~/doosan_ws
source ~/doosan_ws/install/setup.bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m1013
```

### Expected Result

The Doosan virtual stack should launch successfully.

Keep this terminal open while inspecting active services.

---

### Terminal A — List active Doosan services

```bash
ros2 service list | grep dsr
```

### Expected Result

The output should include active Doosan services.

Expected example:

```text
/dsr01/dsr_controller2/motion/move_joint
```

---

### Terminal A — Check MoveJoint active service type

```bash
ros2 service type /dsr01/dsr_controller2/motion/move_joint
```

### Expected Result

```text
dsr_msgs2/srv/MoveJoint
```

## Actual Result

Pending validation.

After validation, document:

- packages detected with `ros2 pkg list | grep dsr`;
- whether `dsr_msgs2` is available;
- relevant service interfaces found;
- active Doosan services found;
- exact service types for motion-related services.

## Evidence

Evidence can be stored in:

```text
assets/evidence/EXP-0003/
```

Suggested evidence:

- terminal output of `ros2 pkg list | grep dsr`;
- terminal output of `ros2 interface list | grep dsr_msgs2`;
- terminal output of `ros2 interface show dsr_msgs2/srv/MoveJoint`;
- terminal output of `ros2 interface show dsr_msgs2/srv/MoveLine`;
- terminal output of `ros2 service list | grep dsr`.

## Conclusion

Pending validation.

This experiment should produce a clear map of the Doosan ROS 2 interfaces available for future custom client development.

## Next Step

The next recommended experiment is:

```text
EXP-0004-moveline-service-validation.md
```

The goal will be to validate Cartesian linear motion using the official Doosan ROS 2 service interface.