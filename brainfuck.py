#from typing import Optional


def bf(
		src: str,
		data: str="",
		left: int=0,
		right: int=0,
		idx: int=0,
		strict: bool=True,
			) -> None:
	""" brainfuck interpreter
		src: source string
		left: start index, right: ending index
		data: input data string, idx: start-index of input data string
	"""

	if left < 0 or left >= len(src):
		left = 0
	if right <= 0 or right >= len(src):
		right = len(src) - 1

	arr = [0] * 30000 # turing machine has infinite array size, increase or decrease here
	ptr = 0
	i = left
	while i <= right:
		s = src[i]
		if s == '>':
			ptr += 1
			if ptr >= len(arr):  # wrap if out of range
				ptr = 0
		elif s == '<':
			ptr -= 1
			if ptr < 0:
				ptr = len(arr) - 1  # wrap if out of range
		elif s == '+':
			arr[ptr] += 1
		elif s == '-':
			arr[ptr] -= 1
		elif s == '.':
			print(chr(arr[ptr]), end="")
		elif s == ',':	 # read from data
			if isinstance(data, str):
				if (0 <= idx < len(data)):
					arr[ptr] = ord(data[idx])
					idx += 1
				elif data == "" or idx > len(data):
					arr[ptr] = 0  # out of input
					#print("out of data")
			else:
				raise TypeError("optional data must be a string or empty")
		elif s == '[':
			if arr[ptr] == 0:
				loop = 1
				while loop > 0:
					i += 1
					c = src[i]
					if c == '[':
						loop += 1
					elif c == ']':
						loop -= 1
		elif s == ']':
			loop = 1
			while loop > 0:
				i -= 1
				c = src[i]
				if c == '[':
					loop -= 1
				elif c == ']':
					loop += 1
			i -= 1
		else:
			pass
		i += 1

	#import re
	# match = re.match("^[><+-., \[\]]*$", src)
	# if strict and not match:
	# 	print("\n" + "none bf detected")

	if strict and any(x not in "+-[]<>., " for x in src):
		print("\n" + "non-BF input detected")
	if not src or len(src) == 0:
		print("\n" + "no BF input detected")


if __name__ == "__main__":
	src = input()
	#bf(src, left=0, right=len(src) - 1, data="stringo", idx=0)
	bf(src, data="stringo")
