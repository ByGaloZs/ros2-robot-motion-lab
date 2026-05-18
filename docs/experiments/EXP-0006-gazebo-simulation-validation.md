# EXP-0006 — Gazebo Simulation Validation

## Status

Pending Validation

## Objective

Validate that Gazebo can launch and simulate the Doosan `m1013` in the local ROS 2 Jazzy environment.

## Context

RViz2, MoveIt2, and Gazebo serve different purposes:

- RViz2 is mainly used for visualization.
- MoveIt2 is used for motion planning.
- Gazebo is used for simulation.

This experiment validates the Gazebo layer and helps clarify how simulation fits into the future architecture.

The result of this experiment will help decide whether Gazebo should be used as part of future validation workflows for motion planning, execution, or environment interaction.

## Environment

Expected environment:

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Doosan Robotics ROS 2
- Doosan `m1013`
- Docker Emulator `doosanrobot/dsr_emulator:3.0.1`
- Gazebo
- RViz2 if enabled by the launch configuration

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
- Gazebo must be installed and available.
- Doosan Gazebo launch files must be available.
- The `m1013` model must be supported by the Doosan Gazebo configuration.

## Interfaces and Tools Under Test

Tool:

```text
Gazebo
```

Expected launch package:

```text
dsr_bringup2
```

Expected launch file:

```text
dsr_bringup2_gazebo.launch.py
```

Robot model:

```text
m1013
```

Expected namespace:

```text
dsr01
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

### Terminal A — Verify Gazebo launch arguments

```bash
ros2 launch dsr_bringup2 dsr_bringup2_gazebo.launch.py --show-args
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
gui
gz
x
y
z
R
P
Y
rt_host
use_sim_time
remap_tf
```

---

### Terminal A — Launch Gazebo with Doosan m1013

```bash
ros2 launch dsr_bringup2 dsr_bringup2_gazebo.launch.py mode:=virtual host:=127.0.0.1 port:=12346 name:=dsr01 model:=m1013 x:=0 y:=0
```

### Expected Result

Gazebo should launch successfully and load the Doosan `m1013` robot model.

The terminal should remain active while the inspection commands are executed from another terminal.

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

The output should include active nodes related to Gazebo, robot state, controllers, and Doosan.

---

### Terminal B — Inspect ROS 2 topics

```bash
ros2 topic list
```

### Expected Result

The output should include active simulation and robot state topics.

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

### Optional — Launch Gazebo with GUI enabled

If the previous launch does not open the expected GUI, test:

```bash
ros2 launch dsr_bringup2 dsr_bringup2_gazebo.launch.py mode:=virtual host:=127.0.0.1 port:=12346 name:=dsr01 model:=m1013 x:=0 y:=0 gui:=true
```

### Expected Result

Gazebo should open with the Doosan `m1013`.

If supported by the launch configuration, RViz2 may also open.

## Actual Result

Pending validation.

After validation, document:

- whether Gazebo launched successfully;
- whether the Doosan `m1013` model loaded correctly;
- whether `/joint_states` was available;
- whether `/tf` and `/tf_static` were available;
- whether Doosan-related services were visible;
- any warnings or errors shown in the terminal.

## Evidence

Evidence can be stored in:

```text
assets/evidence/EXP-0006/
```

Suggested evidence:

- screenshot of Gazebo with the Doosan `m1013`;
- terminal output of the Gazebo launch;
- terminal output of `ros2 node list`;
- terminal output of `ros2 topic list`;
- terminal output of `/joint_states`;
- terminal output of `ros2 service list | grep dsr`.

## Conclusion

Pending validation.

This experiment should confirm whether Gazebo can be used as a simulation layer for the Doosan `m1013` in the local ROS 2 Jazzy environment.

It should also clarify the practical difference between RViz2 visualization, MoveIt2 planning, and Gazebo simulation.

## Next Step

The next recommended experiment is:

```text
EXP-0007-motion-command-failure-handling.md
```

The goal will be to understand how the Doosan ROS 2 services behave when invalid or incomplete motion commands are sent.