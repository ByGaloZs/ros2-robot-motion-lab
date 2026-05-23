"""Generate the basic pallet layout used by pallet_layout_core v0.1.

This script demonstrates the intended use of the pure Python module from a repository
checkout. It builds a layout configuration, generates the deterministic grid layout,
prints a short summary, and exports the resulting data to a JSON file under `reports/`.
"""

from pathlib import Path

from pallet_layout_core import BoxDimensions, LayoutConfig, PalletDimensions
from pallet_layout_core.exporters import export_layout_to_json
from pallet_layout_core.layout_generator import generate_pallet_layout


def main() -> None:
    """Run the basic layout generation example."""

    # The example dimensions are expressed in millimeters and match EXP-0009.
    config = LayoutConfig(
        box=BoxDimensions(length=300, width=200, height=150),
        pallet=PalletDimensions(length=1200, width=1000, height=150),
        layers=3,
        pattern="grid",
    )
    layout = generate_pallet_layout(config)
    total_slots = sum(len(layer.slots) for layer in layout.layers)

    # Keep the console output small and deterministic so it can be used as evidence.
    print(f"Generated layers: {len(layout.layers)}")
    print(f"Generated total slots: {total_slots}")

    # The exporter creates the parent directory if it does not already exist.
    output_path = Path("reports/generated_outputs/pallet_layout_core_v0.1/basic_layout.json")
    export_layout_to_json(layout, output_path)


if __name__ == "__main__":
    main()
