import pytest

from tasks.easy.inheritance_polimorphism.transport import (
    Transport,
    Car,
    Airplane
)


def test_transport():
    with pytest.raises(TypeError):
        Transport("toyota", "supra A80", 1999, "black")

    assert hasattr(Transport, "move")


def test_car():
    car = Car("toyota", "supra A80", 1999, "black", "petrol")

    with pytest.raises(ValueError):
        car.move(0)

    with pytest.raises(ValueError):
        car.move(-15)

    result = car.move(15)
    assert car.mileage == 15
    assert result == "toyota supra A80 (black - 1999) проехала 15 километров"


def test_airplane():
    airplane = Airplane("Боинг", "737", 2000, "white", 200)

    with pytest.raises(ValueError):
        airplane.move(0)

    with pytest.raises(ValueError):
        airplane.move(-15)

    result = airplane.move(15)
    assert airplane.mileage == 15
    assert result == "Боинг 737 (white - 2000) пролетел 15 километров"
