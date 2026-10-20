import json


def load_user(raw):
    return json.loads(raw)


print(load_user("not json"))
