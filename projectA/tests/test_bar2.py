import os
import sys

import pytest

from projectA.src.bar2 import increment_sample

"""
Multiline comment
"""
def test_increment_sample():
    assert increment_sample() == 2.0


class TestExample:
    # single comment
    def test_increment_sample_in_class(self):
        assert increment_sample() == 2.0


if __name__ == "__main__":
    pytest_args = [
        "--junitxml",
        os.environ.pop("XML_OUTPUT_FILE"),
        "--rootdir",
        os.getcwd(),
    ]
    sys.exit(pytest.main([__file__] + pytest_args))
