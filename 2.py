import sys

def get_rare_chars(text):
	"""
	Returns dictionary of rare characters
	"""

	chars,rare = {}, {}

	for c in text:
		chars[c] = chars.get(c,0) + 1

	for k in chars:
		if chars[k] < 2:
			rare[k] = chars[k]

	return rare

if __name__ == '__main__':
	if len(sys.argv) == 2:
		with open(sys.argv[1]) as f:
			text = ''.join([l.rstrip() for l in f.read()])

		rare = get_rare_chars(text)

		print rare

	else:
		print "Err: Not enough arguments\n"
		print "Usage: python 2.py <file_path>"
