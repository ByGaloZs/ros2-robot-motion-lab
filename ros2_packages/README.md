# ROS 2 Packages

## Purpose

This directory contains placeholders for future custom modules and ROS 2 packages
created specifically for this lab.

## Current Status

Base package folders exist, but no ROS 2 package code has been implemented yet.

## Rules

- Do not copy official Doosan packages into this directory.
- Do not place the validated official Doosan workspace here.
- Keep future packages small, focused, and documented.
- Keep general robot motion logic separate from robot-specific adapters.

## Planned Components

```text
pallet_layout_core      -> robot-agnostic layout generation
robot_motion_client    -> generic motion request and execution interface
doosan_motion_adapter  -> Doosan-specific ROS 2 adapter
```

`pallet_layout_core` is the next implementation target and should be pure Python at
first.

## Future Direction

Future package layers may be named:

```text
pallet_layout_core
robot_motion_client
doosan_motion_adapter
```

These package folders are placeholders. Implementation should only start after the
relevant responsibilities, interfaces, commands, and expected behavior are documented.

Do not create `setup.py`, `package.xml`, source code, nodes, launch files, or package
dependencies until implementation is explicitly requested.
