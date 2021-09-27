import pytest

from tasks.hard.meta_annotations import StaticTypeMeta


def test_static_typing():
    class Some(metaclass=StaticTypeMeta):
        a: int

    some = Some()
    some.a = 123
    with pytest.raises(ValueError):
        some.a = "123"
