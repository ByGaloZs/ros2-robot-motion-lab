# Project Status

## Current Stage

TFM architecture consolidation and robot-agnostic module boundary review.

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
- Initial robot-agnostic domain module implemented as pure Python under
  `ros2_packages/pallet_layout_core`.
- Source code, tests, example script, and JSON export are present for the initial domain
  module.
- Generated JSON evidence exists for EXP-0009 under
  `notebooks/evidence/EXP-0009/generated_outputs/`.
- Isolated unit test command for the initial domain module validated with
  `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` to avoid ROS 2 pytest plugin autoloading.

## In Progress

- Defining the modular architecture.
- Separating robot-agnostic motion concepts from Doosan-specific execution.
- Reviewing and documenting the robot-agnostic domain module boundary.
- Keeping the repository aligned with the TFM direction.

## Next Steps

1. Review and document the robot-agnostic domain module boundary.
2. Document module walkthroughs only when they clarify architectural boundaries.
3. Define whether the current JSON output needs a stricter intermediate representation
   schema.
4. Define Dashboard/UI requirements.
5. Define the `robot_motion_client` interface.
6. Define the `doosan_motion_adapter` mapping.
7. Define the first integration path from generated targets to motion requests.

## Not Started Yet

- `robot_motion_client` implementation.
- `doosan_motion_adapter` implementation.
- Dashboard implementation.
- Trajectory optimization.
- Experimental comparison between monolithic and modular architecture.
