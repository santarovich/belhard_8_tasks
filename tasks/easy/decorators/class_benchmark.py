"""
Написать декоратор класса class_benchmark, который будет проводить
бенчмарк (замер времени выполнения) всех публичных методов класса
(те, которые не начинаются с _).

Чтобы у методов класса изменить поведение - дополнительно написать
декоратор функции def_benchmark.

До выполнения метода должен быть вывод в консоль:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода должен быть вывод в консоль:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
from functools import wraps
import time

# start_time = time.time()
# end_time = time.time()
# difference = e - s


def def_benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}\n"
              f"Время начала: {start_time}")
        # end_time = time.time()
        print(f"Выполнено {func.__name__}\n"
              f"Время окончания: {end_time}\n"
              f"Всего затрачено времени на выполнение: {end_time - start_time}")
        return result
    return wrapper


def class_benchmark(cls):
    functions = {
        name: value for name, value
        in cls.__dict__.items()
        if callable(value) and not name.startswith("_")
    }
    for name, func in functions.items():
        func_with_dec = def_benchmark(func)
        setattr(cls, name, func_with_dec)
    return cls


@class_benchmark
class Benchmark:
    attribute = 1

    def function(self):
        return 1 + self.attribute
