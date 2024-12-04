from lib.string_builder import *

def test_add_method():
    stringBuilderA = StringBuilder()

    stringBuilderA.add("Joy")
    assert stringBuilderA.str == "Joy"

def test_size_method():
    stringBuilderB = StringBuilder()
    stringBuilderB.add("Joy")
    assert stringBuilderB.size() == 3
    
def test_output_method():
    stringBuilderC = StringBuilder()
    stringBuilderC.add("Toy")
    assert stringBuilderC.output() == "Toy"