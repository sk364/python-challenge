import zipfile
import re

START = 90052

def get_next_number(num, nums=[]):
	"""
	Returns a list of numbers traversed
	in files
	"""

	with open('channel/{}.txt'.format(num)) as f:
		dat = f.read()

	pattern = re.compile(r'Next nothing is (\d+)')
	match = pattern.findall(dat)

	if match:
		rnum = get_next_number(match[0], nums=nums)
		if rnum:
			nums.append(rnum)
		return int(match[0])
	else:
		return ''

if __name__ == '__main__':
	numlist = []
	get_next_number(START, nums=numlist)

	numlist = [numlist[i] for i in xrange(len(numlist)-1, -1, -1)]

	zp = zipfile.ZipFile('channel.zip')

	comments = ''

	for n in numlist:
		zfile = zp.getinfo('{}.txt'.format(n))

		comments += zfile.comment

	print ''.join(comments)
