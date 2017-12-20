import os
# import unittest
import pytest			# type: ignore

import LOC_count


# class test_countlines(unittest.TestCase):

fold_dirs = [os.getcwd(), "./", ".", ("."), ]
fail_dirs = [5, 1001, ["."], (".", ), {".": "str"}, ]


def test_input():
	for fold_dir in fold_dirs:
		assert isinstance(fold_dir, str)


# def test_bad_input():
# 	for fail_dir in fail_dirs:
# 		try:
# 			x = LOC_count.countlines(fail_dir)
# 			assert isinstance(x, int) and (x >= 0)
# 		except TypeError:
# 			assert type(fail_dir) is not str

def test_bad_input2():
	for fail_dir in fail_dirs:
		with pytest.raises(TypeError):
			LOC_count.countlines(fail_dir)		# type: ignore


def test_output_type():
	for fold_dir in fold_dirs:
		x = LOC_count.countlines(fold_dir)
		assert isinstance(x, int) and (x >= 0)


def test_py_output_type():
	for fold_dir in fold_dirs:
		x = LOC_count.pyLines(fold_dir)
		assert isinstance(x, int) and (x >= 0)


def test_js_output_type():
	for fold_dir in fold_dirs:
		x = LOC_count.jsLines(fold_dir)
		assert isinstance(x, int) and (x >= 0)


def test_c_output_type():
	for fold_dir in fold_dirs:
		x = LOC_count.cLines(fold_dir)
		assert isinstance(x, int) and (x >= 0)


def test_typeLines_print_output():
	for fold_dir in fold_dirs:
		x = LOC_count.typeLines_print(fold_dir)
		assert isinstance(x, dict) and (len(x) >= 1)


def test_typeLines_output():
	file_types = ["python", "javascript", "c"]
	for fold_dir in fold_dirs:
		for file_type in file_types:
			x = LOC_count.typeLines(fold_dir, file_type)
			assert isinstance(x, int) and (x >= 0)


def test_typeLines_input():
	fail_types = [5, 1001, "str", {"str": 5}]
	for fold_dir in fold_dirs:
		for fail_type in fail_types:
			if isinstance(fail_type, str):
				with pytest.raises(ValueError):
					LOC_count.typeLines(fold_dir, fail_type)
			else:
				with pytest.raises(TypeError):
					LOC_count.typeLines(fold_dir, fail_type)		# type: ignore
