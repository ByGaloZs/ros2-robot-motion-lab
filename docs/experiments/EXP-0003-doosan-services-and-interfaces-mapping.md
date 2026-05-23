# EXP-0003 — Doosan Services and Interfaces Mapping

## Status

Validated

## Objective

Map the available Doosan ROS 2 packages, services, and interfaces exposed through
`dsr_msgs2` and the active Doosan ROS 2 stack.

This experiment focuses on understanding what service interfaces are available before
implementing a custom ROS 2 client.

## Context

The future Doosan adapter should communicate directly with official Doosan ROS 2
services while keeping the general motion client layer robot-agnostic.

Before designing that adapter, it is necessary to identify:

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
~/Documents/dev/ros2-robot-motion-lab
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
/home/galozs-dev/doosan_ws/install/dsr_msgs2
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

The experiment was completed successfully.

The Doosan ROS 2 packages were visible from the ROS 2 CLI after sourcing the Doosan
workspace. The `dsr_msgs2` package was available and resolved to the Doosan workspace
install path.

Validated observations:

- Doosan-related packages were detected with `ros2 pkg list | grep dsr`.
- The `dsr_msgs2` package was available.
- Doosan message and service interfaces were listed through `ros2 interface list`.
- Motion-related service interfaces were available, including `dsr_msgs2/srv/MoveJoint`
  and `dsr_msgs2/srv/MoveLine`.
- The `MoveJoint` service definition was inspected successfully and exposed the expected
  request and response fields.
- The `MoveLine` service definition was inspected successfully.
- After launching the Doosan virtual stack, active Doosan services were visible under
  the `/dsr01/dsr_controller2/` namespace.
- The active motion service `/dsr01/dsr_controller2/motion/move_joint` was available.
- The service type for `/dsr01/dsr_controller2/motion/move_joint` was confirmed as
  `dsr_msgs2/srv/MoveJoint`.

## Evidence

Evidence can be stored in:

```text
notebooks/evidence/EXP-0003/
```

Suggested evidence:

- terminal output of `ros2 pkg list | grep dsr`;
- terminal output of `ros2 interface list | grep dsr_msgs2`;
- terminal output of `ros2 interface show dsr_msgs2/srv/MoveJoint`;
- terminal output of `ros2 interface show dsr_msgs2/srv/MoveLine`;
- terminal output of `ros2 service list | grep dsr`.

## Conclusion

The experiment confirms that the Doosan ROS 2 service interfaces required for future
custom client development are available through the official `dsr_msgs2` package.

The validated `MoveJoint` service and the inspected `MoveLine` interface provide a clear
baseline for implementing future direct service-based motion experiments without relying
on high-level wrappers.

## Next Step

The next recommended experiment is:

```text
EXP-0004-moveline-service-validation.md
```

The goal will be to validate Cartesian linear motion using the official Doosan ROS 2
service interface.
