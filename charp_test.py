import charp

from typing import Iterable
from matplotlib.text import Text


def test_break2lines():
    s = "1234 1234 1234 1234"
    assert ["1234 1234", "1234 1234"] == charp._break2lines(s), "Must break in 2 lines. Always."


def test_break2lines_middle():
    s = "123 1234 123"
    assert ["123 1234", "123"] == charp._break2lines(s), "Must break in 2 lines. Always."


def test_break2lines_second_bigger():
    s = "123 123 12 12345"
    assert ["123 123", "12 12345"] == charp._break2lines(s), "Must break in 2 lines. Always."


def test_break2lines_acceptable_size():
    s = "123 123 12"
    assert [s] == charp._break2lines(s, len(s))


def build_ticklabels(labels: Iterable[str]) -> Iterable[Text]:
    return [Text(text=label) for label in labels]


def test_break_labels():
    labels = build_ticklabels(["abc cde efg", "abc cde"])
    labels_breaked = charp.break_labels(labels)
    assert ["abc cde\nefg", "abc cde"] == labels_breaked
