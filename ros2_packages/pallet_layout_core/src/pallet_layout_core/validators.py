"""Validation helpers for pallet layout inputs.

These functions keep input validation separate from layout generation. They raise
`ValueError` with explicit messages so CLI tools, tests, or future application layers
can report invalid user input clearly.
"""

from pallet_layout_core.models import BoxDimensions, LayoutConfig, PalletDimensions

SUPPORTED_PATTERNS = {"grid"}


def validate_positive_dimensions(dimensions: BoxDimensions | PalletDimensions) -> None:
    """Ensure that all length, width, and height values are strictly positive.

    A zero or negative physical dimension cannot produce a meaningful pallet layout and
    would also break floor-division based row and column calculations.
    """

    if dimensions.length <= 0:
        raise ValueError("length must be greater than zero")
    if dimensions.width <= 0:
        raise ValueError("width must be greater than zero")
    if dimensions.height <= 0:
        raise ValueError("height must be greater than zero")


def validate_layer_count(layers: int) -> None:
    """Ensure that the layout contains at least one layer."""

    if layers <= 0:
        raise ValueError("layers must be greater than zero")


def validate_supported_pattern(pattern: str) -> None:
    """Ensure that the requested layout pattern is implemented in this version.

    Version 0.1 intentionally supports only a simple grid pattern. Additional patterns
    should be added explicitly in later versions with their own tests.
    """

    if pattern not in SUPPORTED_PATTERNS:
        supported = ", ".join(sorted(SUPPORTED_PATTERNS))
        raise ValueError(f"unsupported pattern '{pattern}'. Supported patterns: {supported}")


def validate_box_fits_on_pallet(box: BoxDimensions, pallet: PalletDimensions) -> None:
    """Ensure that one box footprint can fit within the pallet footprint.

    This check only validates the X/Y footprint. It does not perform stack stability,
    collision, reachability, or robot-specific feasibility checks.
    """

    if box.length > pallet.length:
        raise ValueError("box length must not be greater than pallet length")
    if box.width > pallet.width:
        raise ValueError("box width must not be greater than pallet width")


def validate_layout_config(config: LayoutConfig) -> None:
    """Validate a complete layout configuration before generation."""

    validate_positive_dimensions(config.box)
    validate_positive_dimensions(config.pallet)
    validate_layer_count(config.layers)
    validate_supported_pattern(config.pattern)
    validate_box_fits_on_pallet(config.box, config.pallet)
