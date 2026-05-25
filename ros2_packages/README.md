# ROS 2 Packages

## Purpose

This directory contains custom modules and future ROS 2 packages created specifically for
this lab.

The repository architecture separates robot-agnostic domain logic from motion abstraction
and robot-specific adapters. This keeps reusable computation independent from the current
Doosan validation platform.

## Current Status

The current implemented module is `pallet_layout_core`.

`pallet_layout_core` is a pure Python, robot-agnostic module with source code, tests,
examples, JSON export, and a validated isolated pytest command. It is not a ROS 2 package
at this stage and must not depend on ROS 2, Doosan Robotics, MoveIt2, Gazebo, or dashboard
code.

The `robot_motion_client` and `doosan_motion_adapter` folders remain placeholders for
future ROS 2 package work.

## Rules

- Do not copy official Doosan packages into this directory.
- Do not place the validated official Doosan workspace here.
- Keep custom modules small, focused, and documented.
- Keep general robot motion logic separate from robot-specific adapters.
- Do not add ROS 2 dependencies to robot-agnostic modules unless their scope changes and
  the architecture is documented first.

## Current And Planned Components

```text
domain modules          -> pure robot-agnostic computation
motion abstraction      -> future generic motion request and execution interface
robot-specific adapters -> future platform-specific ROS 2 adapters
```

## `pallet_layout_core`

`pallet_layout_core` is responsible for generating deterministic pallet layout data from
box and pallet dimensions.

It currently provides a minimal v0.1 implementation for grid-based layouts, including
unit tests, an example script, and JSON output used as experiment evidence.

Current scope:

- box and pallet dimensions;
- layout configuration;
- grid layer generation;
- slot generation;
- target pose calculation;
- JSON export.

Out of scope:

- ROS 2 nodes;
- `rclpy` integration;
- Doosan service calls;
- MoveIt2 planning;
- Gazebo simulation;
- dashboard UI;
- robot reachability or trajectory optimization.

Recommended isolated test command from the repository root:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest ros2_packages/pallet_layout_core/tests -q
```

`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` prevents pytest from loading ROS 2 pytest plugins from a
globally sourced ROS 2 environment.

Validated scaffold result:

```text
10 passed in 0.03s
```

See also:

- `ros2_packages/pallet_layout_core/README.md`
- `docs/implementation/pallet_layout_core_notes.md`
- `docs/commands/validated-commands.md`

## Future Direction

Future package layers should remain separated by responsibility. Implementation of motion
abstractions and robot-specific adapters should only start after the relevant interfaces,
commands, and expected behavior are documented.

Do not create ROS 2 nodes, launch files, `package.xml` files, or ROS 2 package dependencies
for these future layers until implementation is explicitly requested.
