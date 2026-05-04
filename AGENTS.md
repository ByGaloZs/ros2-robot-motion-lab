# AGENTS.md

## Project Context

This repository is a technical lab for documenting and experimenting with **ROS 2 Jazzy** and **Doosan Robotics ROS 2** using the Doosan `m1013` as an experimental platform.

The repository is intentionally separated from the validated official Doosan workspace.

Do not modify, move, or assume control over:

```text
~/doosan_ws
```

That workspace is considered the validated Doosan ROS 2 environment.

This repository should remain focused on documentation, reproducible experiments, study notes, and future custom ROS 2 packages.

## Repository Language

Use English for:

- folder names;
- file names;
- package names;
- class names;
- function names;
- variables;
- comments;
- documentation.

Keep technical writing clear, concise, and practical.

## Main Rules

1. Do not generate complex ROS 2 code unless explicitly requested.
2. Do not modify the official Doosan workspace.
3. Prefer small, incremental, maintainable changes.
4. Document the reason for technical decisions when relevant.
5. Keep the repository simple and avoid overengineering.
6. Use official ROS 2 and Doosan interfaces when possible.
7. Do not invent APIs, packages, services, or commands.
8. When uncertain, inspect the existing project structure before proposing changes.

## Repository Structure

Expected structure:

```text
doosan-ros2-lab/
├── README.md
├── AGENTS.md
├── .gitignore
├── docs/
│   ├── context/
│   ├── study/
│   ├── experiments/
│   └── commands/
├── ros2_packages/
├── scripts/
└── reports/
```

## Directory Guidelines

### `docs/context/`

Use this directory for project context and environment status.

Recommended files:

```text
project-context.md
current-environment-status.md
```

### `docs/study/`

Use this directory for technical study notes.

Examples:

```text
ros2-basics.md
doosan-ros2-services.md
motion-control-notes.md
simulation-notes.md
```

### `docs/experiments/`

Use this directory for reproducible experiment documentation.

Experiment files should follow this naming convention:

```text
EXP-0001-short-description.md
EXP-0002-short-description.md
EXP-0003-short-description.md
```

### `docs/commands/`

Use this directory for tested and validated commands.

Do not add commands unless they have a clear purpose and are known to be relevant.

### `ros2_packages/`

Use this directory only for future custom ROS 2 packages created specifically for this lab.

Do not copy official Doosan packages into this directory.

### `scripts/`

Use this directory for small helper scripts only.

Do not place core ROS 2 package logic here.

### `reports/`

Use this directory for technical summaries, progress notes, and formal reports.

## ROS 2 Development Rules

When ROS 2 code is requested:

1. Prefer Python with `rclpy` unless another language is explicitly requested.
2. Use clear package names in English.
3. Keep nodes small and focused.
4. Separate ROS communication logic from application logic.
5. Use type hints where applicable.
6. Avoid global mutable state when possible.
7. Keep configuration external when it improves maintainability.
8. Do not depend on high-level wrappers unless explicitly required.

Future package direction:

```text
doosan_motion_client
```

This package should eventually communicate directly with:

- `dsr_msgs2`
- `dsr_controller2`
- official ROS 2 services
- Python / `rclpy`

## Doosan ROS 2 Notes

The validated movement service is:

```text
/dsr01/dsr_controller2/motion/move_joint
```

with type:

```text
dsr_msgs2/srv/MoveJoint
```

The project should favor direct use of official ROS 2 services instead of relying on high-level wrappers for core experiments.

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

```md
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
```

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
git clean -fd
sudo
colcon build --symlink-install
```

These commands may be valid in some contexts, but they should not be used casually.

## Git Guidelines

Prefer small commits with clear messages.

Recommended commit message style:

```text
Add initial project documentation
Document validated environment status
Add ROS 2 study notes
Document MoveJoint service validation
Prepare initial ROS 2 package structure
```

Do not commit generated build artifacts, logs, ROS bag files, virtual environments, or local environment files.

## Current Project Status

The repository is in the initial documentation and structure phase.

Current priority:

1. Keep the repository clean.
2. Document the validated environment.
3. Build study notes before writing complex code.
4. Create reproducible experiments.
5. Prepare future ROS 2 packages incrementally.
