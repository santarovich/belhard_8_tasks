import pytest

from tasks.easy.incapsulation.book_card import BookCard, CURRENT_YEAR


@pytest.mark.parametrize(
    "author, title, year", (
        (1, "Book", 1995),
        ("Author", 2, 1995),
        ("Author", "Book", "1995"),
        ("Author", "Book", -15),
        ("Author", "Book", CURRENT_YEAR + 1),
    )
)
def test_creation_with_bad_arguments(author, title, year):
    with pytest.raises(ValueError):
        BookCard(author, title, year)


@pytest.mark.parametrize(
    "property_name, real_name, value", (
        ("author", "_BookCard__author", "New author"),
        ("title", "_BookCard__title", "New title"),
        ("year", "_BookCard__year", 2000),
        ("year", "_BookCard__year", CURRENT_YEAR),
    )
)
def test_property_with_good_data(property_name, real_name, value):
    bc = BookCard("Author", "Book", 1995)
    assert hasattr(bc, real_name)
    setattr(bc, property_name, value)
    assert getattr(bc, real_name) == value


@pytest.mark.parametrize(
    "property_name, value", (
        ("author", 1),
        ("title", 2),
        ("year", "not year"),
        ("year", 0),
        ("year", -123),
        ("year", CURRENT_YEAR + 123),
    )
)
def test_book_card(property_name, value):
    bc = BookCard("Author", "Book", 1995)
    with pytest.raises(ValueError):
        setattr(bc, property_name, value)
