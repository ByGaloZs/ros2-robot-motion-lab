"""Tests for converting and exporting generated layouts.

The exporter tests verify that generated dataclass objects can be converted to standard
Python containers and persisted as JSON without adding runtime dependencies.
"""

import json

from pallet_layout_core.exporters import export_layout_to_json, layout_to_dict
from pallet_layout_core.layout_generator import generate_pallet_layout
from pallet_layout_core.models import BoxDimensions, LayoutConfig, PalletDimensions


def test_layout_to_dict_returns_dictionary() -> None:
    """The dictionary exporter should expose the layout as plain Python data."""

    layout = _basic_layout()

    data = layout_to_dict(layout)

    assert isinstance(data, dict)
    assert "layers" in data


def test_export_layout_to_json(tmp_path) -> None:
    """The JSON exporter should create a readable JSON file with generated layers."""

    layout = _basic_layout()
    output_path = tmp_path / "basic_layout.json"

    export_layout_to_json(layout, output_path)

    assert output_path.exists()
    data = json.loads(output_path.read_text(encoding="utf-8"))
    assert "layers" in data
    assert len(data["layers"]) == 3


def _basic_layout():
    """Create the reference generated layout used by exporter tests."""

    config = LayoutConfig(
        box=BoxDimensions(length=300, width=200, height=150),
        pallet=PalletDimensions(length=1200, width=1000, height=150),
        layers=3,
        pattern="grid",
    )
    return generate_pallet_layout(config)
