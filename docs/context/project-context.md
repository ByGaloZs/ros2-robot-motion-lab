# Project Context

## Purpose

`ros2-robot-motion-lab` is a general modular robotics motion architecture lab for
documenting and experimenting with robot-agnostic domain logic, motion abstraction,
robot-specific adapters, validation platforms, and reproducible experiments.

The repository is intended for study notes, reproducible experiments, validated
commands, Jupyter-based experiment evidence, prototype scripts, and future custom ROS 2
packages.

## Current Validation Platform

Doosan Robotics ROS 2 and the Doosan `m1013` are the current experimental validation
platform, not the architectural scope of the project.

Doosan-specific experiments remain valid because they establish a concrete baseline for
service-based motion, robot state inspection, MoveIt2 planning, Gazebo simulation, and
Python `rclpy` clients.

## Boundary

This repository is intentionally separate from the validated official Doosan workspace:

```text
~/doosan_ws
```

Do not modify, move, copy, or assume control over that workspace from this repository.

## Current Phase

The initial Doosan-based experiment sequence has been completed and documented.

The repository currently contains one initial pure Python, robot-agnostic domain module.
It is an implementation detail used to validate architectural boundaries, not the final
project scope.

No ROS 2 nodes, robot adapter implementation, motion client implementation, or dashboard
implementation has been added yet.

## Future Package Direction

Future software should distinguish between domain modules, intermediate representations,
motion abstraction, robot-specific adapters, and application interfaces.

Conceptual responsibilities:

- Domain modules: robot-agnostic computation and generated targets.
- Intermediate representation: exchange format between generated targets, visualization,
  motion clients, and adapters.
- Motion abstraction: general motion request handling, validation flow, and execution
  orchestration.
- Robot-specific adapters: platform-specific communication through official interfaces.
- Application interfaces: visualization, interaction, supervision, and reproducibility.

The general layer should avoid direct dependency on Doosan-specific message or service
types where possible. Doosan-specific details such as `dsr_msgs2`, `dsr_controller2`,
and service paths should remain in the adapter layer.

ROS 2 package logic has not been implemented in this repository yet.

## Validated Doosan Interface

The currently validated Doosan movement service is:

```text
/dsr01/dsr_controller2/motion/move_joint
```

Service type:

```text
dsr_msgs2/srv/MoveJoint
```

This interface should be treated as the first concrete adapter target, not as the full
project architecture.

## Documentation Policy

When adding technical notes, prefer documenting:

1. What is being tested or built. 2. Why it matters. 3. What interface, package, or
command is involved. 4. What result is expected. 5. What result was obtained. 6. What
the next step is.
