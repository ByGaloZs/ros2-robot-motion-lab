# `pallet_layout_core` Implementation Notes

## Purpose

This module generates robot-agnostic pallet layouts, layers, slots, and target poses.

The v0.1 scaffold has started as a pure Python package under
`ros2_packages/pallet_layout_core`.

## Scope

This module is responsible for:

- Box dimensions.
- Pallet dimensions.
- Layer generation.
- Slot generation.
- Target pose calculation.
- JSON export.

This module is not responsible for:

- ROS 2 node execution.
- Doosan service calls.
- MoveIt2 planning.
- Gazebo simulation.
- Robot kinematics.
- Dashboard UI.

## Coordinate Convention

- The pallet origin is located at the lower-left corner of the pallet footprint.
- X follows the pallet length.
- Y follows the pallet width.
- Z follows the pallet height.
- Slot positions represent the geometric center of each box.

## Initial Position Formula

```text
x = box.length / 2 + column_index * box.length
y = box.width / 2 + row_index * box.width
z = pallet.height + box.height / 2 + layer_index * box.height
```

## Initial Supported Pattern

Only the `grid` pattern is supported in the first version.

## Test Isolation

`pallet_layout_core` is tested as a pure Python module.

Because the development machine may have ROS 2 Jazzy sourced globally, pytest can discover
and autoload ROS 2 testing plugins such as `launch_testing`.

This module does not require ROS 2 during unit testing. Therefore, unit tests should be
executed with pytest plugin autoloading disabled:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest ros2_packages/pallet_layout_core/tests -q
```

This keeps the test environment aligned with the module scope:

- No ROS 2 dependency.
- No Doosan dependency.
- No MoveIt2 dependency.
- No Gazebo dependency.
- No ROS 2 pytest plugin dependency.

## Known Limitations

- Only rectangular pallets are supported.
- Only one box type is supported.
- Only one orientation is supported initially.
- No collision checking is performed.
- No robot reachability validation is performed.
- No trajectory generation is performed.
