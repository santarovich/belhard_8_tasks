from pytest_mock import MockerFixture

from tasks.easy.decorators.class_benchmark import def_benchmark, class_benchmark


def test_def_benchmark(mocker: MockerFixture, capsys):
    mocked_time = mocker.patch("time.time", side_effect=[
        1632094935,
        1632094936
    ])

    def get_sum(a, b):
        return a + b

    decorated_get_sum = def_benchmark(get_sum)
    result = decorated_get_sum(2, b=3)
    assert result == 5

    mocked_time.assert_has_calls((mocker.call(), mocker.call()))

    captured = capsys.readouterr()
    assert captured.out == """\
Выполняем get_sum с args: (2,) и kwargs: {'b': 3}
Время начала: 1632094935
Выполнено get_sum
Время окончания: 1632094936
Всего затрачено времени на выполнение: 1
"""


def test_class_benchmark(mocker: MockerFixture):
    mocked_time = mocker.patch("time.time", side_effect=[
        1632094935,
        1632094936
    ])

    @class_benchmark
    class Sum:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def get_sum(self):
            return self.a + self.b

    sum_obj = Sum(2, 3)
    sum_obj.get_sum()

    mocked_time.assert_has_calls((mocker.call(), mocker.call()))
