from tasks.hard.meta_attr import DynamicInitMeta


def test_dynamic_init():
    class Some(metaclass=DynamicInitMeta):
        pass

    some = Some(a=1, b=[1, 2, 3])

    assert some.a == 1
    assert some.b == [1, 2, 3]
