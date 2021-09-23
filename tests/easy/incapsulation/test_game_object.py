import pytest

from tasks.easy.incapsulation.game_obj import GameObject


def test_game_object():
    point = GameObject(0, 0)

    assert hasattr(point, "_GameObject__x")
    assert hasattr(point, "_GameObject__y")
    assert getattr(point, "_GameObject__x") == 0
    assert getattr(point, "_GameObject__y") == 0
    assert point.x == 0
    assert point.y == 0

    with pytest.raises(AttributeError):
        point.x = 1  # noqa

    with pytest.raises(AttributeError):
        point.y = 1  # noqa

    point.move(5, -5)

    assert point.x == 5
    assert point.y == -5
