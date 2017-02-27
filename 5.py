import pickle
import sys

if __name__ == '__main__':
	if len(sys.argv) == 2:
		with open(sys.argv[1]) as f:
			dat = f.read()

		char_map = pickle.loads(dat)

		for l in char_map:
			print ''.join([c[0]*c[1] for c in l])
