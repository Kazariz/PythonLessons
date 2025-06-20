import re


def validate_password(password):
    pattern = r'^[A-Za-z0-9@_-]{6,18}$'
    if re.fullmatch(pattern, password):
        return True
    else:
        return False


password = "my-p@ssw0rd"
if validate_password(password):
    print("Пароль корректный.")
else:
    print("Пароль не соответствует требованиям.")
