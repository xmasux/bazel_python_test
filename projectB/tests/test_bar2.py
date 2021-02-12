import os
import sys
import unittest

import pytest
import xmlrunner

from projectB.src.bar2 import increment_sample


class IncrementSampleTest(unittest.TestCase):

    def test_increment_sample(self):
        self.assertEqual(increment_sample(), 2.)

    def test_increment_sample_two(self):
        self.assertNotEqual(increment_sample(), 1.)


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
