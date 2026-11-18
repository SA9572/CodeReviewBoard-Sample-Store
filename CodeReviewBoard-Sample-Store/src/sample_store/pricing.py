"""Pricing helpers for a tiny online store."""


def calculate_subtotal(unit_price: float, quantity: int) -> float:
    """Return the pre-discount subtotal for an order."""
    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")
    if quantity < 0:
        raise ValueError("quantity cannot be negative")

    # INTENTIONAL BUG: this should multiply unit_price by quantity.
    return unit_price + quantity


def apply_discount(subtotal: float, discount_percent: float) -> float:
    """Apply a percentage discount and return the final price."""
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")

    # INTENTIONAL BUG: discounts above 100% are not rejected.
    discount = subtotal * (discount_percent / 100)
    return round(subtotal - discount, 2)
