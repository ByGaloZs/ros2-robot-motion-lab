# Modular Motion Architecture

## Purpose

The goal is to separate robot-agnostic motion concepts from robot-specific execution so
that layout generation, motion requests, and vendor-specific communication can evolve
independently.

## Architecture Overview

```text
pallet_layout_core
        ↓
robot_motion_client
        ↓
doosan_motion_adapter
        ↓
Doosan ROS 2 / simulator / robot platform
```

## Components

### `pallet_layout_core`

This module will contain pure layout logic:

- Box dimensions
- Pallet dimensions
- Layers
- Slots
- Target pose generation
- JSON export

It must remain robot-agnostic and should not depend on Doosan or ROS 2 execution
details.

### `robot_motion_client`

This module will define the general motion interface:

- Motion targets
- Motion requests
- Motion sequences
- Execution results

It should represent generic robot motion concepts without depending directly on Doosan.

### `doosan_motion_adapter`

This adapter will translate generic motion requests into Doosan ROS 2 service calls.

It is the Doosan-specific implementation layer.

### `pallet_layout_dashboard`

This future app will visualize:

- Pallet layouts
- Layers
- Slots
- Box positions
- Target poses

It should be used first as a validation tool before sending generated poses to the
robot.

## Design Principle

- Keep layout generation independent from robot execution.
- Keep generic motion concepts separate from vendor-specific adapters.
- Use Doosan as an experimental platform, not as the architectural boundary.
