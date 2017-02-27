import sys

def decrypt(text):
	"""
	Returns the decrypted string
	Decryption is using the following key:
	Add 2 to ascii value of the character
	and replace with original
	"""

	decrypt_text = ''

	for c in text:
		asc_val = ord(c)
		decr_char = chr(asc_val + 2)

		decrypt_text += decr_char

	return decrypt_text


if __name__ == '__main__':
	if len(sys.argv) == 2:
		text = sys.argv[1]

		decr_text = decrypt(text)

		print decr_text

	else:
		print "Err: Not enough arguments!\n"
		print "Usage: python 1.py <string>"
