from autotests_python.validators import is_valid_login


def test_is_valid_login_none():
    assert not is_valid_login(None)


def test_is_valid_login_empty():
    assert not is_valid_login(" ")


def test_is_valid_login_20():
    assert is_valid_login("12345678901234567890")


def test_is_valid_login_21():
    assert not is_valid_login("123456789012345678901")
