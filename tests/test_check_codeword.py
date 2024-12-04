from lib.check_codeword import *

def test_check_codeword_returns_Correct_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_returns_elif_results():
    result = check_codeword("hose")
    assert result == "Close, but nope."

def test_check_codeword_returns_else_results():
    result = check_codeword("Boo")
    assert result == "WRONG!"