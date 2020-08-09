import unittest
from .context import app

LOOPBACK = "127.0.0.1"


class TestPingTools(unittest.TestCase):

    def test_ping(self):
        """
        """
        pt = app.PingTools()
        result = pt.ping(LOOPBACK, "")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
