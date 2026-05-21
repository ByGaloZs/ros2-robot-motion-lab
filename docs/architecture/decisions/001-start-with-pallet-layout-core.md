# ADR 001: Start with `pallet_layout_core`

## Status

Accepted

## Context

The project needs a modular ROS 2 architecture for trajectory generation, planning, and
execution. Before integrating with ROS 2, MoveIt2, Gazebo, or Doosan-specific services,
the project needs to validate whether palletizing target poses can be generated
deterministically from simple geometric inputs.

## Decision

The first implementation module will be `pallet_layout_core`.

## Rationale

Starting with `pallet_layout_core` validates the geometric layer before adding robot
execution complexity. It also creates a stable data source for later clients, adapters,
dashboard previews, and experiments.

## Consequences

### Positive

- The first implementation target is small, testable, and robot-agnostic.
- Generated target poses can be validated before any robot motion is attempted.

### Trade-offs

- ROS 2 execution integration is delayed.
- Early results validate geometry only, not planning, reachability, or execution.

## Future Revision

This decision may be revisited after `pallet_layout_core v0.1` produces stable layout
JSON and unit tests demonstrate predictable behavior.
