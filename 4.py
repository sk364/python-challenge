import requests
import re
from requests.auth import HTTPProxyAuth

def get_next_number(num, proxies='', auth=''):
	"""
	Returns the next number in the chain
	"""

	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
	res = requests.get('{0}?nothing={1}'.format(url, num), proxies=proxies, auth=auth)

	dat = res.content

	pattern = re.compile(r'next nothing is (\d+)')
	match = pattern.findall(dat)

	if match:
		get_next_number(match[0], proxies=proxies, auth=auth)

	else:
		if "Divide" in dat:
			get_next_number(int(num)/2, proxies=proxies, auth=auth)
		else:
			return dat

if __name__ == '__main__':
	# Proxy variables
	proxies = {'http': 'http://ip:port'}
	auth = HTTPProxyAuth('username', 'password')

	start_num = 12345
	file_name = get_next_number(start_num, proxies=proxies, auth=auth)
	
	print file_name
