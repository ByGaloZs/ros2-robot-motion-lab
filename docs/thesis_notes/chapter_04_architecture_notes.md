# Chapter 04 Architecture Notes

## Purpose of This Section

Collect working notes about the modular architecture and design decisions for the future
TFM architecture chapter.

## Key Ideas

- Keep `pallet_layout_core` independent from ROS 2 and vendor-specific execution.
- Use `robot_motion_client` for generic motion concepts.
- Use `doosan_motion_adapter` for Doosan-specific ROS 2 service integration.
- Use the dashboard first as a visual validation tool.

## Technical Evidence from Repository

- `docs/architecture/modular_motion_architecture.md`
- `docs/architecture/decisions/`
- `docs/implementation/pallet_layout_core_notes.md`

## Pending Work

- Refine interfaces after `pallet_layout_core v0.1` is implemented.
- Document data flow between layout generation and motion execution.
