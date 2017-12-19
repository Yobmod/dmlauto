import os
from typing import List, Optional  # , Union, Any, NewType, get_type_hints


def countlines(start: str, lines: int=0, header: bool=True, begin_start: Optional[str]=None) -> int:
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
			if "vendor" in thing:
				pass
			else:
				lines = countlines(thing, lines, header=False, begin_start=start)
	return lines


def pyLines(directory: str) -> int:
	exc_list: List[str] = ["vendor", "dist", "build", "energenie"]
	py_lines = 0
	for thing in os.listdir(directory):
		thing = os.path.join(directory, thing)
		if os.path.isfile(thing):
			with open(thing, 'r') as f:
				if thing.endswith('.py') or thing.endswith('.pyx'):
					newlines = f.readlines()
					py_lines = py_lines + len(newlines)
		elif os.path.isdir(thing):
			if any(x in thing for x in exc_list):
				pass
			else:
				lines = pyLines(thing)
				py_lines = py_lines + lines
	return py_lines

# textList = ['a.tif','b.jpg','c.doc','d.txt','e.tif'];
# filteredList = filter(lambda x:x.endswith('.tif'), textList)


def jsLines(directory: str) -> int:
	js_lines = 0
	ts_lines = 0
	for thing in os.listdir(directory):
		thing = os.path.join(directory, thing)
		if os.path.isfile(thing):
			with open(thing, 'r') as f:
				if thing.endswith('.js') or thing.endswith('.jsx'):
					newlines = f.readlines()
					js_lines = js_lines + len(newlines)
				elif thing.endswith('.ts') or thing.endswith('.tsx'):
					newlines = f.readlines()
					ts_lines = ts_lines + len(newlines)
	jsts_lines = js_lines + ts_lines
	return jsts_lines


def cLines(directory: str) -> int:
	c_lines = 0
	for thing in os.listdir(directory):
		thing = os.path.join(directory, thing)
		if os.path.isfile(thing):
			with open(thing, 'r', encoding="utf8") as f:
				if thing.endswith('.c') or thing.endswith('.cpp'):
					newlines = f.readlines()
					c_lines = c_lines + len(newlines)
		elif os.path.isdir(thing):
			if "vendor" in thing:
				pass
			else:
				lines = cLines(thing)
				c_lines = c_lines + lines
	return c_lines


if __name__ == "__main__":
	dir = os.getcwd()
	countlines(dir)
	pyLOC = pyLines(dir)
	jsLOC = jsLines(dir)
	cLOC = cLines(dir)

	print(str(pyLOC) + "py", str(jsLOC) + "js", str(cLOC) + "c")

# print(get_type_hints(countlines))
