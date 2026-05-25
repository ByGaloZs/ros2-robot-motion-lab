# Current Environment Status

## Purpose

Track the currently validated experimental environment for this ROS 2 robot motion lab.

## Scope

This document describes the environment used for `ros2-robot-motion-lab`.

Do not treat this repository as the validated official Doosan workspace. The official
validated workspace remains separate at:

```text
~/doosan_ws
```

## Current Experimental Environment

- Operating system: Ubuntu 24.04 LTS
- ROS 2 distribution: Jazzy
- Doosan Robotics ROS 2: installed in the separate validated workspace
- Robot model used for experiments: Doosan `m1013`
- Docker Emulator: `doosanrobot/dsr_emulator:3.0.1`
- Visualization: RViz2
- Planning: MoveIt2
- Simulation: Gazebo
- Python client library: `rclpy`
- Repository phase: modular architecture consolidation after completing the initial
  Doosan-based experiment sequence
- ROS 2 package code in this repository: not implemented yet
- Pure Python module code in this repository: initial robot-agnostic domain module present
- Dashboard code in this repository: not implemented yet
- Prototype scripts in this repository: one Python `rclpy` service client prototype

## Repository Status

- Documentation directories are present.
- Architecture documentation directory is present.
- Experiment documentation is present under `docs/experiments/`.
- Base package folders are present under `ros2_packages/`.
- One robot-agnostic implementation module is present as an initial validation input.
- Base application folder is present under `apps/`.
- A prototype script is present under `scripts/prototypes/`.
- `robot_motion_client`, `doosan_motion_adapter`, and application folders remain
  placeholders.

## Validation Status

The initial experiment sequence validates the current Doosan-based experimental
platform. These results support the broader ROS 2 robot motion architecture but should
not force the general layer to become Doosan-specific.

Validated areas include:

- direct `MoveJoint` service control;
- ROS 2 graph and robot state inspection;
- Doosan service and interface mapping;
- `MoveLine` Cartesian motion;
- MoveIt2 planning and execution;
- Gazebo simulation;
- motion command failure handling;
- a Python `rclpy` service client prototype.

## Next Step

Define the intermediate representation schema and the next integration boundary without
letting any single current implementation module define the repository scope.
