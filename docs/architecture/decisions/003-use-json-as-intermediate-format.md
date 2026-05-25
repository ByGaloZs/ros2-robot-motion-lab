# ADR 003: Use JSON as Intermediate Format

## Status

Accepted

## Context

Early project phases need a simple way to inspect, test, store, and exchange generated
domain outputs. The same output may later be consumed by unit tests, dashboard previews,
ROS 2 clients, adapters, notebooks, and experiment evidence.

## Decision

JSON will be used as the intermediate output format for generated domain outputs during
the early implementation phases.

## Rationale

JSON is human-readable, easy to version, simple to validate in tests, and broadly
supported by Python, dashboards, notebooks, and integration tools. It provides a practical
bridge between pure layout generation and later ROS 2 execution layers.

## Consequences

### Positive

- Generated outputs can be inspected and attached to experiment evidence.
- The same output can support tests, dashboard previews, ROS 2 clients, and adapters.

### Trade-offs

- JSON does not enforce schemas unless a schema or explicit validation is added.
- Numeric units and coordinate conventions must be documented clearly to avoid
  ambiguity.

## Future Revision

This decision may be revisited if the project requires strict schemas, binary formats,
ROS 2 messages, or database-backed storage for larger datasets.
