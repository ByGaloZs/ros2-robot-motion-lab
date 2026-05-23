# Master Subject Alignment

## Purpose

This document maps the TFM direction to the Master's Degree in Computer Science and
Technology at UC3M.

It is intended to help future work sessions recover the academic context quickly and keep
the repository aligned with the expected thesis scope.

## Program Context

The Master's Degree in Computer Science and Technology has 60 ECTS:

- 30 ECTS of compulsory subjects.
- 12 ECTS of elective subjects.
- 18 ECTS for the Master's Thesis / TFM.

The official program describes advanced training in areas such as artificial intelligence,
software engineering, secure systems, multimedia systems, and distributed systems.

## Selected Electives

The planned electives are:

- `Robotica` - 6 ECTS.
- `Percepcion 3D` - 3 ECTS.
- `Simuladores de Robots` - 3 ECTS.

These electives support the robotic motion, simulation, perception, and validation focus
of the proposed TFM.

## Alignment With the TFM

| Subject | Relation to the TFM | Repository Evidence or Expected Evidence |
|---|---|---|
| Seminarios: Metodos de Investigacion | Supports research framing, experimental method, evidence collection, and public defense preparation. | `docs/experiments/`, `docs/commands/validated-commands.md`, `docs/thesis_notes/` |
| Inteligencia Artificial de Inspiracion Biologica | Provides context for adaptive, heuristic, or optimization-based future extensions. | Future work for layout optimization or trajectory selection. |
| Planificacion Automatica | Supports planning concepts, task decomposition, and possible motion workflow planning. | MoveIt2 validation experiments and future motion planning layer. |
| Digitalizacion de Ingenieria de Sistemas Complejos | Supports modeling the robotic workflow as a modular, traceable, configurable software system. | `docs/architecture/`, architecture decisions, TFM thesis definition. |
| Sistemas Paralelos y Distribuidos | Supports ROS 2 as a distributed architecture using nodes, services, topics, and execution processes. | ROS 2 graph inspection, service validation, client prototype experiments. |
| Ciberseguridad y Privacidad | Provides awareness of system boundaries, safe interfaces, and future deployment concerns. | Out-of-scope production security noted in thesis scope. |
| Procesamiento del lenguaje natural con aprendizaje profundo | Not central to the current TFM scope, but provides AI context for possible future user interaction or documentation tools. | Not expected as core evidence. |
| Informatica Centrada en el Humano | Supports treating the Dashboard/UI as a formal layer for configuration, visualization, supervision, and usability. | Planned Dashboard/UI requirements and future application layer documentation. |
| Robotica | Directly supports robot motion, ROS 2 workflows, adapters, planning, execution, and platform validation. | Doosan service experiments, MoveIt2 validation, Gazebo validation, future robot adapter. |
| Percepcion 3D | Supports future scene understanding, spatial validation, object localization, and perception-aware robotic workflows. | Future work; not required for the first architecture validation. |
| Simuladores de Robots | Directly supports Gazebo, emulator-based validation, reproducible simulation experiments, and safe testing before hardware execution. | EXP-0005, EXP-0006, Doosan emulator validation, simulation documentation. |
| Trabajo Fin de Master | Integrates the architecture, implementation, experiments, evaluation criteria, and thesis defense. | Full repository documentation and final TFM report. |

## Why This TFM Fits the Program

The TFM combines several areas of the master's program:

- Software engineering through modular architecture, separation of responsibilities, and maintainability criteria.
- Distributed systems through ROS 2 communication concepts and service-based execution.
- Robotics through motion generation, planning, execution, simulation, and robot adapters.
- Human-centered computing through the planned Dashboard/UI configuration and supervision layer.
- Experimental methodology through reproducible commands, experiment files, validation evidence, and notebook-based analysis.

## Academic Framing

The project should be described as a software architecture and experimental validation TFM,
not as a single robot demo.

Preferred framing:

```text
Design and evaluation of a modular software architecture for robotic motion generation and execution, using ROS 2 and validating the proposal through a Doosan Robotics simulation-based use case.
```

Avoid framing it as:

```text
Moving a Doosan robot with ROS 2.
```

## How This Helps Future OpenCode Sessions

When reopening this repository, use this document to understand why the TFM includes:

- ROS 2 and distributed robotic communication.
- Doosan Robotics as a validation platform.
- Gazebo, MoveIt2, and emulator-based experiments.
- A Dashboard/UI as a formal architecture layer.
- Reproducible experiment documentation.
- Software engineering evaluation criteria.

This document should change only if the selected electives or academic framing change.
