import pytest

from tasks.easy.inheritance_polimorphism.duck_typing import (
    AmericanPerson,
    RussianPerson,
    GermanyPerson,
    person_love_science
)


@pytest.mark.parametrize(
    "person_class, expected", (
        (AmericanPerson, "I love science"),
        (RussianPerson, "Я люблю науку"),
        (GermanyPerson, "ich liebe Wissenschaft"),
    )
)
def test_classes(person_class, expected):
    assert person_class().i_love_science() == expected


def test_person_love_science():
    german_person = GermanyPerson()
    assert person_love_science(german_person) == "GermanyPerson says that: ich liebe Wissenschaft"
