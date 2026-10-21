import copy
from collections import Counter

print("--------------задача 1 ---------------")
list_first = [5, 3, 8, 1]
sorted_list_first = sorted(list_first, reverse=True)
print(sorted_list_first[0:2], sorted_list_first[-1])


print("--------------задача 2 ---------------")
tuple_1 = ("login", "qa", 7)
x, y, z = tuple_1
print(x)
print(y)
print(z)

copy.deepcopy(tuple_1)
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)  # 1 [2, 3, 4] 5


print("--------------задача 4 ---------------")


def get_duplicate_items(items: list[str]) -> list[str]:
    result: list[str] = []
    counter_dict = Counter(items)
    for k, v in counter_dict.items():
        if v > 1:
            result.append(k)
    return result


list_1 = ["a", "b", "c", "a", "b"]
print(get_duplicate_items(list_1))


print("--------------задача 5 ---------------")


def compare_responses(expected: dict, actual: dict) -> dict[str, list[str]]:
    missing_set = set(expected) - set(actual)
    extra_set = set(actual) - set(expected)
    common = set(actual) & set(expected)
    common_but_different = []
    for k in common:
        if expected[k] != actual[k]:
            common_but_different.append(k)
    return {
        "missing": sorted(missing_set),
        "extra": sorted(extra_set),
        "different": sorted(common_but_different),
    }


dict_expected = {"a": "a", "b": "b", "c": "c"}
dict_actual = {"a": "x", "b": "b", "d": "d"}
print(compare_responses(dict_expected, dict_actual))


print("--------------задача 7 ---------------")
grid = [[0] * 3] * 3

correct_grid = []
counter = 0
for _i in range(0, 3, 1):
    internal_grid = []
    for _j in range(0, 3, 1):
        internal_grid.append(counter)
        counter += 1
    correct_grid.append(internal_grid)
print(grid)
correct_grid[0][0] = 99
print(correct_grid)
