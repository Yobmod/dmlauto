import os
# import unittest

import LOC_count


# class test_countlines(unittest.TestCase):

fold_dir = os.getcwd()


def test_input():
    assert isinstance(fold_dir, str)


def test_output_type():
    x = LOC_count.countlines(fold_dir)
    assert isinstance(x, int)
