# EXP-0005 — MoveIt2 Planning Validation

## Status

Validated

## Objective

Validate that MoveIt2 can plan and execute trajectories for the Doosan `m1013` in the local ROS 2 Jazzy environment.

## Context

Previous experiments validate direct service-based motion through Doosan ROS 2 interfaces.

This experiment validates the motion planning layer using MoveIt2.

The goal is to understand the role of MoveIt2 in the future architecture:

- Doosan ROS 2 services can be used for direct robot motion execution.
- MoveIt2 can be used for planning and trajectory validation.
- RViz2 can be used for visualization and manual inspection.

This distinction is important because the future architecture should separate motion planning from robot execution.

## Environment

Expected environment:

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Doosan Robotics ROS 2
- Doosan `m1013`
- Docker Emulator `doosanrobot/dsr_emulator:3.0.1`
- RViz2
- MoveIt2

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
- Doosan ROS 2 packages must be visible.
- MoveIt2 launch files must be available.
- The `m1013` model must be supported by the Doosan MoveIt2 configuration.

## Interfaces and Tools Under Test

Tool:

```text
MoveIt2
```

Expected launch package:

```text
dsr_bringup2
```

Expected launch file:

```text
dsr_bringup2_moveit.launch.py
```

Robot model:

```text
m1013
```

## Validation Steps

### Terminal A — Source Doosan workspace

```bash
cd ~/doosan_ws
source ~/doosan_ws/install/setup.bash
```

### Expected Result

The command should complete without errors.

---

### Terminal A — Verify MoveIt2 launch arguments

```bash
ros2 launch dsr_bringup2 dsr_bringup2_moveit.launch.py --show-args
```

### Expected Result

ROS 2 should print the available launch arguments.

Expected arguments may include:

```text
name
host
port
mode
model
color
gz
rt_host
gripper
```

---

### Terminal A — Launch MoveIt2 with Doosan m1013

```bash
ros2 launch dsr_bringup2 dsr_bringup2_moveit.launch.py mode:=virtual model:=m1013 host:=127.0.0.1
```

### Expected Result

MoveIt2 should launch successfully.

RViz2 should open with the MoveIt2 MotionPlanning plugin and the Doosan `m1013` model.

Keep this terminal open while performing the validation.

---

### MoveIt2 GUI — Plan a trajectory

Using the MoveIt2 interface in RViz2:

1. Select the available planning group.
2. Move the interactive marker or set a valid target.
3. Click `Plan`.

### Expected Result

MoveIt2 should generate a valid trajectory.

The planned trajectory should be visible in RViz2.

---

### MoveIt2 GUI — Execute planned trajectory

Using the MoveIt2 interface in RViz2:

1. After a valid plan is generated, click `Execute`.
2. Observe the robot motion in RViz2.

### Expected Result

The Doosan `m1013` should execute the planned motion in virtual mode.

---

### Terminal B — Source Doosan workspace

```bash
source ~/doosan_ws/install/setup.bash
```

### Expected Result

The command should complete without errors.

---

### Terminal B — Inspect ROS 2 nodes

```bash
ros2 node list
```

### Expected Result

The output should include active nodes related to MoveIt2, robot state publishing, controllers, and Doosan.

---

### Terminal B — Inspect ROS 2 topics

```bash
ros2 topic list
```

### Expected Result

The output should include active topics related to robot state, planning, transforms, and controllers.

Expected examples may include:

```text
/joint_states
/tf
/tf_static
```

---

### Terminal B — Inspect Doosan services

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

The experiment was completed successfully.

MoveIt2 launched correctly with the Doosan `m1013` in virtual mode, and RViz2 opened with the MoveIt2 MotionPlanning plugin available for validation.

Validated observations:

- The MoveIt2 launch file `dsr_bringup2_moveit.launch.py` was available and accepted the expected launch arguments.
- The Doosan `m1013` model appeared correctly in RViz2.
- The MoveIt2 MotionPlanning plugin was available in RViz2.
- A valid planning group was available for the robot.
- MoveIt2 generated a valid trajectory for the selected target.
- The planned trajectory was visible in RViz2.
- The planned trajectory executed successfully in virtual mode.
- ROS 2 nodes, topics, and Doosan services were available during the MoveIt2 session.

No blocking warnings, errors, or planning limitations were identified during this validation.

## Evidence

Evidence can be stored in:

```text
assets/evidence/EXP-0005/
```

Suggested evidence:

- screenshot of MoveIt2 loaded in RViz2;
- screenshot of a planned trajectory;
- screenshot or short recording of trajectory execution;
- terminal output of the MoveIt2 launch;
- terminal output of `ros2 node list`;
- terminal output of `ros2 topic list`.

## Conclusion

The experiment confirms that MoveIt2 can be used as a planning and trajectory execution layer for the Doosan `m1013` in the local ROS 2 Jazzy environment.

This validates the role of MoveIt2 as a higher-level planning component, while the previously validated Doosan ROS 2 services remain suitable for direct service-based motion experiments.

## Next Step

The next recommended experiment is:

```text
EXP-0006-gazebo-simulation-validation.md
```

The goal will be to validate the Gazebo simulation flow and clarify the role of Gazebo compared with RViz2 and MoveIt2.
