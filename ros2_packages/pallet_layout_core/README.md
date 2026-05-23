# pallet_layout_core

Pure Python core module for generating robot-agnostic pallet layouts, layers, slots,
and target poses from box and pallet dimensions.

## Purpose

`pallet_layout_core` prepares deterministic palletizing layout data that can later be
consumed by robot motion clients, adapters, or visualization tools.

## Scope

- Box dimensions.
- Pallet dimensions.
- Layout configuration.
- Grid layer generation.
- Slot generation.
- Target pose calculation.
- JSON export.

## Out of Scope

- ROS 2 nodes or `rclpy` integration.
- Doosan service calls.
- Robot kinematics.
- MoveIt2 planning.
- Gazebo simulation.
- Dashboard UI.
- Collision, reachability, or trajectory optimization.

## Coordinate Convention

- The pallet origin is the lower-left corner of the pallet footprint.
- X follows pallet length.
- Y follows pallet width.
- Z follows pallet height.
- Target positions represent each box center.
- Orientation defaults to `rx=0.0`, `ry=0.0`, `rz=0.0`.

## Supported Pattern

Version 0.1 supports only the `grid` pattern.

## Example Input

- Box: 300 x 200 x 150 mm.
- Pallet: 1200 x 1000 x 150 mm.
- Layers: 3.
- Pattern: `grid`.

## Expected Output

- Generated layers: 3.
- Generated slots per layer: 20.
- Generated total slots: 60.

## Running Tests

From the repository root, activate the virtual environment:

```bash
source .venv/bin/activate
```

Then run:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest ros2_packages/pallet_layout_core/tests -q
```

`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` is used because this package is tested as a pure Python
module.

In a ROS 2 development environment, pytest may otherwise attempt to autoload ROS 2 testing
plugins such as `launch_testing`, even though this package does not depend on ROS 2.

## Run Example

From the repository root:

```bash
PYTHONPATH=ros2_packages/pallet_layout_core/src python ros2_packages/pallet_layout_core/examples/generate_basic_layout.py
```

The example writes JSON to:

```text
reports/generated_outputs/pallet_layout_core_v0.1/basic_layout.json
```
