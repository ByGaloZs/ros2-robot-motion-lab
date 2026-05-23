"""Data models for robot-agnostic pallet layouts.

The classes in this file describe the geometric input and output of the pallet layout
generator. They are intentionally small dataclasses with typed fields only. Validation
and generation logic live in separate modules so these models can remain reusable data
containers.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BoxDimensions:
    """Physical dimensions of one box.

    The unit is not enforced by the model. Callers should use one consistent unit for
    all dimensions, such as millimeters.
    """

    length: float
    width: float
    height: float


@dataclass(frozen=True)
class PalletDimensions:
    """Physical dimensions of the pallet used as the layout base.

    `height` represents the top surface elevation offset used when calculating the
    first box center on the Z axis.
    """

    length: float
    width: float
    height: float


@dataclass(frozen=True)
class Orientation:
    """Target orientation expressed as roll, pitch, and yaw-like values.

    Version 0.1 uses the default zero orientation for every slot. The model is present
    so generated target poses already have a stable shape for later consumers.
    """

    rx: float = 0.0
    ry: float = 0.0
    rz: float = 0.0


@dataclass(frozen=True)
class Position:
    """Target position of a slot center in the pallet coordinate frame."""

    x: float
    y: float
    z: float


@dataclass(frozen=True)
class TargetPose:
    """Full target pose for placing or referencing a box slot."""

    position: Position
    orientation: Orientation


@dataclass(frozen=True)
class LayoutConfig:
    """Input configuration used to generate a complete pallet layout."""

    box: BoxDimensions
    pallet: PalletDimensions
    layers: int
    pattern: str = "grid"


@dataclass(frozen=True)
class PalletSlot:
    """One generated box slot inside a pallet layer."""

    slot_id: str
    layer_index: int
    row_index: int
    column_index: int
    target_pose: TargetPose


@dataclass(frozen=True)
class PalletLayer:
    """A horizontal pallet layer containing ordered slots."""

    layer_index: int
    slots: list[PalletSlot]


@dataclass(frozen=True)
class GeneratedLayout:
    """Complete generated layout including the original config and all layers."""

    config: LayoutConfig
    layers: list[PalletLayer]
