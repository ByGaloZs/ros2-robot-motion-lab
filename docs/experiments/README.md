# Experiments

This folder contains reproducible technical experiments for the ROS 2 robot motion lab.

The first experiments were environment and ROS 2 validation experiments performed before
implementing the custom modular architecture.

The Markdown files in this folder are the canonical experiment protocols. Complementary
Jupyter notebooks live under `../../notebooks/experiments/` and can be used as lab notes
for terminal outputs, evidence links, generated data, plots, and analysis.

External evidence files should be stored under `../../notebooks/evidence/`, organized by
experiment ID.

## Experiment Index

- [Experiment Log](experiment-log.md)
- [EXP-0001: MoveJoint Service Validation](EXP-0001-move-joint-service-validation.md)
  ([notebook](../../notebooks/experiments/EXP-0001-move-joint-service-validation.ipynb))
- [EXP-0002: Robot State Inspection](EXP-0002-robot-state-inspection.md)
  ([notebook](../../notebooks/experiments/EXP-0002-robot-state-inspection.ipynb))
- [EXP-0003: Doosan Services and Interfaces
  Mapping](EXP-0003-doosan-services-and-interfaces-mapping.md)
  ([notebook](../../notebooks/experiments/EXP-0003-doosan-services-and-interfaces-mapping.ipynb))
- [EXP-0004: MoveLine Service Validation](EXP-0004-moveline-service-validation.md)
  ([notebook](../../notebooks/experiments/EXP-0004-moveline-service-validation.ipynb))
- [EXP-0005: MoveIt2 Planning Validation](EXP-0005-moveit2-planning-validation.md)
  ([notebook](../../notebooks/experiments/EXP-0005-moveit2-planning-validation.ipynb))
- [EXP-0006: Gazebo Simulation Validation](EXP-0006-gazebo-simulation-validation.md)
  ([notebook](../../notebooks/experiments/EXP-0006-gazebo-simulation-validation.ipynb))
- [EXP-0007: Motion Command Failure
  Handling](EXP-0007-motion-command-failure-handling.md)
  ([notebook](../../notebooks/experiments/EXP-0007-motion-command-failure-handling.ipynb))
- [EXP-0008: Python rclpy Service Client
  Prototype](EXP-0008-python-rclpy-service-client-prototype.md)
  ([notebook](../../notebooks/experiments/EXP-0008-python-rclpy-service-client-prototype.ipynb))
- [EXP-0009: Pallet Layout Core v0.1](EXP-0009-pallet-layout-core-v0.1.md)
  ([notebook](../../notebooks/experiments/EXP-0009-pallet-layout-core-v0.1.ipynb))

## Future Validation Areas

Future experiments will validate custom modules and integration paths such as:

- `pallet_layout_core`
- `robot_motion_client`
- `doosan_motion_adapter`
- dashboard preview
- RViz pose visualization
- MoveIt2 planning
- Gazebo simulation
