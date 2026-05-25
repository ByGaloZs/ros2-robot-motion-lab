# AGENTS.md

## Project Context

This repository is a general robot-agnostic modular robotics motion architecture lab. It supports a thesis-oriented software architecture project focused on modular motion systems, clear architectural boundaries, reproducible validation, and progressive integration from pure domain logic toward ROS 2 only when explicitly requested.

The architecture is robot-agnostic by design. Doosan ROS 2 is the current validation platform, not the architectural scope of the project.

The repository should remain focused on production-quality source code, formal documentation, reproducible experiments, validated commands, tests, examples, prototype scripts, and future custom ROS 2 packages when explicitly requested.

## Architectural Scope

The long-term architecture separates these responsibilities:

```text
ros2-robot-motion-lab/
├── domain modules
│   └── pure robot-agnostic computation
├── motion abstraction
│   └── general motion request, validation, and execution flow
├── robot-specific adapters
│   └── platform-specific communication behind adapter boundaries
├── apps
│   └── application interfaces, only when explicitly requested
├── docs
│   └── formal repository documentation and validated experiments
└── notebooks
    └── experiment notes, evidence, outputs, and analysis
```

Conceptual responsibilities:

- Domain modules: pure robot-agnostic logic that can be tested without ROS 2, robot hardware, simulators, dashboards, or vendor APIs.
- Motion abstraction: general motion request, validation, and execution-flow concepts.
- Robot-specific adapters: platform-specific communication through official vendor or ROS 2 interfaces.
- Apps: future application-level interfaces, only when explicitly requested.
- Docs and notebooks: formal documentation, reproducible experiment protocols, evidence, outputs, and analysis.

The architecture should remain transferable to other robots or validation platforms. General logic must not depend directly on Doosan-specific service types, paths, package names, MoveIt2, Gazebo, dashboard code, or robot-specific APIs.

Specific implementation modules must not redefine the repository scope. Domain modules must remain robot-agnostic, robot-specific execution must stay behind adapters, and validation platforms must not define the architecture.

Do not create or implement ROS 2 packages, nodes, launch files, `package.xml` files, or `rclpy` integrations unless explicitly requested.

## Current Validation Platform

Doosan Robotics ROS 2 and the Doosan `m1013` are the current experimental validation platform. They are relevant for validation experiments and future adapter work, but they must not become the conceptual center of the repository.

Doosan-specific logic belongs only behind adapter boundaries or inside documented Doosan validation experiments. Do not add Doosan service calls to robot-agnostic domain modules.

The repository is intentionally separated from the validated official Doosan workspace. Do not modify, move, copy, or assume control over:

```text
~/doosan_ws
```

That workspace is considered the validated official Doosan ROS 2 environment. Do not copy official Doosan packages into this repository.

The currently validated movement service is:

```text
/dsr01/dsr_controller2/motion/move_joint
```

with type:

```text
dsr_msgs2/srv/MoveJoint
```

Treat this as the first concrete adapter target, not as the full project architecture.

## External Knowledge Base

This repository is connected to an external Obsidian Vault used as a thesis-oriented knowledge base:

```text
/home/galozs-dev/Documents/Modular Robotics Architecture
```

The Vault is not part of this repository and must not be treated as source code or formal repository documentation.

Use the Vault for thesis context, research notes, source-backed knowledge, papers and official documentation captures, ROS 2 and Doosan knowledge synthesis, architecture reasoning, hypotheses, open questions, ADRs, experiment ideas, reusable AI prompts and workflows, and long-term project memory.

Use this repository for implementation, reproducible experiments, validated commands, formal project documentation, implementation notes, tests, examples, future ROS 2 packages when explicitly requested, and artifacts that directly support implementation and validation.

The Vault informs the repository.
The repository implements, documents, and validates.
The Vault does not replace formal repository documentation.

When an AI agent needs broader thesis context, research notes, source-backed knowledge, prior decisions, or reusable prompts, it may consult the Vault. When using the Vault:

1. Read this repository `AGENTS.md` first.
2. Read the Vault `AGENTS.md` before navigating the Vault.
3. Read `wiki/index.md` before navigating individual wiki pages.
4. Prefer processed knowledge in `wiki/`.
5. Use `sources/` only for verification, raw evidence, or source-level checks.
6. Do not modify Vault files unless the user explicitly requests Vault maintenance.
7. Do not copy raw Vault notes into repository documentation without explicit approval.
8. Do not treat the Vault as source code.
9. Do not treat the Vault as a replacement for repository documentation.
10. If a repository decision is derived from Vault knowledge, document the final decision inside the repository and optionally reference the Vault path.

## Agent Instruction Stability

`AGENTS.md` is a stable instruction file for AI agents. It is not a development log, experiment record, research note, or feature changelog.

Update `AGENTS.md` only when structural or long-term rules change, such as architectural boundaries, repository responsibilities, AI agent behavior, external knowledge base paths, validation platform strategy, or allowed and prohibited implementation behavior.

Do not update `AGENTS.md` for normal feature work, individual functions, small implementation changes, routine tests, regular experiment results, temporary notes, or short-term ideas.

Use this placement rule:

- If the change affects how an AI agent should behave in the project, update `AGENTS.md`.
- If the change explains what was done, use `docs/`.
- If the change captures research, reasoning, sources, or hypotheses, use the Vault.
- If the change is implementation, use the repository source tree.

## Repository Language

Use English for folder names, file names, package names, code, comments, and documentation.

Keep technical writing clear, concise, and practical.

## Main Rules

1. Do not generate ROS 2 code unless explicitly requested.
2. Do not create ROS 2 packages unless explicitly requested.
3. Do not create ROS 2 nodes, launch files, `package.xml` files, or `rclpy` integrations unless explicitly requested.
4. Do not modify the official Doosan workspace.
5. Do not copy official Doosan packages into this repository.
6. Prefer small, incremental, maintainable changes.
7. Keep the repository simple and avoid overengineering.
8. Separate robot-agnostic logic from robot-specific communication.
9. Keep robot-specific behavior behind adapter boundaries.
10. Use official ROS 2 and Doosan interfaces when possible.
11. Do not invent APIs, packages, services, commands, message types, or launch files.
12. When uncertain, inspect the existing project structure before proposing changes.

## Repository Structure

Expected structure:

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

## Directory Guidelines

### `docs/context/`

Use this directory for project context, thesis context, and environment status.

Recommended files:

```text
project-context.md
current-environment-status.md
thesis-context.md
```

### `docs/thesis_notes/`

Use this directory for repository-side thesis notes that directly support implementation or validation. Broader research notes, source synthesis, hypotheses, and long-term reasoning belong in the external Vault.

### `docs/implementation/`

Use this directory for implementation notes, assumptions, limitations, and module-level design details.

### `docs/templates/`

Use this directory for reusable repository documentation templates.

### `docs/architecture/`

Use this directory for architecture boundaries, package responsibilities, data flow, and design decisions that are formalized for this repository.

### `docs/experiments/`

Use this directory for reproducible experiment documentation.

The Markdown experiment files are the canonical protocols. Jupyter notebooks under `notebooks/experiments/` are complementary lab notes for results, outputs, and analysis. External evidence files should be stored under `notebooks/evidence/`.

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

Use this directory for custom modules and future ROS 2 packages created specifically for this lab.

Current and planned contents may include pure domain modules, motion abstractions, and robot-specific adapters. Do not let any single implementation module redefine the repository scope.

Existing implementation detail: `pallet_layout_core` is currently a pure Python, ROS-independent domain module with source code, tests, examples, and JSON export. It is not a ROS 2 package at this stage.

Do not add ROS 2 package code, nodes, launch files, `package.xml` files, or `rclpy` integration unless explicitly requested.

Do not copy official Doosan packages into this directory.

### `apps/`

Use this directory for future application-level interfaces.

Do not add dashboard or application code unless explicitly requested.

### `scripts/`

Use this directory for small helper scripts and temporary prototypes only.

Do not place final ROS 2 package logic here.

## Development Rules

When code is requested:

- Use clear English names.
- Prefer simple modules.
- Include type hints when supported.
- Write minimal comments only for non-obvious logic.
- Avoid unnecessary abstractions.
- Keep functions focused.
- Avoid large files when a smaller module is clearer.
- Keep pure domain logic independent from ROS 2, Doosan, MoveIt2, Gazebo, dashboard code, and robot-specific APIs.

When ROS 2 code is explicitly requested:

1. Prefer Python with `rclpy` unless another language is explicitly requested.
2. Use clear package names in English.
3. Keep nodes small and focused.
4. Separate ROS communication logic from application logic.
5. Keep robot-specific communication behind adapter boundaries when possible.
6. Use type hints where applicable.
7. Keep configuration external when it improves maintainability.
8. Do not depend on high-level wrappers unless explicitly required.

## Documentation Rules

For every meaningful technical task, prefer documenting:

1. What is being tested or built.
2. Why it matters.
3. What interface, package, or command is involved.
4. What result is expected.
5. What result was obtained.
6. What the next step is.

Architecture ideas from the external Vault should only be copied into this repository when they become actionable implementation documentation, ADRs, or experiment plans and the user has approved using that Vault content.

Do not treat the Vault as canonical for this repository unless the relevant concept is reflected in repository documentation such as `README.md`, `docs/architecture/`, `docs/implementation/`, or `docs/experiments/`.

## Experiment Documentation Template

Use this structure for experiment files:

```md
# EXP-XXXX - Experiment Title

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

## Official References

Use these official references when working with ROS 2 or Doosan Robotics ROS 2:

- ROS 2 Jazzy documentation: https://docs.ros.org/en/jazzy/
- Doosan Robotics ROS 2 Jazzy manual: https://doosanrobotics.github.io/doosan-robotics-ros-manual/jazzy/index.html

When implementing or documenting ROS 2 behavior, prefer official documentation over assumptions.

Do not invent ROS 2 commands, Doosan services, message types, launch files, package names, or APIs. If something is unknown, inspect the local workspace, consult official documentation, consult approved repository documentation, or ask for clarification before making changes.

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

## Change Policy

Keep this file stable and focused on agent behavior. Prefer changing repository documentation, experiment files, implementation notes, source code, tests, or the external Vault instead of changing `AGENTS.md` unless the change affects long-term agent instructions.
