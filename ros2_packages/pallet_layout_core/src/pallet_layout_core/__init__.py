"""Public API for the pure Python pallet layout generation core.

This package exposes the data models and the main layout generation function used by
`pallet_layout_core` v0.1. The module intentionally stays independent from ROS 2,
Doosan Robotics, MoveIt2, Gazebo, and dashboard code so it can be reused by future
robot-specific adapters or application layers.
"""

from pallet_layout_core.layout_generator import generate_pallet_layout
from pallet_layout_core.models import (
    BoxDimensions,
    GeneratedLayout,
    LayoutConfig,
    Orientation,
    PalletDimensions,
    PalletLayer,
    PalletSlot,
    Position,
    TargetPose,
)

__all__ = [
    "BoxDimensions",
    "GeneratedLayout",
    "LayoutConfig",
    "Orientation",
    "PalletDimensions",
    "PalletLayer",
    "PalletSlot",
    "Position",
    "TargetPose",
    "generate_pallet_layout",
]
