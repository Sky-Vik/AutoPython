import pytest
from string_utils import StringUtils


string_utils = StringUtils()

"""
Позитивные проверки
"""


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("привет Мир", "Привет мир"),
    ("PYTHON", "Python")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" ", ""),
    ("                                                      hello", "hello"),
    ("      ", ""),
    (" привет Мир", "привет Мир"),
    ("  PYTHON  ", "PYTHON  ")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, search_symbol, expected", [
    ("SkyPro", "S", True),
    ("hello", "ll", True),
    ("12345", "4", True),
    ("", "", True),
    ("привет Мир", "привет Мир", True),
    ("привет Мир", "", True),
    ("PYTHON", "THO", True),
    ("?/.^%", "/.", True)
])
def test_contains_positive(input_str, search_symbol, expected):
    assert string_utils.contains(input_str, search_symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, del_str, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Sky", "Pro"),
    ("12345", "23", "145"),
    ("  привет  Мир ", "  ", "приветМир ")
])
def test_delete_symbol_positive(input_str, del_str, expected):
    assert string_utils.delete_symbol(input_str, del_str) == expected


"""
Негативные проверки
"""


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("?/.^%", "?/.^%"),
    pytest.param(None, None, marks=pytest.mark.xfail)
    # пометить failed, если параметр пустой
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("4566ва", "4566ва"),
    ("", ""),
    ("?/.^%", "?/.^%"),
    ("PYT HON", "PYT HON"),
    pytest.param(None, None, marks=pytest.mark.xfail)
    # пометить failed, если параметр пустой
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, search_symbol, expected", [
    ("4566ва", "s", False),
    ("12", "1234", False),
    ("", "привет Мир", False)
])
def test_contains_negative(input_str, search_symbol, expected):
    assert string_utils.contains(input_str, search_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, search_symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("", "", ""),
    ("123", "12", "3"),
    ("test test test", "", "test test test"),
])
def test_delete_symbol_negative(input_str, search_symbol, expected):
    assert string_utils.delete_symbol(input_str, search_symbol) == expected
