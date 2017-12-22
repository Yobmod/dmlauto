import os
import pytest			# type: ignore
from .. import LOC_count
# import unittest
# import sys
# sys.path.append('..')


class Test_Countlines():
	fold_dirs = [os.getcwd(), "./", ".", ("."), ]
	fail_dirs = [5, 1001, ["."], (".", ), {".": "str"}, "./not_exist", ]

	def test_input(self) -> None:
		for fold_dir in self.fold_dirs:
			assert isinstance(fold_dir, str)

	def test_bad_input(self):
		for fail_dir in self.fail_dirs:
			if isinstance(fail_dir, str):
				with pytest.raises(FileNotFoundError):
					LOC_count.countlines(fail_dir)		# type: ignore
			else:
				with pytest.raises(TypeError):
					LOC_count.countlines(fail_dir)		# type: ignore

	def test_output_type(self):
		for fold_dir in self.fold_dirs:
			x = LOC_count.countlines(fold_dir)
			assert isinstance(x, int) and (x >= 0)


class TestPyJsCLines():
	fold_dirs = [os.getcwd(), "./", ".", ("."), ]

	def test_py_output_type(self):
		for fold_dir in self.fold_dirs:
			x = LOC_count.pyLines(fold_dir)
			assert isinstance(x, int) and (x >= 0)

	def test_js_output_type(self):
		for fold_dir in self.fold_dirs:
			x = LOC_count.jsLines(fold_dir)
			assert isinstance(x, int) and (x >= 0)

	def test_c_output_type(self):
		for fold_dir in self.fold_dirs:
			x = LOC_count.cLines(fold_dir)
			assert isinstance(x, int) and (x >= 0)


class TestTypeLines():
	fold_dirs = [os.getcwd(), "./", ".", ("."), ]
	fail_dirs = [5, 1001, ["."], (".", ), {".": "str"}, "./not_exist", ]

	fail_types = [5, 1001, "str", None, {"str": 5}, ["jkld", 7], ]
	fail_tups = [(4, 2000), (5, "wrg"), ("djkl", "jlk"), ]
	succ_types = [
		"python", "javascript", "c", "ts", "cy", ("js", "py", "C"),
		".py", ".txt", ".INI", (".js", ".md")
	]

	black_list_types = ["folder", ["fold", "not"], ("allowed", "use")]

	def test_typeLines_print_output(self):
		for fold_dir in self.fold_dirs:
			x = LOC_count.typeLines_print(fold_dir)
			assert isinstance(x, dict) and (len(x) >= 1)

	def test_bad_input(self):
		for fail_dir in self.fail_dirs:
			for succ_type in self.succ_types:
				if isinstance(fail_dir, str):
					with pytest.raises(FileNotFoundError):
						LOC_count.typeLines(fail_dir, succ_type)		# type: ignore
				else:
					with pytest.raises(TypeError):
						LOC_count.typeLines(fail_dir, succ_type)		# type: ignore

	def test_ext_tuple_input_type(self):
		for folder in self.fold_dirs:
			for fail_type in self.fail_types:
				if isinstance(fail_type, str):
					with pytest.raises(ValueError):
						LOC_count.ext_tuple(fail_type)
				else:
					with pytest.raises(TypeError):
						LOC_count.ext_tuple(fail_type)		# type: ignore

	def test_ext_tuple_input_tup(self):
			for fail_tup in self.fail_tups:
				if all(isinstance(x, str) for x in fail_tup):
					with pytest.raises(ValueError):
						LOC_count.ext_tuple(fail_tup)
				else:
					with pytest.raises(TypeError):
						LOC_count.ext_tuple(fail_tup)

	def test_exclude_list(self):
		for black_list in self.black_list_types:
			if isinstance(black_list, (str, list)):
				x = LOC_count.exclude_list(black_list)
				assert isinstance(x, list) and len(x) > 0
			else:
				with pytest.raises(TypeError):
					x = LOC_count.exclude_list(black_list)

	def test_typeLines_output(self):
		for fold_dir in self.fold_dirs:
			for succ_type in self.succ_types:
				x = LOC_count.typeLines(fold_dir, succ_type)
				assert isinstance(x, int) and (x >= 0)

	def test_typeLines_input(self):
		for fold_dir in self.fold_dirs:
			for fail_type in self.fail_types:
				if isinstance(fail_type, str):
					with pytest.raises(ValueError):
						LOC_count.typeLines(fold_dir, fail_type)
				else:
					with pytest.raises(TypeError):
						LOC_count.typeLines(fold_dir, fail_type)		# type: ignore
