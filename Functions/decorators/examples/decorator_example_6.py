import functools
import time


def slow_down(total_time=1):
    def slow_down_internal(func):
        """Sleep 1 second before calling the function"""
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(total_time)
            return func(*args, **kwargs)
        return wrapper_slow_down
    return slow_down_internal


@slow_down(total_time=2)
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


countdown(5)

