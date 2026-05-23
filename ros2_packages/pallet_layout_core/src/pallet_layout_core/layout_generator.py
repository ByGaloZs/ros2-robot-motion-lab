"""Grid-based pallet layout generation.

The generator converts a validated `LayoutConfig` into deterministic layers and slots.
It contains only geometric layout logic and does not perform robot motion planning,
collision checking, reachability analysis, or ROS 2 communication.
"""

from pallet_layout_core.models import (
    GeneratedLayout,
    LayoutConfig,
    Orientation,
    PalletLayer,
    PalletSlot,
    Position,
    TargetPose,
)
from pallet_layout_core.validators import validate_layout_config


def generate_pallet_layout(config: LayoutConfig) -> GeneratedLayout:
    """Generate a complete pallet layout from box, pallet, and layer settings.

    Version 0.1 supports a single `grid` pattern. Rows and columns are calculated with
    floor division, so any leftover pallet space remains unused. Slot positions are the
    geometric centers of boxes in the pallet coordinate frame.
    """

    validate_layout_config(config)

    # Floor division intentionally keeps only full boxes that fit on the pallet.
    columns = int(config.pallet.length // config.box.length)
    rows = int(config.pallet.width // config.box.width)
    layers: list[PalletLayer] = []

    for layer_index in range(config.layers):
        slots: list[PalletSlot] = []
        for row_index in range(rows):
            for column_index in range(columns):
                # Target positions represent the center point of each box slot.
                position = Position(
                    x=config.box.length / 2 + column_index * config.box.length,
                    y=config.box.width / 2 + row_index * config.box.width,
                    z=config.pallet.height
                    + config.box.height / 2
                    + layer_index * config.box.height,
                )
                target_pose = TargetPose(
                    position=position,
                    orientation=Orientation(),
                )
                slots.append(
                    PalletSlot(
                        slot_id=f"L{layer_index}_R{row_index}_C{column_index}",
                        layer_index=layer_index,
                        row_index=row_index,
                        column_index=column_index,
                        target_pose=target_pose,
                    )
                )
        layers.append(PalletLayer(layer_index=layer_index, slots=slots))

    return GeneratedLayout(config=config, layers=layers)
