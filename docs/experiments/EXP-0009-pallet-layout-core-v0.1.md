# EXP-0009: Pallet Layout Core v0.1

## Objective

Validate whether a robot-agnostic Python module can generate palletizing target poses
from box and pallet dimensions.

## Context

This experiment starts the implementation phase of the custom modular architecture.
Previous experiments validated the ROS 2, Doosan, MoveIt2, and Gazebo environment. This
experiment validates the geometric layout layer before connecting it to ROS 2 execution.

## Hypothesis

A pure Python module can generate a deterministic grid-based pallet layout with layers,
slots, and target poses without depending on ROS 2 or Doosan-specific services.

## Setup

### Environment

- OS: Ubuntu 24.04 LTS
- ROS 2 version: Jazzy
- Robot platform: Not required for this experiment
- Simulator: Not required for this experiment
- Relevant package: `pallet_layout_core`

### Inputs

- Box dimensions: 300 x 200 x 150 mm
- Pallet dimensions: 1200 x 1000 x 150 mm
- Layers: 3
- Pattern: grid

## Procedure

1. Define the initial data models. 2. Validate input dimensions. 3. Generate grid-based
slots for one layer. 4. Generate multiple layers. 5. Calculate target poses for every
slot. 6. Export the generated layout as JSON. 7. Run unit tests. 8. Review the generated
output manually.

## Expected Result

The module should generate:

- 4 columns.
- 5 rows.
- 20 boxes per layer.
- 3 layers.
- 60 total slots.
- One target pose per slot.
- A JSON output with all generated layers, slots, and target poses.

## Actual Result

To be completed after implementation.

## Validation Criteria

- All generated poses must be inside the pallet boundaries.
- Z positions must increase by one box height per layer.
- Slot IDs must be unique.
- Total slot count must match the expected result.
- JSON export must preserve all relevant layout data.
- The module must not depend on ROS 2, Doosan, MoveIt2, Gazebo, or dashboard code.

## Evidence

To be completed with links to generated JSON files, test results, or logs.

## Result

Pending

## Notes

This experiment validates only geometric layout generation. It does not validate robot
motion, trajectory planning, collision checking, or reachability.

## Impact on Architecture

The result of this experiment will influence the data models consumed later by
`robot_motion_client`, `pallet_layout_dashboard`, and `doosan_motion_adapter`.
