import pytest
from string_processor import StringProcessor


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello."),
        ("Hello", "Hello."),
        ("hello world", "Hello world."),
        ("hello.", "Hello."),  # уже есть точка
        ("HELLO", "HELLO."),  # первая буква уже заглавная
    ],
)
def test_process_positive(input_text, expected_output):
    result = StringProcessor.process(input_text)
    assert result == expected_output, f"Для '{input_text}' ожидалось '{expected_output}', получено '{result}'"

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", "."),           # пустая строка
        (" ", " ."),         # один пробел
        ("    ", "    ."),   # четыре пробела
        ("  test  ", "  test  ."),  # пробелы вокруг
    ],
)
def test_process_negative(input_text, expected_output):
    result = StringProcessor.process(input_text)
    assert result == expected_output, f"Для '{input_text}' ожидалось '{expected_output}', получено '{result}'"
