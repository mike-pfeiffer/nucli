  
import unittest
from context import app


class TestSorts(unittest.TestCase):

    def test_ping_sweep(self):
        """
        """
        results = app.PingTools.ping_range("10.253.176.70", "10.253.176.77", "")
        print(results)

if __name__ == "__main__":
    unittest.main()
