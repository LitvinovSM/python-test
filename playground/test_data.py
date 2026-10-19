import uuid


def make_user(prefix="qa"):
    """Return a dict with a unique login for a test user."""
    suffix = uuid.uuid4().hex[:8]
    return {"login": f"{prefix}_{suffix}", "active": True}


if __name__ == "__main__":
    print(make_user())
