# EXP-0004 — MoveLine Service Validation

## Status

Validated

## Objective

Validate that the Doosan `m1013` can execute a Cartesian linear motion command in
virtual mode using the official ROS 2 `MoveLine` service.

## Context

`MoveJoint` validates joint-space motion.

For future trajectory planning, palletizing, or Cartesian path execution, it is also
important to validate Cartesian motion.

This experiment verifies whether the robot can receive and execute a linear Cartesian
motion using the official Doosan ROS 2 service interface.

## Environment

Expected environment:

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
- The `move_line` service must be visible in the ROS 2 graph.
- The `MoveLine` service definition must be inspected before calling the service.

## Interface Under Test

### Expected Service

```text
/dsr01/dsr_controller2/motion/move_line
```

### Expected Type

```text
dsr_msgs2/srv/MoveLine
```

If the service name is different, document the actual service name found with:

```bash
ros2 service list | grep line
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

Keep this terminal open while the experiment is executed from another terminal.

---

### Terminal B — Source Doosan workspace

```bash
source ~/doosan_ws/install/setup.bash
```

### Expected Result

The command should complete without errors.

---

### Terminal B — Search for line motion services

```bash
ros2 service list | grep line
```

### Expected Result

The output should include a line motion service.

Expected service:

```text
/dsr01/dsr_controller2/motion/move_line
```

If the exact service differs, document the actual name.

---

### Terminal B — Verify MoveLine service type

```bash
ros2 service type /dsr01/dsr_controller2/motion/move_line
```

### Expected Result

```text
dsr_msgs2/srv/MoveLine
```

If the service name differs, replace the command with the actual service path.

---

### Terminal B — Inspect MoveLine interface

```bash
ros2 interface show dsr_msgs2/srv/MoveLine
```

### Expected Result

The command should print the full `MoveLine` service definition.

Document the actual request fields before executing the service call.

---

### Terminal B — Execute small Cartesian linear motion

> Important: validate the exact `MoveLine` request structure before running this
> command. Adjust the fields if the local interface definition differs.

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_line dsr_msgs2/srv/MoveLine "{pos: [0.0, 0.0, -100.0, 0.0, 0.0, 0.0], vel: [20.0, 10.0], acc: [20.0, 10.0], time: 0.0, radius: 0.0, ref: 0, mode: 1, blend_type: 0, sync_type: 0}"
```

### Expected Result

The robot should execute a small Cartesian linear motion in virtual mode.

Expected response:

```text
success: true
```

or an equivalent successful service response.

---

### Terminal B — Return from small Cartesian linear motion

> Important: validate the exact `MoveLine` request structure before running this
> command. Adjust the fields if the local interface definition differs.

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_line dsr_msgs2/srv/MoveLine "{pos: [0.0, 0.0, 100.0, 0.0, 0.0, 0.0], vel: [20.0, 10.0], acc: [20.0, 10.0], time: 0.0, radius: 0.0, ref: 0, mode: 1, blend_type: 0, sync_type: 0}"
```

### Expected Result

The robot should execute a small Cartesian linear motion in the opposite direction.

Expected response:

```text
success: true
```

or an equivalent successful service response.

## Actual Result

The experiment was completed successfully.

The Doosan virtual stack launched correctly in virtual mode and the Cartesian linear
motion service was available in the ROS 2 graph.

Validated observations:

- The active line motion service path was `/dsr01/dsr_controller2/motion/move_line`.
- The service type was confirmed as `dsr_msgs2/srv/MoveLine`.
- The `MoveLine` service interface was inspected before executing the service call.
- The request fields used for validation were `pos`, `vel`, `acc`, `time`, `radius`,
  `ref`, `mode`, `blend_type`, and `sync_type`.
- The first Cartesian linear motion service call succeeded.
- The robot motion was visible in RViz2 while running in virtual mode.
- The return Cartesian linear motion service call also succeeded.

Both service calls returned a successful response and the robot returned from the small
Cartesian displacement as expected.

## Evidence

Evidence can be stored in:

```text
notebooks/evidence/EXP-0004/
```

Suggested evidence:

- terminal output of `ros2 service list | grep line`;
- terminal output of `ros2 service type`;
- terminal output of `ros2 interface show dsr_msgs2/srv/MoveLine`;
- terminal output of the successful `ros2 service call`;
- RViz2 screenshot or screen recording showing the motion.

## Conclusion

The experiment confirms that Cartesian linear motion can be executed directly through
the official Doosan ROS 2 `MoveLine` service in virtual mode.

This validates `dsr_msgs2/srv/MoveLine` as a suitable interface for future direct
service-based Cartesian motion experiments and provides a baseline for later MoveIt2
planning validation.

## Next Step

The next recommended experiment is:

```text
EXP-0005-moveit2-planning-validation.md
```

The goal will be to validate motion planning using MoveIt2 with the Doosan `m1013`.
