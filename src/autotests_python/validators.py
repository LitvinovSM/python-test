def is_valid_login(login: str | None) -> bool:
    if not login:
        return False
    stripped = login.strip()
    return 0 < len(stripped) <= 20
