"""Tests for input validation rules used by the pallet layout generator.

These tests define the minimum accepted and rejected inputs for version 0.1. They are
kept close to the public validation functions so future changes to validation behavior
are explicit and reviewed.
"""

import pytest

from pallet_layout_core.models import BoxDimensions, LayoutConfig, PalletDimensions
from pallet_layout_core.validators import (
    validate_box_fits_on_pallet,
    validate_layer_count,
    validate_layout_config,
    validate_positive_dimensions,
    validate_supported_pattern,
)


def test_valid_dimensions_pass() -> None:
    """Positive box and pallet dimensions should be accepted without errors."""

    validate_positive_dimensions(BoxDimensions(length=300, width=200, height=150))
    validate_positive_dimensions(PalletDimensions(length=1200, width=1000, height=150))


def test_negative_box_dimensions_fail() -> None:
    """A negative box dimension should fail because physical sizes must be positive."""

    with pytest.raises(ValueError, match="length must be greater than zero"):
        validate_positive_dimensions(BoxDimensions(length=-300, width=200, height=150))


def test_zero_pallet_dimensions_fail() -> None:
    """A zero pallet dimension should fail because it cannot produce valid slots."""

    with pytest.raises(ValueError, match="width must be greater than zero"):
        validate_positive_dimensions(PalletDimensions(length=1200, width=0, height=150))


def test_zero_layers_fail() -> None:
    """A layout must contain at least one layer."""

    with pytest.raises(ValueError, match="layers must be greater than zero"):
        validate_layer_count(0)


def test_unsupported_pattern_fail() -> None:
    """Only the grid pattern is supported in version 0.1."""

    with pytest.raises(ValueError, match="unsupported pattern"):
        validate_supported_pattern("interlocked")


def test_box_larger_than_pallet_fails() -> None:
    """A box footprint larger than the pallet footprint should be rejected."""

    with pytest.raises(ValueError, match="box length"):
        validate_box_fits_on_pallet(
            BoxDimensions(length=1300, width=200, height=150),
            PalletDimensions(length=1200, width=1000, height=150),
        )


def test_layout_config_validation_passes_for_basic_grid() -> None:
    """The reference grid configuration should pass full config validation."""

    config = LayoutConfig(
        box=BoxDimensions(length=300, width=200, height=150),
        pallet=PalletDimensions(length=1200, width=1000, height=150),
        layers=3,
        pattern="grid",
    )

    validate_layout_config(config)
