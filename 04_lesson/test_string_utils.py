import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# --- Тесты для capitalize ---

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("s", "S"),
    (" skypro", " skypro"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# --- Тесты для trim ---

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    (" ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# --- Тесты для contains ---

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "S"),
    ("SkyPro", "P"),
    ("SkyPro", "y"),
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol)

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "U"),
    ("", "a"),
])
def test_contains_negative(string, symbol):
    assert not string_utils.contains(string, symbol)

@pytest.mark.positive
def test_contains_empty_symbol():
    assert string_utils.contains("SkyPro", "")

# --- Тесты для delete_symbol ---

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", "SkyPro"),
    ("", "S", ""),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_capitalize_with_date_like_string(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    None
])
def test_capitalize_none(input_str):
    with pytest.raises(AttributeError):
        string_utils.capitalize(input_str)

# --- trim ---

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_trim_with_date_like_string(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    None
])
def test_trim_none(input_str):
    with pytest.raises(AttributeError):
        string_utils.trim(input_str)

# --- contains ---

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
])
def test_contains_none(string, symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(string, symbol)

# --- delete_symbol ---

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),
])
def test_delete_symbol_none(string, symbol):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(string, symbol)