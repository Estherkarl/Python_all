
def concatenate(s1: str, s2: str) -> str:
    return s1 + s2

def create_string_from_list(lst: list) -> str:
    return ''.join(lst)

def has_digit(s: str) -> bool:
    return any(char.isdigit() for char in s)
