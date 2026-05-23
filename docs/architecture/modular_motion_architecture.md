# Modular Motion Architecture

## Purpose

The goal is to separate robot-agnostic motion concepts from robot-specific execution so
that layout generation, motion requests, and vendor-specific communication can evolve
independently.

## Architecture Overview

```text
User / Operator
      ↓
Dashboard / UI
      ↓
Application API / Backend
      ↓
pallet_layout_core
      ↓
Intermediate Target Representation / JSON
      ↓
robot_motion_client
      ↓
doosan_motion_adapter
      ↓
Doosan ROS 2 / MoveIt2 / Gazebo / Emulator
```

## Components

### `pallet_layout_core`

This module contains pure layout logic:

- Box dimensions
- Pallet dimensions
- Layers
- Slots
- Target pose generation
- JSON export

It must remain robot-agnostic and should not depend on Doosan, ROS 2 execution details,
MoveIt2, Gazebo, or Dashboard/UI code.

Current status: implemented as a pure Python module.

### Intermediate Target Representation / JSON

This layer provides a stable data format between layout generation, visualization, motion
clients, and future adapters.

Current status: partially implemented through JSON export from `pallet_layout_core`.

### `robot_motion_client`

This module will define the general motion interface:

- Motion targets
- Motion requests
- Motion sequences
- Execution results

It should represent generic robot motion concepts without depending directly on Doosan.

Current status: placeholder / future implementation.

### `doosan_motion_adapter`

This adapter will translate generic motion requests into Doosan ROS 2 service calls.

It is the Doosan-specific implementation layer.

Current status: placeholder / future implementation.

### `pallet_layout_dashboard`

This future app is a formal application layer. It will allow a user or operator to
configure and supervise palletizing scenarios, including:

- Pallet layouts
- Layers
- Slots
- Box positions
- Target poses
- Intermediate JSON or target data
- Validation results

It should be used first as a validation tool before sending generated poses to the
robot.

The dashboard must not contain core layout generation or Doosan-specific execution logic.

Current status: planned / not implemented yet.

## Design Principle

- Keep layout generation independent from robot execution.
- Keep generic motion concepts separate from vendor-specific adapters.
- Use Doosan as an experimental platform, not as the architectural boundary.
- Keep dependencies flowing from upper layers to lower layers, not from core modules back
  into UI or robot-specific layers.
