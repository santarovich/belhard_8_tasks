import pytest

from tasks.easy.inheritance_polimorphism.library import Person, LibraryReader


def test_person():
    person = Person("Fullname", "375557894545")
    assert person.fullname == "Fullname"
    assert person.phone == "375557894545"


def test_library_reader_creation():
    library_reader = LibraryReader("Fullname", "375557894545", 123)

    assert library_reader.fullname == "Fullname"
    assert library_reader.phone == "375557894545"
    assert library_reader.uid == 123
    assert library_reader.books == set()


def test_take_books():
    library_reader = LibraryReader("Fullname", "375557894545", 123)

    expected = {"Азбука", "Буратино"}

    result = library_reader.take_books(*expected)

    assert result == "Fullname взял(а) книги: Азбука, Буратино"
    assert library_reader.books == expected

    new_books = {"Весна", "Дом у озера", "Оно", "Страна радости"}

    expected.update(new_books)
    result = library_reader.take_books(*new_books)
    assert result == "Fullname взял(а) 4 книги"
    assert library_reader.books == expected


def test_return_books():
    library_reader = LibraryReader("Fullname", "375557894545", 123)
    library_reader.books = {
        "Азбука", "Буратино", "Весна", "Дом у озера", "Оно", "Страна радости"
    }
    result = library_reader.return_book(
        "Весна", "Дом у озера", "Оно", "Страна радости"
    )
    assert result == "Fullname вернул(а) 4 книги"

    with pytest.raises(ValueError):
        library_reader.return_book("Азбука", "Страна радости")

    assert len(library_reader.books) == 2
    result = library_reader.return_book("Азбука", "Буратино")
    assert result == "Fullname вернул(а) книги: Азбука, Буратино"
