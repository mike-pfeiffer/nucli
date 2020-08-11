import unittest
from .context import app

OCTET = 8
DOT = "."
LOOPBACK_V4 = "127.0.0.1"


class TestValidationTools(unittest.TestCase):

    def test_decimal_to_binary(self):
        """
        """
        int_10 = 10
        string_10 = "10"
        binary_10 = "00001010"
        not_int = "abcdefg"
        vt = app.ValidationTools()

        test_1 = vt.decimal_to_binary(int_10)
        self.assertEqual(binary_10, test_1)

        test_2 = vt.decimal_to_binary(string_10)
        self.assertEqual(binary_10, test_2)

        test_3 = vt.decimal_to_binary(not_int)
        self.assertIsNone(test_3)

        test_4 = len(vt.decimal_to_binary(int_10))
        self.assertEqual(OCTET, test_4)

    def test_is_unicast(self):
        """
        """
        valid_unicast = ["192.0.2.1", "198.51.100.254", "203.0.113.99"]
        invalid_unicast = ["192.0.2.256", "229.51.100.254", "203.257.113.99"]
        vt = app.ValidationTools()

        for valid in valid_unicast:
            test_1 = vt.is_unicast(valid)
            self.assertTrue(test_1)

        for invalid in invalid_unicast:
            test_2 = vt.is_unicast(invalid)
            self.assertFalse(test_2)

        print(test_1)

    def test_split_address(self):
        """
        """
        vt = app.ValidationTools()
        test_1 = vt.split_address(LOOPBACK_V4)
        test_1 = DOT.join(test_1)
        self.assertTrue(test_1 == LOOPBACK_V4)


if __name__ == "__main__":
    unittest.main()
