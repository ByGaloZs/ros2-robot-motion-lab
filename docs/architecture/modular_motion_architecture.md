# Modular Motion Architecture

## Purpose

The goal is to separate robot-agnostic domain computation, motion requests,
robot-specific execution, validation workflows, and application interfaces so they can
evolve independently.

## Architecture Overview

```text
User / Operator
      ↓
Dashboard / UI
      ↓
Application API / Backend
      ↓
Robot-Agnostic Domain Modules
      ↓
Intermediate Target Representation
      ↓
Motion Abstraction
      ↓
Robot-Specific Adapter
      ↓
ROS 2 / MoveIt2 / Gazebo / Emulator / Robot Platform
```

## Components

### Robot-Agnostic Domain Modules

Domain modules contain pure task or scenario computation:

- Input models and validation
- Scenario or target generation
- Deterministic outputs for tests and experiments
- Export to documented intermediate representations when needed

They must remain robot-agnostic and should not depend on Doosan, ROS 2 execution details,
MoveIt2, Gazebo, robot-specific APIs, or Dashboard/UI code.

Current status: one pure Python domain module exists as an initial implementation detail.

### Intermediate Target Representation / JSON

This layer provides a stable data format between domain modules, visualization, motion
clients, and future adapters.

Current status: partially explored through JSON export from the first domain module.

### Motion Abstraction

This module will define the general motion interface:

- Motion targets
- Motion requests
- Motion sequences
- Execution results

It should represent generic robot motion concepts without depending directly on any
specific robot platform.

Current status: placeholder / future implementation.

### Robot-Specific Adapter

Adapters translate generic motion requests into concrete platform interfaces.

The current validation platform implies a future Doosan-specific adapter, but that adapter
does not define the general architecture.

Current status: placeholder / future implementation.

### Application Interface

Future apps are formal application layers. They may allow a user or operator to configure
and supervise validation scenarios, including:

- Domain-specific inputs
- Generated targets
- Target poses
- Intermediate representations
- Validation results

It should be used first as a validation tool before sending generated poses to the
robot.

Application interfaces must not contain core domain computation or robot-specific
execution logic.

Current status: planned / not implemented yet.

## Design Principle

- Keep domain computation independent from robot execution.
- Keep generic motion concepts separate from vendor-specific adapters.
- Use Doosan as an experimental platform, not as the architectural boundary.
- Keep dependencies flowing from upper layers to lower layers, not from domain modules
  back into UI or robot-specific layers.
