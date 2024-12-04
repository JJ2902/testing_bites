from lib.counter import *

def test_add_count():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5

def test_report_count():
    counterA = Counter()
    counterA.add(7)
    result = counterA.report()
    assert result == "Counted to 7 so far."

def test_both_methods():
    counterB = Counter()
    counterB.add(5)
    assert counterB.count == 5

    result = counterB.report()
    assert result == "Counted to 5 so far."