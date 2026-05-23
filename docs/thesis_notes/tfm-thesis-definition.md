# TFM Thesis Definition

## Purpose of This Document

This document defines the expected final direction of the Master's Thesis / TFM. It should
be treated as a stable reference for the goal, hypothesis, scope, and target architecture.

It is not a project status report. Implementation progress, validated commands, and
experiment results should be tracked in `docs/context/project_status.md`,
`docs/experiments/`, and `docs/implementation/`.

## Working Title

Spanish title:

```text
Diseno y evaluacion de una arquitectura modular para la configuracion, generacion y ejecucion de movimientos roboticos en ROS 2
```

English title:

```text
Design and Evaluation of a Modular Architecture for Configuring, Generating, and Executing Robotic Motion in ROS 2
```

Doosan Robotics is the intended experimental validation platform. It is not the full scope
of the thesis.

## Central Thesis

A modular, robot-agnostic architecture based on ROS 2, complemented by a user interface
for configuration and supervision, can structure robotic motion generation and execution
in a more maintainable, extensible, traceable, configurable, and experimentally evaluable
way than a monolithic implementation directly coupled to a specific robot platform.

## Main Hypothesis

If the robotic motion system is separated into independent layers, including a user
interface, application backend, robot-agnostic scenario or target generation, intermediate
target representation, generic motion client, and robot-specific adapter, then the
resulting system can be more maintainable, reusable, configurable, traceable, and
experimentally evaluable than a monolithic implementation tied directly to one robot
platform.

## General Objective

Design, implement, and evaluate a modular architecture based on ROS 2 for the
configuration, generation, planning, and execution of robotic motion, integrating a user
interface for scenario configuration and result supervision, and validating the proposal
through a palletizing use case with Doosan Robotics in a simulated environment.

## Specific Objectives

1. Analyze the requirements of a modular robotic motion architecture in ROS 2.
2. Design a layered architecture separating UI, application logic, robot-agnostic generation, intermediate representation, generic motion execution, and robot-specific adaptation.
3. Define and validate a robot-agnostic generation layer for palletizing scenarios and target poses.
4. Define an intermediate representation for generated motion targets.
5. Specify or develop a Dashboard/UI layer for configuring palletizing scenarios and visualizing generated layouts.
6. Define or implement a generic motion client capable of consuming intermediate targets.
7. Define or implement a Doosan-specific adapter using the available Doosan Robotics ROS 2 interfaces.
8. Validate the architecture through reproducible experiments in simulation.
9. Evaluate the architecture using criteria such as maintainability, modularity, traceability, extensibility, error handling, configurability, and separation of responsibilities.

## Scope

In scope:

- Modular software architecture.
- ROS 2-based robotic motion workflow.
- Dashboard/UI as an interaction and supervision layer.
- Palletizing as the experimental use case.
- Doosan Robotics as validation platform.
- Simulation-based validation.
- Intermediate data representation.
- Experimental documentation.
- Robot-agnostic scenario and target generation.
- Generic motion client design.
- Robot-specific adapter design.

Out of scope unless the thesis direction is explicitly revised:

- Real industrial deployment.
- Full production-grade palletizing system.
- Physical robot execution as a hard requirement.
- Industrial safety certification.
- Full warehouse management integration.
- Multi-robot orchestration.
- Advanced collision avoidance beyond available planning tools.
- Production-grade frontend authentication and authorization.
- Full MES/WMS/ERP integration.

## Target Architecture

```text
User / Operator
      ↓
Dashboard / UI
      ↓
Application API / Backend
      ↓
Robot-Agnostic Scenario and Target Generation
      ↓
Intermediate Target Representation / JSON
      ↓
Generic Motion Client
      ↓
Robot-Specific Adapter
      ↓
ROS 2 / MoveIt2 / Gazebo / Emulator / Robot Platform
```

Correct dependency direction:

```text
Dashboard / UI
      ↓
Application API / Backend
      ↓
Core generation modules
      ↓
Motion client
      ↓
Robot adapter
```

Lower-level modules must not depend on upper-level modules. For example, target generation
logic must not depend on Dashboard/UI code, and robot adapters must not embed UI logic.

## Role of Each Target Layer

### Dashboard / UI

The Dashboard/UI should allow a user or operator to configure palletizing scenarios, enter
dimensions, select layout parameters, visualize generated layouts, inspect intermediate
data, and supervise validation results.

The Dashboard/UI is a formal application layer. It should not contain core target
generation logic or robot-specific execution logic.

### Application API / Backend

The Application API / Backend should bridge the UI and backend modules. It receives user
input, validates requests, calls target generation logic, stores or returns intermediate
data, and can eventually trigger motion workflows.

### Robot-Agnostic Scenario and Target Generation

This layer should generate robot-agnostic scenario data, layouts, and target poses from
input parameters. It should remain independent from ROS 2, Doosan Robotics, MoveIt2,
Gazebo, robot kinematics, and Dashboard/UI code.

An initial prototype of this idea can be used to validate palletizing geometry before full
ROS 2 integration.

### Intermediate Target Representation / JSON

The intermediate representation should provide a stable data format between target
generation, visualization, motion clients, and robot adapters.

JSON is the initial practical candidate because it is inspectable, testable, and easy to
exchange between scripts, dashboards, notebooks, and integration layers.

### Generic Motion Client

The generic motion client should represent motion targets, requests, sequences, execution
status, and validation flow independently from a specific robot brand.

### Robot-Specific Adapter

The robot-specific adapter should translate generic motion requests into the interfaces
provided by a concrete platform.

For the planned validation platform, this adapter is expected to map generic requests to
Doosan Robotics ROS 2 services, MoveIt2 workflows, or simulator-specific execution paths.

### ROS 2 / MoveIt2 / Gazebo / Emulator / Robot Platform

This layer provides the experimental execution and simulation environment used to validate
the architecture. It validates the architecture but does not define the entire thesis
scope.

## Role of Doosan Robotics

Doosan Robotics should be treated as the concrete validation platform for experiments in
ROS 2. It provides realistic services, interfaces, simulation workflows, and robot motion
constraints.

The thesis should not be framed as a Doosan-specific command wrapper. It should be framed
as a modular architecture that can be validated through Doosan Robotics and could later be
adapted to other robot platforms.

## Role of the Dashboard / UI

The Dashboard/UI demonstrates that the system can be configured and supervised without
manually editing scripts. It is part of the architecture because configurability and human
supervision are central to the final system goal.

The Dashboard/UI should call backend or application services. It should not directly own
robot-agnostic target generation logic or robot-specific execution logic.

## What the TFM Wants to Demonstrate

- The system can be decomposed into independent software layers.
- Core target generation can be validated separately from ROS 2 execution and robot hardware.
- Intermediate representations can decouple modules.
- A UI can configure and supervise the workflow without embedding robot logic.
- Robot-specific code can remain isolated in adapters.
- The architecture is more maintainable and explainable than a monolithic script.
- The architecture supports reproducible experiments.
- The project can be evaluated using software engineering criteria, not only robot motion results.

## Stable Context for Future OpenCode Sessions

When reopening this repository in a future session, interpret this file as the target TFM
vision. Do not infer the current implementation state from this document.

Use these files for current state and evidence:

- `docs/context/project_status.md`
- `docs/experiments/experiment-log.md`
- `docs/implementation/`
- `docs/commands/validated-commands.md`

The intended final thesis is about a modular architecture for robotic motion generation
and execution. The repository may contain prototypes, scaffolds, and experiments that
support this final goal, but those intermediate artifacts should not redefine the thesis
scope unless the user explicitly changes the TFM direction.
