from lib.report_length import *

def test_report_length_returns_correct_output():
    result = report_length("Matilde")
    assert result == "This string was 7 characters long."

def test_string_with_spaces():
    result = report_length("This is a test")
    assert result == "This string was 14 characters long."