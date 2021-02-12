import os
import sys
import unittest

import pytest
import xmlrunner as xmlrunner

from projectB.src.bar2 import is_palindrome


class IsPalindromeTest(unittest.TestCase):
    is_palindrome_params = [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("Never odd or even", True),
        ("Do geese see God?", False),
        ("abc", False),
        ("abab", False),
    ]

    def test_is_palindrome(self):
        for p1, p2 in self.is_palindrome_params:
            with self.subTest(msg="asd", p1=p1, p2=p2):
                self.assertEqual(is_palindrome(p1), p2)


if __name__ == "__main__":
    pytest_args = [
        "--junitxml",
        os.environ.pop("XML_OUTPUT_FILE"),
        "--rootdir",
        os.getcwd(),
    ]
    sys.exit(pytest.main([__file__] + pytest_args))

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output=os.environ.pop("XML_OUTPUT_FILE")),
        failfast=False, buffer=False, catchbreak=False)
