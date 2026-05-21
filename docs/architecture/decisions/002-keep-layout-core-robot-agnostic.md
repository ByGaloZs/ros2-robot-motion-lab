# ADR 002: Keep Layout Core Robot-Agnostic

## Status

Accepted

## Context

The current validation platform uses Doosan Robotics ROS 2, but the architecture must
remain general and reusable. If layout generation depends on Doosan services, ROS 2
execution details, MoveIt2, Gazebo, robot joints, velocity parameters, or service calls,
the core module becomes difficult to reuse with other robots or simulation environments.

## Decision

`pallet_layout_core` will remain independent from Doosan, ROS 2 execution details,
MoveIt2, Gazebo, robot joints, velocity parameters, and service calls.

## Rationale

Keeping the layout core robot-agnostic preserves a clean boundary between geometric task
generation and robot execution. Robot-specific behavior should be introduced later
through `robot_motion_client` and vendor-specific adapters.

## Consequences

### Positive

- The layout logic can be tested without a robot, simulator, or ROS 2 runtime.
- The generated data can be reused by multiple robot adapters or visualization tools.

### Trade-offs

- The layout core cannot validate robot reachability or trajectory feasibility by
  itself.
- Additional integration layers are required before generated poses can drive a robot.

## Future Revision

This decision may be revisited if future requirements show that some limited robot
capability metadata is necessary, but execution-specific behavior should remain outside
the layout core.
