# Chapter 04 Architecture Notes

## Purpose of This Section

Collect working notes about the modular architecture and design decisions for the future
TFM architecture chapter.

## Key Ideas

- Keep domain modules independent from ROS 2 and vendor-specific execution.
- Use JSON or another documented intermediate representation to decouple domain
  computation, visualization, motion clients, and adapters.
- Use `robot_motion_client` for generic motion concepts.
- Use `doosan_motion_adapter` for Doosan-specific ROS 2 service integration.
- Treat the Dashboard/UI as a formal application layer for configuration, visualization,
  supervision, and reproducibility.
- Keep dependency direction from UI and application layers toward core and adapter layers,
  not from lower layers back into the UI.

## Technical Evidence from Repository

- `docs/architecture/modular_motion_architecture.md`
- `docs/architecture/decisions/`
- `docs/implementation/`
- `docs/thesis_notes/tfm-thesis-definition.md`

## Pending Work

- Refine interfaces after the first robot-agnostic module boundary is validated.
- Document data flow between domain computation and motion execution.
- Define Dashboard/UI requirements without embedding core logic or robot-specific logic in
  the UI.
