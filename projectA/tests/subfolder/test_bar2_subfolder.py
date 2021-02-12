import os
import sys

import pytest

from projectA.src.bar2 import is_palindrome


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", False),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result


@pytest.mark.parametrize("y", [2, 3])
@pytest.mark.parametrize("x", [0, 1])
def test_foo(x, y):
    pass


@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected


class TestExample:
    @pytest.mark.parametrize("y", [2, 3])
    @pytest.mark.parametrize("x", [0, 1])
    def test_foo_in_class(self, x, y):
        pass


if __name__ == "__main__":
    pytest_args = [
        "--junitxml",
        os.environ.pop("XML_OUTPUT_FILE"),
        "--rootdir",
        os.getcwd(),
    ]
    sys.exit(pytest.main([__file__] + pytest_args))
