import pytest

from tasks.easy.abstract_class.animals import (
    Animal,
    Cat,
    Dog,
    Cow
)


def test_animal():
    with pytest.raises(TypeError):
        Animal("SomeName")

    assert hasattr(Animal, "says")


@pytest.mark.parametrize(
    "child, expected_says", (
        (Cat, "SomeName - кошка. Говорит МЯУ!"),
        (Dog, "SomeName - собака. Говорит ГАВ!"),
        (Cow, "SomeName - корова. Говорит МУ!"),
    )
)
def test_child(child, expected_says):
    child_object = child("SomeName")
    assert child_object.says() == expected_says
