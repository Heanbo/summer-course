"""THIS IS a deffinitiion of what this module (file) does"""

TEST = 3


def my_func(user_input: str) -> str:
    """This is what my function does"""
    print(type(user_input))
    return user_input


print(my_func(TEST))
