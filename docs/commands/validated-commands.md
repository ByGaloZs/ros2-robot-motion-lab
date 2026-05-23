# Validated Commands

This document records the command catalog used to validate the current ROS 2 robot
motion lab environment.

The goal is to keep a reliable list of commands that are useful, reproducible, and
aligned with the current lab setup.

## Scope

This document covers:

- repository checks;
- terminal environment checks;
- Python virtual environment setup;
- Docker checks;
- Doosan workspace checks;
- Doosan emulator and virtual mode launch commands;
- ROS 2 graph inspection;
- Doosan interface inspection;
- RViz2 launch;
- MoveIt2 launch;
- Gazebo launch;
- basic `MoveJoint` service call.

## Important Paths

The lab repository is located at:

```text
~/Documents/dev/ros2-robot-motion-lab
```

The validated official Doosan ROS 2 workspace is located at:

```text
~/doosan_ws
```

This repository must remain separate from the official Doosan workspace.

## Important Rule

Do not modify, move, delete, or rewrite files inside:

```text
~/doosan_ws
```

unless the task explicitly requires working on the official Doosan workspace.

---

# 1. Repository Commands

## Check current repository directory

### Purpose

Verify that the terminal is located inside the local lab repository.

### Command

```bash
pwd
```

### Expected Result

```text
/home/galozs-dev/Documents/dev/ros2-robot-motion-lab
```

### Notes

Use this before editing documentation or running Git commands.

---

## Check repository status

### Purpose

Check the current Git status of the repository.

### Command

```bash
git status
```

### Expected Result

Git should show the current branch and whether there are modified, staged, or untracked
files.

Example of a clean repository:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### Notes

Use this before creating commits.

---

## Check repository remote

### Purpose

Verify that the repository is connected to the expected GitHub remote.

### Command

```bash
git remote -v
```

### Expected Result

```text
origin  https://github.com/ByGaloZs/ros2-robot-motion-lab.git (fetch)
origin  https://github.com/ByGaloZs/ros2-robot-motion-lab.git (push)
```

### Notes

If SSH is used instead of HTTPS, the remote may look different.

---

## Check commit history

### Purpose

Show recent commits in a compact format.

### Command

```bash
git log --oneline --decorate -n 5
```

### Expected Result

Git should print the latest five commits.

### Notes

Useful to verify recent documentation changes.

---

# 2. Terminal Environment Commands

## Activate repository Python virtual environment

### Purpose

Activate the repository-local Python virtual environment in the current terminal session.

### Command

```bash
source .venv/bin/activate
```

### Expected Result

The shell prompt should indicate that the `.venv` environment is active.

### Notes

Run this from the repository root before executing Python tools that depend on the local
virtual environment.

---

## Upgrade Python packaging tool

### Purpose

Upgrade `pip` inside the active Python environment.

### Command

```bash
python -m pip install --upgrade pip
```

### Expected Result

`pip` should install or confirm the latest available version for the active environment.

### Notes

Run this after activating `.venv` when preparing the local Python development
environment.

---

## Install pallet layout core in editable mode

### Purpose

Install the local `pallet_layout_core` package in editable mode for development.

### Command

```bash
python -m pip install -e ros2_packages/pallet_layout_core
```

### Expected Result

The package should be installed into the active Python environment, while changes made in
the source directory remain immediately available.

### Notes

Run this from the repository root after activating `.venv`.

---

## Run `pallet_layout_core` Unit Tests Without ROS 2 Pytest Plugins

### Command

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest ros2_packages/pallet_layout_core/tests -q
```

### Context

This command is used to run the unit tests for `pallet_layout_core` as a pure Python
module.

The development shell may have ROS 2 Jazzy sourced through `.bashrc`, which exposes ROS 2
Python packages and pytest plugins such as `launch_testing`.

When pytest plugin autoloading is enabled, pytest may attempt to load ROS 2 testing
plugins even though `pallet_layout_core` does not depend on ROS 2.

### Reason

`pallet_layout_core` must remain robot-agnostic and independent from:

- ROS 2.
- Doosan Robotics.
- MoveIt2.
- Gazebo.
- ROS 2 launch testing plugins.

Disabling pytest plugin autoloading ensures that the unit tests validate only the pure
Python package.

### Validated Result

```txt
10 passed in 0.03s
```

### Notes

Do not install extra packages such as `PyYAML` only to satisfy ROS 2 pytest plugins for
this module.

If a future package needs ROS 2 integration tests, those tests should be documented
separately and executed with the ROS 2 test environment enabled.

---

## Check active ROS 2 distribution

### Purpose

Verify that ROS 2 is sourced and that the active distribution is Jazzy.

### Command

```bash
echo $ROS_DISTRO
```

### Expected Result

```text
jazzy
```

### Notes

If the output is empty, ROS 2 has not been sourced in the current terminal session.

---

## Check ROS 2 executable path

### Purpose

Verify that the `ros2` command is available in the terminal and identify where it is
loaded from.

### Command

```bash
which ros2
```

### Expected Result

```text
/opt/ros/jazzy/bin/ros2
```

### Notes

This confirms that the ROS 2 CLI is available.

---

## Check ROS 2 CLI availability

### Purpose

Verify that the ROS 2 CLI responds correctly.

### Command

```bash
ros2 --help
```

### Expected Result

ROS 2 should print the available CLI commands.

### Notes

This is a basic ROS 2 CLI sanity check.

---

# 3. Docker Commands

## Check Docker installation

### Purpose

Verify that Docker is installed and available from the terminal.

### Command

```bash
docker --version
```

### Expected Result

Docker should print the installed version.

Example:

```text
Docker version 28.x.x, build xxxxxxx
```

### Notes

Docker is required for the Doosan emulator in virtual mode.

---

## Check Docker access without sudo

### Purpose

Verify that Docker can be executed without using `sudo`.

### Command

```bash
docker ps
```

### Expected Result

Docker should list running containers or show an empty table.

Example:

```text
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Notes

An empty table is valid when no containers are currently running.

If this command fails with a permission error, the current user may not be correctly
added to the `docker` group.

---

## List Docker images

### Purpose

List locally available Docker images.

### Command

```bash
docker images
```

### Expected Result

Docker should print locally available images.

### Notes

Useful to verify whether the Doosan emulator image is already available locally.

---

## Check Doosan emulator Docker image

### Purpose

Verify whether the Doosan emulator image is available locally.

### Command

```bash
docker images | grep dsr_emulator
```

### Expected Result

The output should include:

```text
doosanrobot/dsr_emulator
```

Expected image tag:

```text
3.0.1
```

### Notes

The expected emulator image for this lab is:

```text
doosanrobot/dsr_emulator:3.0.1
```

---

# 4. Doosan Workspace Commands

## Go to official Doosan workspace

### Purpose

Move to the validated official Doosan ROS 2 workspace.

### Command

```bash
cd ~/doosan_ws
```

### Expected Result

The terminal should move to:

```text
/home/galozs-dev/doosan_ws
```

### Notes

This workspace is separate from the lab repository.

---

## Verify Doosan workspace location

### Purpose

Confirm that the terminal is located inside the official Doosan workspace.

### Command

```bash
pwd
```

### Expected Result

```text
/home/galozs-dev/doosan_ws
```

### Notes

Use this before running Doosan ROS 2 launch commands.

---

## Source Doosan workspace

### Purpose

Load the installed Doosan ROS 2 packages into the current terminal session.

### Command

```bash
source ~/doosan_ws/install/setup.bash
```

### Expected Result

The command should complete without printing errors.

### Notes

This command makes packages such as `dsr_bringup2`, `dsr_msgs2`, `dsr_controller2`,
`dsr_description2`, `dsr_moveit2`, and related packages available to the ROS 2 CLI.

---

## Check Doosan package availability

### Purpose

Verify that Doosan ROS 2 packages are visible from the current terminal session.

### Command

```bash
ros2 pkg list | grep dsr
```

### Expected Result

The output should include Doosan-related packages such as:

```text
dsr_bringup2
dsr_controller2
dsr_description2
dsr_gazebo2
dsr_hardware2
dsr_moveit2
dsr_msgs2
```

### Notes

If no packages appear, the Doosan workspace may not be sourced.

---

## Check `dsr_bringup2` package path

### Purpose

Verify where ROS 2 finds the `dsr_bringup2` package.

### Command

```bash
ros2 pkg prefix dsr_bringup2
```

### Expected Result

The output should point to the Doosan workspace install directory.

Expected example:

```text
/home/galozs-dev/doosan_ws/install/dsr_bringup2
```

### Notes

This confirms that `dsr_bringup2` is available.

---

## Check `dsr_msgs2` package path

### Purpose

Verify where ROS 2 finds the `dsr_msgs2` package.

### Command

```bash
ros2 pkg prefix dsr_msgs2
```

### Expected Result

The output should point to the Doosan workspace install directory.

Expected example:

```text
/home/galozs-dev/doosan_ws/install/dsr_msgs2
```

### Notes

This confirms that Doosan service and message interfaces are available.

---

# 5. Doosan Emulator and Virtual Mode Commands

## Show RViz2 launch arguments

### Purpose

Inspect available arguments for the Doosan RViz2 launch file.

### Command

```bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py --show-args
```

### Expected Result

ROS 2 should print launch arguments such as:

```text
name
host
port
mode
model
color
gui
gz
rt_host
remap_tf
```

### Notes

This is a safe inspection command and does not launch the robot stack.

---

## Launch Doosan virtual stack with RViz2

### Purpose

Launch the Doosan `m1013` in virtual mode with RViz2.

### Command

```bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m1013
```

### Expected Result

The Doosan virtual environment should launch with:

- emulator process;
- Doosan ROS 2 control stack;
- robot state publisher;
- controller manager;
- RViz2;
- Doosan `m1013` model.

### Notes

Keep this terminal open while running inspection commands from another terminal.

In virtual mode, the emulator is started as part of the launch lifecycle.

Stop the launch with:

```text
Ctrl+C
```

---

## Verify emulator container after virtual launch

### Purpose

Check whether an emulator-related Docker container is running after launching Doosan in
virtual mode.

### Command

```bash
docker ps | grep emulator
```

### Expected Result

The output should show a running emulator-related container.

### Notes

Run this command in a second terminal while the virtual launch is still running.

---

## List running Docker containers after virtual launch

### Purpose

Inspect all running Docker containers after launching Doosan in virtual mode.

### Command

```bash
docker ps
```

### Expected Result

Docker should list the active containers.

### Notes

The Doosan emulator container should appear while the virtual Doosan launch is active.

---

# 6. ROS 2 Graph Inspection Commands

These commands should be executed after launching the Doosan virtual stack.

Use a second terminal and source the Doosan workspace before running them:

```bash
source ~/doosan_ws/install/setup.bash
```

## List ROS 2 nodes

### Purpose

List active ROS 2 nodes in the current ROS graph.

### Command

```bash
ros2 node list
```

### Expected Result

ROS 2 should print active nodes.

Expected Doosan-related nodes may include entries under:

```text
/dsr01
```

### Notes

This confirms that the Doosan ROS 2 graph is active.

---

## List Doosan-related ROS 2 nodes

### Purpose

Filter active ROS 2 nodes related to Doosan.

### Command

```bash
ros2 node list | grep dsr
```

### Expected Result

The output should include Doosan-related nodes under the expected namespace.

Expected namespace:

```text
/dsr01
```

### Notes

If there is no output, the Doosan stack may not be running or the namespace may be
different.

---

## List available ROS 2 services

### Purpose

List available ROS 2 services in the current ROS graph.

### Command

```bash
ros2 service list
```

### Expected Result

ROS 2 should print active services.

### Notes

This command is only useful for Doosan validation after the Doosan virtual stack is
running.

---

## List Doosan-related services

### Purpose

List only ROS 2 services related to the Doosan namespace.

### Command

```bash
ros2 service list | grep dsr
```

### Expected Result

The output should include Doosan-related services.

Expected example:

```text
/dsr01/dsr_controller2/motion/move_joint
```

### Notes

If this command returns no output, verify that the Doosan virtual stack is running and
that the workspace has been sourced.

---

## List controller-related services

### Purpose

List services related to `controller_manager`.

### Command

```bash
ros2 service list | grep controller
```

### Expected Result

The output should include controller-related services.

### Notes

This helps confirm that `ros2_control` and controller services are active.

---

## List ROS 2 topics

### Purpose

List active ROS 2 topics in the current graph.

### Command

```bash
ros2 topic list
```

### Expected Result

ROS 2 should print active topics.

Expected examples may include:

```text
/joint_states
/tf
/tf_static
```

### Notes

Useful to confirm that robot state and transforms are being published.

---

## Echo joint states

### Purpose

Inspect robot joint state messages.

### Command

```bash
ros2 topic echo dsr01/joint_states
```

### Expected Result

ROS 2 should print joint state messages.

### Notes

Stop the command with:

```text
Ctrl+C
```

If `/joint_states` is namespaced differently, inspect the topic list first.

---

# 7. Doosan Interface Inspection Commands

These commands validate that Doosan service interfaces are available.

They do not require the robot stack to be running if the Doosan workspace has already
been sourced.

## List available Doosan interfaces

### Purpose

List available interfaces from the `dsr_msgs2` package.

### Command

```bash
ros2 interface list | grep dsr_msgs2
```

### Expected Result

ROS 2 should print available Doosan message and service interfaces.

### Notes

This confirms that Doosan interfaces are available from the terminal.

---

## List Doosan service interfaces

### Purpose

List only service interfaces from `dsr_msgs2`.

### Command

```bash
ros2 interface list | grep "dsr_msgs2/srv"
```

### Expected Result

ROS 2 should print service interfaces such as:

```text
dsr_msgs2/srv/MoveJoint
dsr_msgs2/srv/MoveLine
```

### Notes

Useful before selecting which service to inspect or call.

---

## Check MoveJoint service type

### Purpose

Verify the service type used by the Doosan joint motion service.

### Command

```bash
ros2 service type /dsr01/dsr_controller2/motion/move_joint
```

### Expected Result

```text
dsr_msgs2/srv/MoveJoint
```

### Notes

This command requires the Doosan virtual stack to be running.

---

## Inspect MoveJoint service definition

### Purpose

Inspect the request and response fields required by the `MoveJoint` service.

### Command

```bash
ros2 interface show dsr_msgs2/srv/MoveJoint
```

### Expected Result

ROS 2 should print the full service definition.

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
```

Expected response field:

```text
bool success
```

### Notes

This command is important before writing any Python client with `rclpy`.

---

## Inspect MoveLine service definition

### Purpose

Inspect the request and response fields required by the `MoveLine` service.

### Command

```bash
ros2 interface show dsr_msgs2/srv/MoveLine
```

### Expected Result

ROS 2 should print the full service definition for Cartesian linear motion.

### Notes

This command is useful for future Cartesian motion experiments.

---

# 8. RViz2 Commands

## Launch RViz2 with Doosan m1013 in virtual mode

### Purpose

Launch RViz2 with the Doosan `m1013` model in virtual mode.

### Command

```bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m1013
```

### Expected Result

RViz2 should open and display the Doosan `m1013`.

### Notes

This command also starts the Doosan virtual stack.

Keep the launch terminal open while inspecting nodes, topics, and services from another
terminal.

---

# 9. MoveIt2 Commands

## Show MoveIt2 launch arguments

### Purpose

Inspect available arguments for the Doosan MoveIt2 launch file.

### Command

```bash
ros2 launch dsr_bringup2 dsr_bringup2_moveit.launch.py --show-args
```

### Expected Result

ROS 2 should print available launch arguments.

Expected arguments include:

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

### Notes

This is a safe inspection command.

---

## Launch MoveIt2 with Doosan m1013 in virtual mode

### Purpose

Launch MoveIt2 for the Doosan `m1013` in virtual mode.

### Command

```bash
ros2 launch dsr_bringup2 dsr_bringup2_moveit.launch.py mode:=virtual model:=m1013 host:=127.0.0.1
```

### Expected Result

MoveIt2 should launch successfully and allow planning or executing trajectories.

### Notes

MoveIt2 is used for motion planning validation.

Keep the launch terminal open while running inspection commands from another terminal.

---

# 10. Gazebo Commands

## Show Gazebo launch arguments

### Purpose

Inspect available arguments for the Doosan Gazebo launch file.

### Command

```bash
ros2 launch dsr_bringup2 dsr_bringup2_gazebo.launch.py --show-args
```

### Expected Result

ROS 2 should print available launch arguments.

Expected arguments include:

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

### Notes

This is a safe inspection command.

---

## Launch Gazebo with Doosan m1013 in virtual mode

### Purpose

Launch Gazebo with the Doosan `m1013` in virtual mode.

### Command

```bash
ros2 launch dsr_bringup2 dsr_bringup2_gazebo.launch.py mode:=virtual host:=127.0.0.1 port:=12346 name:=dsr01 model:=m1013 x:=0 y:=0
```

### Expected Result

Gazebo should open and load the Doosan `m1013` robot model.

### Notes

This command starts the Gazebo simulation flow.

The namespace is:

```text
dsr01
```

The port used here is:

```text
12346
```

---

## Launch Gazebo with RViz enabled

### Purpose

Launch Gazebo and enable RViz visualization if supported by the launch configuration.

### Command

```bash
ros2 launch dsr_bringup2 dsr_bringup2_gazebo.launch.py mode:=virtual host:=127.0.0.1 port:=12346 name:=dsr01 model:=m1013 x:=0 y:=0 gui:=true
```

### Expected Result

Gazebo should open with the Doosan `m1013`, and RViz2 should also open if the launch
configuration supports `gui:=true`.

### Notes

Use this only when visual inspection in both Gazebo and RViz2 is needed.

---

# 11. Motion Service Commands

These commands send motion commands to the robot.

Use them only when the robot is running in virtual mode.

## Call MoveJoint service with small relative motion

### Purpose

Send a small relative joint motion command using the official Doosan `MoveJoint`
service.

### Command

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_joint dsr_msgs2/srv/MoveJoint "{pos: [0.0, 0.0, 5.0, 0.0, 0.0, 0.0], vel: 10.0, acc: 10.0, time: 0.0, radius: 0.0, mode: 1, blend_type: 0, sync_type: 0}"
```

### Expected Result

The robot should execute a small relative joint movement.

Expected response:

```text
success=True
```

or an equivalent successful service response.

### Notes

This command uses:

```text
mode: 1
```

which means relative motion.

The movement is intentionally small for safer validation in virtual mode.

---

## Return from small relative MoveJoint motion

### Purpose

Return the robot approximately to the previous joint position after the small relative
motion test.

### Command

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_joint dsr_msgs2/srv/MoveJoint "{pos: [0.0, 0.0, -5.0, 0.0, 0.0, 0.0], vel: 10.0, acc: 10.0, time: 0.0, radius: 0.0, mode: 1, blend_type: 0, sync_type: 0}"
```

### Expected Result

The robot should execute a small relative joint movement in the opposite direction.

Expected response:

```text
success=True
```

or an equivalent successful service response.

### Notes

Use this after the previous relative movement test.

---

## Call MoveJoint service with absolute joint target

### Purpose

Send an absolute joint target to the Doosan `m1013` using the official `MoveJoint`
service.

### Command

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_joint dsr_msgs2/srv/MoveJoint "{pos: [0.0, 0.0, 90.0, 0.0, 90.0, 0.0], vel: 20.0, acc: 20.0, time: 0.0, radius: 0.0, mode: 0, blend_type: 0, sync_type: 0}"
```

### Expected Result

The robot should move to the requested absolute joint configuration.

Expected response:

```text
success=True
```

or an equivalent successful service response.

### Notes

This command uses:

```text
mode: 0
```

which means absolute motion.

Use this only in virtual mode unless the target has been reviewed for a real robot.

---

# 12. Recommended Validation Order

Use the following order when validating from a fresh terminal session.

## Terminal A — Launch Doosan virtual stack

```bash
cd ~/doosan_ws
source ~/doosan_ws/install/setup.bash
ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m1013
```

Keep this terminal open.

## Terminal B — Inspect ROS 2 graph

```bash
source ~/doosan_ws/install/setup.bash
ros2 node list
ros2 service list | grep dsr
ros2 service type /dsr01/dsr_controller2/motion/move_joint
ros2 interface show dsr_msgs2/srv/MoveJoint
```

## Terminal B — Run motion service test

```bash
ros2 service call /dsr01/dsr_controller2/motion/move_joint dsr_msgs2/srv/MoveJoint "{pos: [0.0, 0.0, 5.0, 0.0, 0.0, 0.0], vel: 10.0, acc: 10.0, time: 0.0, radius: 0.0, mode: 1, blend_type: 0, sync_type: 0}"
```

## Terminal A — Stop launch

```text
Ctrl+C
```

---

# 13. Command Documentation Template

Use this template when adding new validated commands:

```md
## Command title

### Purpose

Explain what the command does.

### Command

```bash
command_here
```

### Expected Result

Describe the expected output or behavior.

### Notes

Add any relevant context, warning, or requirement.
```
