def is_Valid_Password(password):
    if len(password) < 8:
        return False
    if password.isalpha():
        return False
    if password.isnumeric():
        return False
    return True