from collections import defaultdict
from itertools import groupby, product

print("------Разминка 1 -----------")
nums = [3, -1, 4, -1, 5, -9]
print([n for n in nums if n > 0])
print([n**2 for n in nums])
print(["even" if n % 2 == 0 else "odd" for n in nums])

print("------Разминка 2 -----------")
words = ["apple", "Banana", "cherry", "apple"]
print({w: len(w) for w in words})
print({w.lower() for w in words})
print([w for w in sorted(words, key=str.lower)])


print("------Задача 4 -----------")
order_list: list[dict] = [
    {"id": 1, "status": "paid", "total": 100},
    {"id": 2, "status": "unpaid", "total": 200},
    {"id": 3, "status": "paid", "total": 300},
    {"id": 4, "status": "paid", "total": 400},
]


def get_unpaid(order_list: list[dict]) -> list[int]:
    return [order["id"] for order in order_list if order["status"] != "paid"]


def get_id_total_dict(order_list: list[dict]) -> dict:
    return {i["id"]: i["total"] for i in order_list}


def get_max_total_id(order_list: list[dict]) -> float | int:
    return max(order_list, key=lambda oi: oi["total"])["id"]


print(get_unpaid(order_list))
print(get_id_total_dict(order_list))
print(get_max_total_id(order_list))


print("------Задача 5 -----------")

responses_list: list[dict] = [
    {"id": 1, "status": 200, "total": 100},
    {"id": 2, "status": 500, "total": 200},
    {"id": 3, "status": 200, "total": 300},
    {"id": 4, "status": 200, "total": 400},
]


def all_statuses_ok(responses: list[dict]) -> bool:
    return bool(responses) and all(response["status"] == 200 for response in responses)


print(all_statuses_ok(responses_list))


print("------Задача 6 -----------")
browser_list = ["chrome", "yandex"]
languages_list = ["ru", "en"]


def browser_matrix(browsers: list[str], languages: list[str]) -> list[str]:
    return [f"{br}-{lg}" for br, lg in product(browsers, languages)]


print(browser_matrix(browser_list, languages_list))


print("------Задача 8 -----------")
# 8. Дан список результатов [("login", "pass"), ("cart", "fail"), ("pay", "pass"), ("search", "fail")].
# Сгруппируй имена по статусу двумя способами: через defaultdict (модуль 2.3) и через groupby.
# Что нужно сделать с данными, чтобы второй способ дал верный результат? Подсказки по запросу (/hint).
#
# Самопроверка:
# ты заменяешь цикл с append на comprehension там, где он читается проще, и не делаешь этого там, где он усложняет.
# Ты знаешь, что генератор одноразовый, что all([]) истинно, что groupby требует сортировки, и можешь объяснить, что делает key= в sorted.

result_list: list[tuple[str, str]] = [
    ("login", "pass"),
    ("cart", "fail"),
    ("pay", "pass"),
    ("search", "fail"),
]


def group_names_by_status_dict(result):
    d = defaultdict(list)
    for result_name, result_state in result:
        d[result_state].append(result_name)
    return dict(d)


print(group_names_by_status_dict(result_list))


def group_names_by_status_group_by(result):
    sorted_result = sorted(result, key=lambda i: i[1])  # Сортируем по правому значению
    result_of_group = {}
    for result_state, grp in groupby(sorted_result, key=lambda i: i[1]):
        result_of_group[result_state] = [i[0] for i in grp]
    return result_of_group


print(group_names_by_status_group_by(result_list))
