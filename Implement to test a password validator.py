import unittest

def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit


# Unit Tests
class TestPasswordValidator(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid_password("StrongPass1"))

    def test_too_short(self):
        self.assertFalse(is_valid_password("Ab1"))

    def test_no_digit(self):
        self.assertFalse(is_valid_password("NoDigitsHere"))

    def test_no_uppercase(self):
        self.assertFalse(is_valid_password("weakpass1"))

    def test_no_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD"))

if __name__ == "__main__":
    unittest.main()
