# ROS 2 Robot Motion Lab

## Purpose

This repository is a general ROS 2 robot motion architecture lab focused on modular
robot motion, trajectory planning, and execution.

It is used to document validated commands, reproducible experiments, prototype scripts,
and future package design for robot motion software. The repository also supports
preparation for a future master's thesis / TFM, but it remains a practical engineering
lab rather than a thesis manuscript.

## Current Experimental Platform

The current validation platform is:

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Doosan Robotics ROS 2
- Doosan `m1013`
- Docker Emulator `doosanrobot/dsr_emulator:3.0.1`
- RViz2
- MoveIt2
- Gazebo
- Python / `rclpy`

Doosan Robotics ROS 2 and the Doosan `m1013` are the current experimental validation
platform. They are not intended to define the full scope of the repository.

The validated Doosan workspace remains separate at:

```text
~/doosan_ws
```

## Repository Structure

```text
ros2-robot-motion-lab/
├── README.md
├── AGENTS.md
├── .gitignore
├── docs/
│   ├── architecture/
│   ├── commands/
│   ├── context/
│   ├── experiments/
│   ├── implementation/
│   ├── thesis_notes/
│   └── templates/
├── notebooks/
│   ├── evidence/
│   ├── experiments/
│   └── templates/
├── ros2_packages/
│   ├── pallet_layout_core/
│   ├── robot_motion_client/
│   └── doosan_motion_adapter/
├── apps/
│   └── pallet_layout_dashboard/
└── scripts/
```

## Documentation Structure

- `docs/architecture/`: architecture design and ADRs.
- `docs/context/`: project and TFM context.
- `docs/experiments/`: reproducible technical experiments.
- `docs/implementation/`: implementation notes.
- `docs/thesis_notes/`: rough notes for future TFM writing.
- `docs/templates/`: reusable documentation templates.
- `notebooks/`: Jupyter notebooks for experiment notes, evidence, and analysis.
- `docs/commands/`: validated commands.

The repository is intentionally structured to support future TFM writing. Experiments,
ADRs, implementation notes, and generated outputs should be cross-referenced when
relevant.

Markdown experiment files are the canonical experiment protocols. Jupyter notebooks are
complementary lab notes for recording terminal outputs, evidence links, generated data,
plots, and lightweight analysis. Robot motion commands should remain in validated
terminals or scripts unless an experiment explicitly requires notebook execution.

Experiment evidence and generated outputs should be stored under `notebooks/evidence/`
and referenced from the matching notebook.

## Future Direction

Future software should separate general robot motion logic from robot-specific
communication.

Planned conceptual layers:

- `pallet_layout_core`: future pallet layout and trajectory generation logic.
- `robot_motion_client`: general robot motion client layer for motion requests,
  validation, and execution flow.
- `doosan_motion_adapter`: Doosan-specific adapter for official Doosan ROS 2 services
  and interfaces.
- `pallet_layout_dashboard`: future application interface for pallet layout
  visualization and interaction.

Only the base folder structure exists. No ROS 2 package logic, nodes, or dashboard code
has been implemented yet.

The current next implementation target is `pallet_layout_core v0.1`, before the
dashboard or Doosan-specific adapter.
