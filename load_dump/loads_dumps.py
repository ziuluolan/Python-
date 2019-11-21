import requests
import json
import pprint

'''
url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"

response = requests.get(url)

response_string = response.content.decode()

#将字符串转化成字典
response_dict = json.loads(response_string)

f = open("douban.txt","w")

json.dump(response_dict,f,ensure_ascii = False,indent = 2)

f.close()
'''
f = open("douban.txt","r")
ret = json.load(f)
pprint.pprint(ret)
