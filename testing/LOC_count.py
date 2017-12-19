import os
from typing import List, Dict, Optional  # , Union, Any, NewType, get_type_hints


def countlines(start: str, lines: int=0, header: bool=True, begin_start: Optional[str]=None) -> int:
	exc_list: List[str] = ["vendor", "dist", "build", "energenie"]
	if header:
		print('{:>10} |{:>10} | {:<20}'.format('ADDED', 'TOTAL', 'FILE'))  # print column titles
		print('{:->11}|{:->11}|{:->20}'.format('', '', ''))  # print line
	ext_tup = ('.py', '.pyx', '.c', '.cpp', '.js', '.jsx', '.ts', '.tsx')
	for thing in os.listdir(start):
		thing = os.path.join(start, thing)
		if os.path.isfile(thing):

			if thing.endswith(ext_tup):
				with open(thing, 'r', encoding="utf8") as f:
					newlines = f.readlines()
					num_lines: int = len(newlines)
					lines += num_lines

					if begin_start is not None:
						reldir_of_thing = '.' + thing.replace(begin_start, '')
					else:
						reldir_of_thing = '.' + thing.replace(start, '')

					print('{:>10} |{:>10} | {:<20}'.format(num_lines, lines, reldir_of_thing))

	for thing in os.listdir(start):
		thing = os.path.join(start, thing)
		if os.path.isdir(thing):
			if any(x in thing for x in exc_list) is False:
				lines = countlines(thing, lines, header=False, begin_start=start)
	return lines


def pyLines(directory: str) -> int:
	exc_list: List[str] = ["vendor", "dist", "build", "energenie"]
	py_lines = 0
	for thing in os.listdir(directory):
		thing = os.path.join(directory, thing)
		if os.path.isfile(thing):
			with open(thing, 'r') as f:
				if thing.endswith(('.py', '.pyx', )):
					newlines = f.readlines()
					py_lines = py_lines + len(newlines)
		elif os.path.isdir(thing) and not any(x in thing for x in exc_list):
				lines = pyLines(thing)
				py_lines = py_lines + lines
	return py_lines


def typeLines(fold_dir: str, file_type: str) -> int:
	exc_list: List[str] = ["vendor", "dist", "build", "energenie"]
	# ext_tup = ()
	lines = 0
	if file_type == "python":
		ext_tup = ('.py', '.pyx', )
	elif file_type == "javascript":
		ext_tup = ('.js', '.jsx', )
	elif file_type == "c":
		ext_tup = ('.c', '.cpp', )
	else:
		if isinstance(file_type, str):
			raise ValueError("allowed filetypes are: 'python', 'javascript', 'c' ")
		else:
			raise TypeError("filetype must be a string")
	for thing in os.listdir(fold_dir):
		thing = os.path.join(fold_dir, thing)
		if os.path.isfile(thing):
			with open(thing, 'r') as f:
				if thing.endswith(ext_tup):
					newlines = f.readlines()
					lines += len(newlines)
		elif os.path.isdir(thing) and not any(x in thing for x in exc_list):
			fold_lines = typeLines(thing, file_type)
			lines += fold_lines
	return lines

# textList = ['a.tif','b.jpg','c.doc','d.txt','e.tif'];
# filteredList = filter(lambda x:x.endswith('.tif'), textList)


def jsLines(directory: str) -> int:
	js_lines = 0
	exc_list: List[str] = ["vendor", "dist", "build", "energenie"]
	for thing in os.listdir(directory):
		thing = os.path.join(directory, thing)
		if os.path.isfile(thing):
			with open(thing, 'r') as f:
				if thing.endswith('.js') or thing.endswith('.jsx'):
					newlines = f.readlines()
					js_lines = js_lines + len(newlines)
		elif os.path.isdir(thing) and not any(x in thing for x in exc_list):
				lines = jsLines(thing)
				js_lines += lines
	return js_lines


def cLines(directory: str) -> int:
	c_lines = 0
	exc_list: List[str] = ["vendor", "dist", "build", "energenie"]
	for thing in os.listdir(directory):
		thing = os.path.join(directory, thing)
		if os.path.isfile(thing):
			with open(thing, 'r', encoding="utf8") as f:
				if thing.endswith('.c') or thing.endswith('.cpp'):
					newlines = f.readlines()
					c_lines = c_lines + len(newlines)
		elif os.path.isdir(thing) and not any(x in thing for x in exc_list):
				lines = cLines(thing)
				c_lines = c_lines + lines
	return c_lines


def typeLines_print(fold_dir: str) -> Dict[str, int]:
	pyLOC = pyLines(fold_dir)
	jsLOC = jsLines(fold_dir)
	cLOC = cLines(fold_dir)
	pyLOC2 = typeLines(fold_dir, "python")
	jsLOC2 = typeLines(fold_dir, "javascript")
	cLOC2 = typeLines(fold_dir, "c")
	print(str(pyLOC) + "py", str(jsLOC) + "js", str(cLOC) + "c")
	print(str(pyLOC2) + "py", str(jsLOC2) + "js", str(cLOC2) + "c")

	return {"py": pyLOC, "js": jsLOC, "c": cLOC, }


if __name__ == "__main__":
	fold_dir = os.getcwd()
	countlines(fold_dir)
	typeLines_print(fold_dir)

# print(get_type_hints(countlines))
