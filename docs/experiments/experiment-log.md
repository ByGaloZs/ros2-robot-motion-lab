# Experiment Log

## Purpose

Track reproducible experiments for this ROS 2 robot motion lab.

## Current Status

The initial experiment sequence has been completed and documented.

| Experiment | Title | Status | Main Result |
|---|---|---|---|
| EXP-0001 | MoveJoint Service Validation | Validated | Direct joint motion through `dsr_msgs2/srv/MoveJoint` works in virtual mode. |
| EXP-0002 | Robot State Inspection | Validated | Runtime state topics, transforms, nodes, and services are visible in the ROS 2 graph. |
| EXP-0003 | Doosan Services and Interfaces Mapping | Validated | Doosan packages, interfaces, and motion services are available for future clients. |
| EXP-0004 | MoveLine Service Validation | Validated | Cartesian linear motion through `dsr_msgs2/srv/MoveLine` works in virtual mode. |
| EXP-0005 | MoveIt2 Planning Validation | Validated | MoveIt2 can plan and execute trajectories for the Doosan `m1013` in virtual mode. |
| EXP-0006 | Gazebo Simulation Validation | Validated | Gazebo can simulate the Doosan `m1013` and expose robot state through ROS 2. |
| EXP-0007 | Motion Command Failure Handling | Validated | Invalid service calls fail safely and a recovery command confirms service usability. |
| EXP-0008 | Python rclpy Service Client Prototype | Validated | A Python `rclpy` prototype can call the official `MoveJoint` service. |
| EXP-0009 | Pallet Layout Core v0.1 | Pending | Initial isolated unit test command validated; full module validation remains pending. |

## Experiment Files

```text
EXP-0001-move-joint-service-validation.md
EXP-0002-robot-state-inspection.md
EXP-0003-doosan-services-and-interfaces-mapping.md
EXP-0004-moveline-service-validation.md
EXP-0005-moveit2-planning-validation.md
EXP-0006-gazebo-simulation-validation.md
EXP-0007-motion-command-failure-handling.md
EXP-0008-python-rclpy-service-client-prototype.md
EXP-0009-pallet-layout-core-v0.1.md
```

## Naming Convention

Future experiment files should use this pattern:

```text
EXP-0001-short-description.md
EXP-0002-short-description.md
EXP-0003-short-description.md
```

## Future Experiment Entry Template

```md
# EXP-XXXX - Experiment Title

## Objective

Describe what this experiment validates.

## Context

Briefly explain why this experiment is relevant.

## Preconditions

- TBD

## Interface or Tool Used

- TBD

## Steps

1. TBD

## Expected Result

TBD

## Actual Result

TBD

## Notes

TBD

## Conclusion

TBD

## Next Step

TBD
```
