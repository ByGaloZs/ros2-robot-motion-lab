# Learning Map

## Purpose

Organize the study path for this ROS 2 robot motion lab.

## Current Focus

The repository has completed the initial Doosan-based validation sequence. The priority
is to define a modular robot motion architecture before creating ROS 2 package code.

## Study Areas

1. ROS 2 Jazzy basics 2. ROS 2 nodes, topics, services, and messages 3. Python client
libraries with `rclpy` 4. Robot motion client architecture 5. Robot-specific adapter
boundaries 6. RViz2 visualization workflow 7. MoveIt2 planning workflow 8. Gazebo
simulation workflow 9. Current Doosan experimental platform and emulator usage
10. Reproducible experiment documentation

## Known Future Direction

Future custom modules and ROS 2 packages may be created under `ros2_packages/`, but no
ROS 2 code should be added before the minimal `pallet_layout_core`,
`robot_motion_client`, and `doosan_motion_adapter` responsibilities are defined.

## Next Step

Create focused study notes as each topic is reviewed and validated.
