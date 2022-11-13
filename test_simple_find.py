import pytest

from simple_find import match


@pytest.mark.parametrize("text, expected", [
    ("", -1),
    ("a", -1),
    ("b", -1),
    ("+", -1),
    ("-", -1),
    ("ab", -1),
    ("ba", -1),
    ("++", 2),
    ("+a+", 3),
    ("+b+", 3),
    ("+ab+", 4),
    ("+ba+", 4),
    ("+a+b+", 3),
    ("+b+a+", 3),
    ("+a-a+", 5),
    ("+b-b+", 5),
    ("+a-b+", -1),
    ("+b-a+", -1),
    ("+a+a+", 3),
    ("+b+b+", 3),
    ("+ab-b+", 6),
    ("+ba-a+", 6),
    ("+ab-a+", -1),
    ("+ba-b+", -1),
    ("+ab-ba+", 7),
])
def test_match(text, expected):
    assert match(text) == expected
