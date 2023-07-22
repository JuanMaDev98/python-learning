import functools


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)  # Se usa functools.update_wrapper en vez de functools.wraps
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):  # El método especial call se ejecuta cada vez que llamas a una instancia de la clase
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print("Whee!")


say_whee()
say_whee()