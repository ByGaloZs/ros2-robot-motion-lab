# Chapter 01 Introduction Notes

## Purpose of This Section

Collect working notes about the project problem, motivation, and context for the future
TFM introduction.

## Key Ideas

- The TFM should be framed as the design and evaluation of a modular software
  architecture for robotic motion generation and execution, not as a Doosan-only demo.
- Modular robot motion software should separate task generation, planning, execution,
  and robot-specific communication.
- Doosan Robotics provides the current validation platform, but the architecture should
  remain reusable.
- Dashboard/UI interaction is part of the architecture because it supports configuration,
  supervision, and reproducibility without editing scripts manually.
- Validation use cases should be practical enough to exercise target generation, motion
  abstraction, adapter boundaries, and execution flow.

## Technical Evidence from Repository

- `docs/context/project-context.md`
- `docs/context/thesis-context.md`
- `docs/context/project_status.md`
- `docs/thesis_notes/tfm-thesis-definition.md`

## Pending Work

- Refine the final TFM research question.
- Refine the problem statement after the first robot-agnostic module boundary is fully
  reviewed.
