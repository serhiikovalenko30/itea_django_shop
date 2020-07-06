import re


def phone_formatting(value):
    return re.sub(r'\D', '', value)
