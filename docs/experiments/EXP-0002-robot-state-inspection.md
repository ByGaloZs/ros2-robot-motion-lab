# EXP-0002 — Robot State Inspection

## Status

Pending Validation

## Objective

Validate how to inspect the current state of the Doosan `m1013` while the robot is running in virtual mode.

This experiment focuses on observing:

- active ROS 2 nodes;
- active ROS 2 topics;
- joint state publication;
- transform publication;
- Doosan-related services.

## Context

Before building a custom motion client, it is important to understand how the robot exposes its current state through the ROS 2 graph.

This experiment does not send motion commands. It only inspects the active ROS 2 system.

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
~/Documents/dev/doosan-ros2-lab
```

## Preconditions

Before running this experiment:

- ROS 2 Jazzy must be sourced.
- The Doosan ROS 2 workspace must be sourced.
- Docker must work without `sudo`.
- The Doosan virtual stack must be launched.
- The robot must be visible in RViz2 or another supported visualization tool.

## Interfaces Under Inspection

Expected topics may include:

```text
/joint_states
/tf
/tf_static
```

Expected namespace:

```text
/dsr01
```

Expected service namespace:

```text
/dsr01/dsr_controller2/
```

## Validation Steps

### Terminal A — Launch Doosan virtual stack

```bash
cd ~/doosan_ws
source ~/doosan_ws/install/setup.bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m1013
```

### Expected Result

The Doosan virtual stack should launch successfully with RViz2 and the Doosan `m1013` model.

The terminal should remain active while the inspection commands are executed from another terminal.

---

### Terminal B — Source Doosan workspace

```bash
source ~/doosan_ws/install/setup.bash
```

### Expected Result

The command should complete without errors.

---

### Terminal B — List ROS 2 nodes

```bash
ros2 node list
```

### Expected Result

The output should include active ROS 2 nodes related to the robot stack.

Expected Doosan-related entries may appear under:

```text
/dsr01
```

---

### Terminal B — List Doosan-related nodes

```bash
ros2 node list | grep dsr
```

### Expected Result

The output should include Doosan-related nodes if the naming includes `dsr`.

If no output is returned, inspect the full node list manually with:

```bash
ros2 node list
```

---

### Terminal B — List ROS 2 topics

```bash
ros2 topic list
```

### Expected Result

The output should include active topics.

Expected examples:

```text
/joint_states
/tf
/tf_static
```

---

### Terminal B — Inspect joint states

```bash
ros2 topic echo /joint_states
```

### Expected Result

The terminal should print joint state messages.

Expected message fields include:

```text
name
position
velocity
effort
```

Stop the command with:

```text
Ctrl+C
```

---

### Terminal B — Inspect transform topics

```bash
ros2 topic list | grep tf
```

### Expected Result

The output should include transform-related topics.

Expected examples:

```text
/tf
/tf_static
```

---

### Terminal B — List Doosan-related services

```bash
ros2 service list | grep dsr
```

### Expected Result

The output should include Doosan-related services.

Expected example:

```text
/dsr01/dsr_controller2/motion/move_joint
```

## Actual Result

Pending validation.

After validation, document:

- whether `/joint_states` was available;
- whether `/tf` and `/tf_static` were available;
- whether Doosan-related nodes were visible;
- whether Doosan-related services were visible;
- any namespace differences found during inspection.

## Evidence

Evidence can be stored in:

```text
assets/evidence/EXP-0002/
```

Suggested evidence:

- terminal output of `ros2 node list`;
- terminal output of `ros2 topic list`;
- terminal output of `/joint_states`;
- terminal output of `ros2 service list | grep dsr`;
- RViz2 screenshot showing the robot model.

## Conclusion

Pending validation.

This experiment should confirm whether the Doosan `m1013` exposes enough runtime state information through the ROS 2 graph to support future custom clients and validation tools.

## Next Step

The next recommended experiment is:

```text
EXP-0003-doosan-services-and-interfaces-mapping.md
```

The goal will be to map available Doosan service interfaces and identify which services are relevant for future custom motion clients.