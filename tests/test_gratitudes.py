from lib.gratitudes import *

# class Gratitudes:
#     def __init__(self):
#         self.gratitudes = []

#     def add(self, gratitude):
#         self.gratitudes.append(gratitude)

#     def format(self):
#         formatted = "Be grateful for: "
#         formatted += ", ".join(self.gratitudes)
#         return formatted

def test_add_method():
    gradA = Gratitudes()

    gradA.add("Thank You")
    assert gradA.gratitudes == ["Thank You"]

def test_format_method():
    gradB = Gratitudes()

    gradB.gratitudes = ["You", "M"]
    assert gradB.format() == "Be grateful for: You, M"