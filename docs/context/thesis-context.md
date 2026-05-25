# Thesis Context

## Objective

Design, implement, and evaluate a modular robotics motion architecture for domain
computation, motion abstraction, planning or execution integration, and reproducible
validation, using Doosan ROS 2 as the current experimental validation platform.

The canonical working definition of the TFM thesis, hypothesis, objectives, scope, and
layer responsibilities is maintained in:

```text
docs/thesis_notes/tfm-thesis-definition.md
```

## Scope

This repository supports preparation for a master's thesis, but it is not intended to be
only a Doosan demo.

Doosan Robotics ROS 2 and the Doosan `m1013` provide the current experimental validation
platform. The core contribution should be the modular software architecture, not a
robot-specific command wrapper.

## Architectural Separation

The architecture should separate:

- Dashboard/UI configuration and supervision;
- application API or backend orchestration;
- trajectory generation;
- intermediate target representation;
- motion planning;
- robot execution;
- robot-specific adapters;
- configuration;
- validation and experiments.

Lower-level modules must not depend on upper-level modules. Domain modules must not depend
on Dashboard/UI code, and robot adapters must not embed UI logic.

## Candidate Use Cases

Use cases should be selected because they exercise the architectural boundaries: domain
computation, intermediate representations, motion requests, robot-specific adapters, and
validation workflows.

Any current implementation module should be treated as a validation input, not as the
final thesis scope.

## Validation Tools

Future validation may involve:

- RViz2 for visualization;
- MoveIt2 for planning;
- Gazebo for simulation;
- Doosan ROS 2 services for execution on the current experimental platform.
