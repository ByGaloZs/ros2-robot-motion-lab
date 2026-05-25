# ROS 2 Robot Motion Lab

## Purpose

This repository is a general modular robotics motion architecture lab focused on
robot-agnostic domain logic, motion abstraction, robot-specific adapters, reproducible
validation, and formal documentation.

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
│   │   └── decisions/
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
│   └── custom modules and future ROS 2 packages
├── apps/
│   └── future application-level interfaces
└── scripts/
    ├── prototypes/
    ├── setup/
    └── utilities/
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

Future software should separate domain computation, motion requests, robot-specific
communication, validation workflows, and application interfaces.

Planned conceptual layers:

- Domain modules: pure robot-agnostic computation.
- Motion abstraction: general motion requests, validation, and execution flow.
- Robot-specific adapters: platform communication through official interfaces.
- Application interfaces: configuration, visualization, supervision, and reproducibility
  when explicitly requested.

Current implementation detail: `pallet_layout_core` is an initial pure Python,
robot-agnostic domain module under `ros2_packages/pallet_layout_core/`. It is not the
repository identity or final thesis scope.

No ROS 2 package implementation, robot adapter logic, or dashboard application code has
been implemented yet.

The next implementation targets should be selected from architecture needs, validated
experiment results, and explicit user direction rather than from any single current
module.
