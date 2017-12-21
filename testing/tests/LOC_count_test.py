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
	fail_types = [5, 1001, "str", {"str": 5}]
	succ_types = ["python", "javascript", "c"]

	def test_typeLines_print_output(self):
		for fold_dir in self.fold_dirs:
			x = LOC_count.typeLines_print(fold_dir)
			assert isinstance(x, dict) and (len(x) >= 1)

	def test_ext_tupple_input_type(self):
		for folder in self.fold_dirs:
			for fail_type in self.fail_types:
				if isinstance(fail_type, str):
					with pytest.raises(ValueError):
						LOC_count.ext_tupple(fail_type)
				else:
					with pytest.raises(TypeError):
						LOC_count.ext_tupple(fail_type)		# type: ignore
			for succ_type in self.succ_types:
				x = LOC_count.ext_tupple(succ_type)
				assert isinstance(x, tuple) and len(x) > 0
				for item in x:
					assert isinstance(item, str) and len(x) > 0

	def test_typeLines_output(self):
		for fold_dir in self.fold_dirs:
			for file_type in self.file_types:
				x = LOC_count.typeLines(fold_dir, file_type)
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
