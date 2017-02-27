import sys
import re

def get_pattern(text):
	"""
	Returns the pattern required in Level 4
	"""

	pattern = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
	match = pattern.findall(text)

	return match

if __name__ == '__main__':
	if len(sys.argv) == 2:
		with open(sys.argv[1]) as f:
			text = ''.join([l.rstrip() for l in f.read()])

		pattern = get_pattern(text)

		print pattern

	else:
		print "Err: Not enough arguments\n"
		print "Usage: python 3.py <file_path>"
