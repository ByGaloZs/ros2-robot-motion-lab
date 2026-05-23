# Project Status

## Current Stage

TFM architecture consolidation and first robot-agnostic module implementation.

The project is currently focused on defining a modular robot motion architecture and
validating the first robot-agnostic layer before implementing ROS 2 integration packages.

## Completed

- Repository created for ROS 2 robot motion experimentation.
- Doosan Robotics identified as the current experimental validation platform.
- Base folders created for future custom modules.
- Documentation folders created for architecture, context, experiments, commands, and
  study notes.
- TFM context documented.
- Canonical TFM thesis definition documented.
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

1. Complete and review `pallet_layout_core v0.1`.
2. Document the `pallet_layout_core` walkthrough.
3. Close EXP-0009 after validating tests, generated output, and review evidence.
4. Define the intermediate representation schema.
5. Define Dashboard/UI requirements.
6. Define the `robot_motion_client` interface.
7. Define the `doosan_motion_adapter` mapping.
8. Define the first integration path from generated targets to motion requests.

## Not Started Yet

- `robot_motion_client` implementation.
- `doosan_motion_adapter` implementation.
- Dashboard implementation.
- Trajectory optimization.
- Experimental comparison between monolithic and modular architecture.
