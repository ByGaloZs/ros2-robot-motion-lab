# Scripts

## Purpose

This directory is reserved for small helper scripts used by this lab.

## Layout

- `prototypes/`: temporary scripts used to validate an idea or experiment before package
  implementation.
- `setup/`: future setup helpers for repeatable environment preparation.
- `utilities/`: future small utilities for repository maintenance or experiment support.

## Current Status

A prototype script has been added for experiment validation:

```text
prototypes/move_joint_client.py
```

This script is a temporary Python `rclpy` prototype for calling the official Doosan
`MoveJoint` service. It is not the final ROS 2 package structure.

Before running it, source ROS 2 Jazzy and the validated Doosan workspace:

```bash
source /opt/ros/jazzy/setup.bash
source /home/galozs-dev/doosan_ws/install/setup.bash
```

## Rules

- Keep scripts small and practical.
- Do not place core ROS 2 package logic here.
- Do not use scripts to modify the official Doosan workspace.
- Document script purpose and usage before relying on it for experiments.
- Do not add executable scripts unless they are needed for a documented task or
  experiment.
