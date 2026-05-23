"""JSON export helpers for generated pallet layouts.

The exporter module serializes dataclass-based layouts with Python standard library
tools only. It does not define a custom JSON schema yet; the exported structure mirrors
the dataclass tree produced by the layout generator.
"""

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from pallet_layout_core.models import GeneratedLayout


def layout_to_dict(layout: GeneratedLayout) -> dict[str, Any]:
    """Convert a generated layout dataclass tree into plain dictionaries and lists."""

    return asdict(layout)


def export_layout_to_json(layout: GeneratedLayout, output_path: str | Path) -> None:
    """Write a generated layout to a JSON file.

    Parent directories are created automatically so examples and future scripts can
    write outputs into report folders without requiring manual setup.
    """

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(layout_to_dict(layout), indent=2), encoding="utf-8")
