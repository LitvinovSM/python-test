import json
from typing import Any


def classify_response(resp: dict[str, Any]) -> str:
    match resp:
        case {"status": 200 | 201, "body": {"id": order_id}}:
            return f"Создана заявка с айди {order_id}"
        case {"status": 200 | 2001}:
            return "Ответ успешный, но нет информации о заявке"
        case {"status": 404}:
            return "Эндпоинт не найден"
        case {"status": status} if 500 <= status < 600:
            return "Ошибка сервера"
        case _:
            return "Неожиданный ответ"


if __name__ == "__main__":
    print(classify_response({"status": 201, "body": {"id": 42}}))
    print(classify_response({"status": 200, "body": {}}))
    print(classify_response({"status": 503}))
    print(classify_response({}))

    items = ["a", "b"]
    for i, item in enumerate(items, start=0):
        if i == 0:
            print(item)

    print("----------------------- Задача 1 ----------------------------------")
    sum = 0
    for i in range(10, 0, -1):
        sum += i
    print(f"sum = {sum}")

    print("----------------------- Задача 2 ----------------------------------")
    for i, j in enumerate(["a", "b", "c"], start=1):
        print(f"{i}.{j}", end=" ")

    print("----------------------- Задача 4 ----------------------------------")

    def http_family_if(status_code: int) -> str:
        result = "unknown"
        if 100 <= status_code < 200:
            result = "information"
        elif 200 <= status_code < 300:
            result = "success"
        elif 300 <= status_code < 400:
            result = "redirect"
        elif 400 <= status_code < 500:
            result = "client error"
        elif 500 <= status_code < 600:
            result = "server error"
        return result

    def http_family_match(status_code: int) -> str:
        match status_code:
            case c if 100 <= c < 200:
                return "information"
            case c if 200 <= c < 300:
                return "success"
            case c if 300 <= c < 400:
                return "redirect"
            case c if 400 <= c < 500:
                return "client error"
            case c if 500 <= c < 600:
                return "server error"
            case _:
                return "unknown"

    print("----------------------- Задача 5 ----------------------------------")

    def missing_fields(required: list[str], actual: dict[str, str]) -> list[str]:
        missing_field_list: list[str] = []

        for required_item in required:
            if required_item in actual:
                continue
            else:
                missing_field_list.append(required_item)
        return missing_field_list

    req_list = ["a", "b", "c"]
    some_dict = {"a": "x", "b": "y"}
    print(missing_fields(req_list, some_dict))

    print("----------------------- Задача 6 ----------------------------------")
    raw = r'{"status": 200, "body": {"items": [{"sku": "A1", "price": 10}, {"sku": "B2", "price": -5}]}}'
    raw_as_dict = json.loads(raw)

    def invalid_items(resp: dict) -> list[str]:
        invalid_items_list = []
        items = resp.get("body", {}).get("items", {})
        for item in items:
            if item.get("price", 0) <= 0:
                invalid_items_list.append(item.get("sku", "missed sku name"))
        return invalid_items_list

    print(invalid_items(raw_as_dict))
