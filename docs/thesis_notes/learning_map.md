# Learning Map

## Purpose

Organize the study path for this ROS 2 robot motion lab.

## Current Focus

The repository has completed the initial Doosan-based validation sequence. The priority is
to consolidate the TFM thesis definition, complete `pallet_layout_core v0.1`, and define
the next architecture boundaries before creating ROS 2 package code.

## Study Areas

1. TFM thesis definition and research framing.
2. Modular software architecture for robotic motion.
3. ROS 2 Jazzy basics.
4. ROS 2 nodes, topics, services, and messages.
5. Python client libraries with `rclpy`.
6. Robot-agnostic layout generation.
7. Intermediate target representation and JSON schema design.
8. Dashboard/UI requirements for configuration and supervision.
9. Robot motion client architecture.
10. Robot-specific adapter boundaries.
11. RViz2 visualization workflow.
12. MoveIt2 planning workflow.
13. Gazebo simulation workflow.
14. Current Doosan experimental platform and emulator usage.
15. Reproducible experiment documentation.

## Known Future Direction

`pallet_layout_core` is the first implemented robot-agnostic layer. Future custom ROS 2
packages may be created under `ros2_packages/`, but no ROS 2 code should be added before
the `robot_motion_client` and `doosan_motion_adapter` responsibilities are defined.

## Next Step

Use `tfm-thesis-definition.md` as the current reference when adding focused study notes or
new experiments.
