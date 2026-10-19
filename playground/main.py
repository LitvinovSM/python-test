# playground/main.py
from playground.pricing import apply_discount

print(f"main: __name__ = {__name__}")
print(apply_discount(200.0, 15))
