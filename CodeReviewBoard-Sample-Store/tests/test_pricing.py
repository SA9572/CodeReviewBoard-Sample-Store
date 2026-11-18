import pytest

from sample_store.pricing import apply_discount, calculate_subtotal


def test_calculate_subtotal_for_one_item():
    assert calculate_subtotal(12.50, 1) == 12.50


def test_apply_discount():
    assert apply_discount(100.00, 10) == 90.00


def test_negative_quantity_is_rejected():
    with pytest.raises(ValueError):
        calculate_subtotal(10.00, -1)
