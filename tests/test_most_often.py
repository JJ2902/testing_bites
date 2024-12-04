from lib.most_often import *

def test_add_new_method():
    listA = []
    mostOftenA = MostOften(listA)

    mostOftenA.add_new("Apple")
    assert mostOftenA.starting_list == ["Apple"]

def test_get_most_often_method():
    
    mostOftenB = MostOften(["Apple","Banana", "Pineapple", "Apple"])
    
    assert mostOftenB.get_most_often() == "Apple"

def test_no_clear_winner_in_list():
    mostOftenC = MostOften(["Apple","Banana", "Pineapple"])

    assert mostOftenC.get_most_often() == "no clear winner"