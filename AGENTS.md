# AGENTS.md

## Project Context

This repository is a general ROS 2 robot motion lab focused on modular robot motion, trajectory planning, and execution.

Doosan Robotics ROS 2 and the Doosan `m1013` are the current experimental validation platform. Do not design the whole project as Doosan-only.

The repository is intentionally separated from the validated official Doosan workspace.

Do not modify, move, copy, or assume control over:

```text
~/doosan_ws
```

That workspace is considered the validated Doosan ROS 2 environment.

This repository should remain focused on documentation, reproducible experiments, study notes, prototype scripts, and future custom ROS 2 packages.

## Architectural Direction

Future software should distinguish between:

```text
robot_motion_client
doosan_motion_adapter
```

Conceptual responsibilities:

- `robot_motion_client`: general robot motion client layer for motion requests, validation, and execution flow.
- `doosan_motion_adapter`: Doosan-specific communication through official Doosan ROS 2 services and interfaces.

Do not create these packages unless explicitly requested.

General logic should not depend directly on Doosan-specific service types, paths, or package names unless the task is explicitly about the Doosan adapter or Doosan validation experiments.

## Official References

Use these official references when working with ROS 2 or Doosan Robotics ROS 2:

- ROS 2 Jazzy documentation: https://docs.ros.org/en/jazzy/
- Doosan Robotics ROS 2 Jazzy manual: https://doosanrobotics.github.io/doosan-robotics-ros-manual/jazzy/index.html

When implementing or documenting ROS 2 behavior, prefer official documentation over assumptions.

Do not invent ROS 2 commands, Doosan services, message types, launch files, package names, or APIs. If something is unknown, inspect the local workspace or ask for clarification before making changes.

## Repository Language

Use English for folder names, file names, package names, code, comments, and documentation.

Keep technical writing clear, concise, and practical.

## Main Rules

1. Do not generate ROS 2 code unless explicitly requested.
2. Do not create ROS 2 packages unless explicitly requested.
3. Do not modify the official Doosan workspace.
4. Prefer small, incremental, maintainable changes.
5. Keep the repository simple and avoid overengineering.
6. Use official ROS 2 and Doosan interfaces when possible.
7. Do not invent APIs, packages, services, or commands.
8. When uncertain, inspect the existing project structure before proposing changes.

## Repository Structure

Expected structure:

```text
ros2-robot-motion-lab/
├── README.md
├── AGENTS.md
├── .gitignore
├── docs/
│   ├── context/
│   ├── architecture/
│   ├── study/
│   ├── experiments/
│   └── commands/
├── ros2_packages/
│   ├── pallet_layout_core/
│   ├── robot_motion_client/
│   └── doosan_motion_adapter/
├── apps/
│   └── pallet_layout_dashboard/
├── scripts/
└── reports/
```

## Directory Guidelines

### `docs/context/`

Use this directory for project context, thesis context, and environment status.

Recommended files:

```text
project-context.md
current-environment-status.md
thesis-context.md
```

### `docs/study/`

Use this directory for technical study notes about ROS 2, robot motion architecture, planning, simulation, and platform-specific interfaces.

### `docs/architecture/`

Use this directory for architecture boundaries, package responsibilities, data flow, and design decisions.

### `docs/experiments/`

Use this directory for reproducible experiment documentation.

Experiment files should follow this naming convention:

```text
EXP-0001-short-description.md
EXP-0002-short-description.md
EXP-0003-short-description.md
```

Doosan-specific experiment names may remain Doosan-specific because they validate the current experimental platform.

### `docs/commands/`

Use this directory for tested and validated commands.

Do not add commands unless they have a clear purpose and are known to be relevant.

### `ros2_packages/`

Use this directory only for future custom ROS 2 packages created specifically for this lab.

Current placeholders:

```text
pallet_layout_core
robot_motion_client
doosan_motion_adapter
```

These folders are placeholders only. Do not add ROS 2 package code, nodes, or business logic unless explicitly requested.

Do not copy official Doosan packages into this directory.

### `apps/`

Use this directory for future application-level interfaces.

Current placeholder:

```text
pallet_layout_dashboard
```

Do not add dashboard code unless explicitly requested.

### `scripts/`

Use this directory for small helper scripts and temporary prototypes only.

Do not place final ROS 2 package logic here.

### `reports/`

Use this directory for technical summaries, progress notes, and formal reports.

## ROS 2 Development Rules

When ROS 2 code is requested:

1. Prefer Python with `rclpy` unless another language is explicitly requested.
2. Use clear package names in English.
3. Keep nodes small and focused.
4. Separate ROS communication logic from application logic.
5. Keep robot-specific communication behind adapter boundaries when possible.
6. Use type hints where applicable.
7. Keep configuration external when it improves maintainability.
8. Do not depend on high-level wrappers unless explicitly required.

## Doosan Platform Notes

The currently validated movement service is:

```text
/dsr01/dsr_controller2/motion/move_joint
```

with type:

```text
dsr_msgs2/srv/MoveJoint
```

Treat this as the first concrete adapter target, not as the full project architecture.

## Documentation Rules

For every meaningful technical task, prefer documenting:

1. What is being tested or built.
2. Why it matters.
3. What interface, package, or command is involved.
4. What result is expected.
5. What result was obtained.
6. What the next step is.

## Experiment Documentation Template

Use this structure for experiment files:

```md
# EXP-XXXX — Experiment Title

## Objective

Describe what this experiment validates.

## Context

Briefly explain why this experiment is relevant.

## Preconditions

- TBD

## Interface or Tool Used

- TBD

## Steps

1. TBD

## Expected Result

TBD

## Actual Result

TBD

## Notes

TBD

## Conclusion

TBD

## Next Step

TBD
```

## Command Documentation Template

Use this structure when documenting validated commands:

````md
# Command Title

## Purpose

Explain what the command does.

## Command

```bash
command_here
```

## Expected Result

TBD

## Notes

TBD
````

## Code Style

When code is requested:

- use clear English names;
- prefer simple modules;
- include type hints when supported;
- write minimal comments only for non-obvious logic;
- avoid unnecessary abstractions;
- keep functions focused;
- avoid large files when a smaller module is clearer.

## Safety and Stability

Do not suggest destructive commands unless explicitly requested and clearly justified.

Avoid commands that delete, overwrite, or reset files without explaining the impact first.

Be especially careful with:

```bash
rm -rf
git reset --hard
sudo
colcon build --symlink-install
```

These commands may be valid in some contexts, but they should not be used casually.

## Git Guidelines

Prefer small commits with clear messages.

Recommended commit message style:

```text
Generalize project documentation
Document validated environment status
Add thesis context
Document motion experiment results
Prepare package architecture notes
```

Do not commit generated build artifacts, logs, ROS bag files, virtual environments, or local environment files.

## Current Project Status

The initial Doosan-based experiment sequence is complete. The current priority is to define the minimal future package architecture before creating ROS 2 package code.
