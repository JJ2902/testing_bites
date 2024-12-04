from lib.high_value import *

def test_get_highest_value_method():
    highvalueA = HighValue(5, 10)

    result = highvalueA.get_highest()
    assert result ==  "Second value is higher"

    highvalueB = HighValue(5,5)

    resultOne = highvalueB.get_highest()
    assert resultOne == "Values are equal"

def test_first_value_higher():
    highvalueC = HighValue(12, 10)

    result = highvalueC.get_highest()
    assert result == "First value is higher"

def test_add_method_works():
    highValueD = HighValue(26,20)

    highValueD.add(6, "second")
    assert highValueD.value_second == 26

