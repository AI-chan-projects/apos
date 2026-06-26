def evaluate_policy(action):
    """
    Returns:
        ALLOW / DENY / APPROVE_REQUIRED
    """

    if action["type"] == "log":
        return "ALLOW"

    if action["type"] in ["delete", "write", "system"]:
        return "APPROVE_REQUIRED"

    return "ALLOW"