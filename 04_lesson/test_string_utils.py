import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# позитивные для trim
@pytest.mark.positive
@pytest.mark.parametrize(
        "input_str, expected",
        [
            ("   skypro", "skypro"),  # Строка с пробелами вначале
            ("skypro", "skypro"),  # Строка без пробелов
            ("  hello world", "hello world"),  # Строка с пробелами и двумя словами
        ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


# негативные для trim
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                     # Пустая строка
    ("   ", ""),                  # Только пробелы
    ("hello  ", "hello  "),       # Пробелы в конце НЕ удаляет!
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# позитивные для capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),          # Строчная → Заглавная первая
        ("hello world", "Hello world"),  # Два слова
        ("python", "Python"),          # Ещё пример
    ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# негативные для capitalize
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),          # Цифры в начале
    ("", ""),                      # Пустая строка
    ("   ", "   "),                # Только пробелы
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Позитивные на contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
   ("Skypro", "S", True),  # Проверяем, что содержит символ в начале
   ("SkyPro", "Pro", True),  # Проверяем, что содержит подстроку
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Негативные на contains
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),  # Символа нет в строке
    ("", "a", False),  # Пустая строка
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# позитивные для delete
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),  # удаляем 1 букву
    ("SkyPro", "Pro", "Sky"),   # удаляем подстроку
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


# негативные для delete
@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),  # символа нет, строка не меняется
    ("", "k", ""),  # пустая строка
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
