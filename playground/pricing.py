print(f"pricing: __name__ = {__name__}")


def apply_discount(price, percent):
    """Return price reduced by percent."""
    return round(price * (1 - percent / 100), 2)


if __name__ == "__main__":
    print(apply_discount(200.0, 15))
