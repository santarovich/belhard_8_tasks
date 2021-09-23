import pytest
from math import pi

from tasks.easy.abstract_class.geometry import (
    Shape,
    Circle,
    Rectangle,
    Square
)


def test_shape():
    with pytest.raises(TypeError):
        Shape()

    assert hasattr(Shape, "get_perimeter")
    assert hasattr(Shape, "get_square")


@pytest.mark.parametrize(
    "child, init_args, expected_perimeter, expected_square", (
        (Circle, (5,), 10 * pi, pi * 25),
        (Rectangle, (3, 7), 20, 21),
        (Square, (5,), 20, 25),
    )
)
def test_child(child, init_args, expected_perimeter, expected_square):
    child_object = child(*init_args)
    assert child_object.get_perimeter() == expected_perimeter
    assert child_object.get_square() == expected_square
