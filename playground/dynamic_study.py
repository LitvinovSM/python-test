# suite = "smoke"
# build = 7
# passed = 47
# total = 52
# duration = 3.14159
# ratio = Decimal(passed) / Decimal(total)
# ratio = ratio.quantize(Decimal("0.001"),rounding=ROUND_HALF_UP)
#
# print(f"[{suite}] build #{build:04d} | {passed}/{total} passed ({ratio:.1%}) | {duration:.2f} s")
# print(f"passed={passed}, total={total}")
# #
# # [smoke] build #0007 | 47/52 passed (90.4%) | 3.14 s
# # passed=47, total=52
#
user_name = "  Alice "
email = None
age = 0
is_active = True

stripped_name = user_name.strip()
has_email = email is not None
is_named = len(stripped_name) > 0
is_valid_age = 0 <= age < 120


summary = f"User: {stripped_name.lower()}, age: {age} , valid age:{is_valid_age}, active: {is_active}, email set: {has_email}, named: {is_named}"
print(summary)
