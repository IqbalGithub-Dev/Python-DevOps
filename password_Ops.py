def is_Strong_Password(password):
    if len(password) < 8:
        return False
    if "!" not in password and "@" not in password:
        return False
    return True