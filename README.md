# Doosan ROS 2 Lab

A technical lab for documenting and experimenting with **ROS 2 Jazzy** and **Doosan Robotics ROS 2** using the Doosan `m1013` as an experimental platform.

## Purpose

This repository is intended to provide a clean and organized workspace for:

- documenting the validated environment;
- keeping technical study notes;
- registering tested commands;
- documenting reproducible experiments;
- preparing future custom ROS 2 packages;
- exploring robot simulation, motion control, and trajectory planning.

## Validated Environment

The current environment has been installed and tested with:

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Doosan Robotics ROS 2
- Doosan `m1013`
- Docker Emulator `doosanrobot/dsr_emulator:3.0.1`
- RViz2
- MoveIt2
- Gazebo
- Python / `rclpy`

## Repository Structure

```text
doosan-ros2-lab/
├── README.md
├── .gitignore
├── docs/
│   ├── context/
│   ├── study/
│   ├── experiments/
│   └── commands/
├── ros2_packages/
├── scripts/
└── reports/
```

## Main Directories

### `docs/context/`

General project context and current environment status.

### `docs/study/`

Technical study notes about ROS 2, Doosan Robotics ROS 2, services, simulation, and modular robotics architecture.

### `docs/experiments/`

Reproducible technical experiments and validation notes.

### `docs/commands/`

Tested and validated commands used during the lab setup and experiments.

### `ros2_packages/`

Future custom ROS 2 packages.

### `scripts/`

Auxiliary scripts for local tasks and small utilities.

### `reports/`

Technical reports, summaries, and progress documents.

## Current Direction

The next technical goal is to prepare a custom ROS 2 package, for example:

```text
doosan_motion_client
```

This package should control the robot directly through:

- `dsr_msgs2`
- `dsr_controller2`
- official ROS 2 services
- Python / `rclpy`

The long-term goal is to avoid depending on high-level wrappers for the core lab experiments and to build a clearer understanding of the official Doosan ROS 2 service interfaces.
