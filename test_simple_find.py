import re

import pytest
from hypothesis import given
from hypothesis.strategies import from_regex

from simple_find import match, find_all_patterns

re_matcher = re.compile(r"^\+(|(b(-b)*))((a(-a)*)(b(-b)*))*(|(a(-a)*))\+$")


@given(from_regex(re_matcher, fullmatch=True))
def test_match_with_equivalent_regex(text):
    assert match(text) == len(text)


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
    ("sjknvsdv", -1),  # случайный текст
])
def test_match(text, expected):
    assert match(text) == expected


@pytest.mark.parametrize("text, expected_patterns", [
    ("", []),
    ("a", []),
    ("b", []),
    ("+", []),
    ("-", []),
    ("ab", []),
    ("ba", []),
    ("++", ["++"]),
    ("+a+a+", ["+a+", "+a+"]),
    ("+b+b+", ["+b+", "+b+"]),
    ("+++", ["++", "++"]),
    ("++a++", ["++", "+a+", "++"]),
    ("+ab-ba++ba+", ["+ab-ba+", "++", "+ba+"]),
    ("+ab-b+++aba+bab++", ["+ab-b+", "++", "++", "+aba+", "+bab+", "++"]),
])
def test_find_all_patterns(text, expected_patterns):
    result_patterns = list(text[begin:end] for begin, end in find_all_patterns(text))
    assert result_patterns == expected_patterns
