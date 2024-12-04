import pytest
from lib.present import *

def test_wrap_method():
    presentA = Present()

    
    with pytest.raises(Exception) as e:
        presentA.wrap(None)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap_method():
    presentB = Present()

    
    with pytest.raises(Exception) as e:
        presentB.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


# class Present:
#     def __init__(self):
#         self.contents = None

#     def wrap(self, contents):
#         if self.contents is not None:
#             raise Exception("A contents has already been wrapped.")
#         self.contents = contents

#     def unwrap(self):
#         if self.contents is None:
#             raise Exception("No contents have been wrapped.")
#         return self.contents