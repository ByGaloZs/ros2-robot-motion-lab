"""Tests for deterministic grid layout generation.

The reference input is the basic v0.1 scenario: a 300 x 200 x 150 mm box on a
1200 x 1000 x 150 mm pallet with three layers. The expected result is 4 columns, 5 rows,
20 slots per layer, and 60 total slots.
"""

from pallet_layout_core.layout_generator import generate_pallet_layout
from pallet_layout_core.models import BoxDimensions, LayoutConfig, PalletDimensions


def test_generate_basic_grid_layout() -> None:
    """Generate the reference grid layout and verify slots, poses, and identifiers."""

    config = LayoutConfig(
        box=BoxDimensions(length=300, width=200, height=150),
        pallet=PalletDimensions(length=1200, width=1000, height=150),
        layers=3,
        pattern="grid",
    )

    layout = generate_pallet_layout(config)
    total_slots = sum(len(layer.slots) for layer in layout.layers)
    first_slot = layout.layers[0].slots[0]
    last_layer_first_slot = layout.layers[-1].slots[0]
    slot_ids = [slot.slot_id for layer in layout.layers for slot in layer.slots]

    # Geometry checks: 1200 / 300 = 4 columns and 1000 / 200 = 5 rows.
    assert len(layout.layers) == 3
    assert all(len(layer.slots) == 20 for layer in layout.layers)
    assert total_slots == 60

    # The first slot is centered over the first box footprint on top of the pallet.
    assert first_slot.slot_id == "L0_R0_C0"
    assert first_slot.target_pose.position.x == 150
    assert first_slot.target_pose.position.y == 100
    assert first_slot.target_pose.position.z == 225
    assert first_slot.target_pose.orientation.rx == 0
    assert first_slot.target_pose.orientation.ry == 0
    assert first_slot.target_pose.orientation.rz == 0

    # Layer index 2 adds two box heights to the first layer Z center: 225 + 300 = 525.
    assert last_layer_first_slot.target_pose.position.z == 525
    assert len(slot_ids) == len(set(slot_ids))
