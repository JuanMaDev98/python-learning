import functools
import random


def num_blocker(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if value > 50:
            return value
        else:
            return 50
    return wrapper


@num_blocker
def random_num():
    return random.randint(0, 100)


print(random_num())