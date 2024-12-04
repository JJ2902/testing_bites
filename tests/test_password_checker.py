import pytest
from lib.password_checker import *

def test_check_method_exception():
    passwordA = PasswordChecker()

    with pytest.raises(Exception) as e:
        passwordA.check("Boo")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."