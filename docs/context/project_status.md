# Project Status

## Current Stage

Repository architecture preparation before implementing custom ROS 2 packages.

The project is currently focused on organizing the codebase and documentation for a
modular robot motion architecture that can later be validated using Doosan Robotics ROS
2.

## Completed

- Repository created for ROS 2 robot motion experimentation.
- Doosan Robotics identified as the current experimental validation platform.
- Base folders created for future custom modules.
- Documentation folders created for architecture, context, experiments, commands, and
  study notes.
- TFM context documented.
- Initial experiment documentation started.

## In Progress

- Defining the modular architecture.
- Separating robot-agnostic motion concepts from Doosan-specific execution.
- Preparing the future pallet layout generation pipeline.
- Scaffold started for `pallet_layout_core` v0.1 as a pure Python module.
- Verified the isolated unit test command for `pallet_layout_core` using
  `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` to avoid ROS 2 pytest plugin autoloading.
- Keeping the repository aligned with the TFM direction.

## Next Steps

1. Implement the first version of `pallet_layout_core`. 2. Define data models for boxes,
pallets, layers, slots, and target poses. 3. Generate static pallet layouts from JSON
input. 4. Export calculated target poses as JSON. 5. Add unit tests for layout
generation. 6. Later connect generated poses to `robot_motion_client`. 7. Later
implement `doosan_motion_adapter`. 8. Later create a minimal `pallet_layout_dashboard`
for visual validation.

## Not Started Yet

- `robot_motion_client` implementation.
- `doosan_motion_adapter` implementation.
- Dashboard implementation.
- Trajectory optimization.
- Experimental comparison between monolithic and modular architecture.
