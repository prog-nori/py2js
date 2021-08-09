from typing import TypeVar, Union

U = Union[str, int]

T = TypeVar("T", str, int)


def test_union(p: U):
    pass


def test_typevar(p: T):
    pass


test_union(1)  # OK
test_union("union")  # OK
test_union(None)  # NG

test_typevar(2)  # OK
test_typevar("typevar")  # OK
test_typevar(None)  # NG