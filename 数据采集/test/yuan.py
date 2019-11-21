import requests
import time 
from bs4 import BeautifulSoup
import random
class Spider_nsr(object):
	"""docstring for Spider_nsr"""
	def __init__(self, spider_nums):
		self.tieba_name = "南师人"
		self.spider_nums = spider_nums
		self.spider_url = "http://nsr.wiki"
		self.proxies = {'http': 'http://171.35.171.148:9999',
						'https': 'http://171.35.171.148:9999'
		}
		self.headers={
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.9',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Upgrade-Insecure-Requests':'1' }
    
	def spider_now(self,url):
		print("now parse",self.spider_url)
		response = requests.get(self.spider_url ,headers = self.headers ,proxies = self.proxies)
		'''
		try:
			response = requests.get(self.spider_url,headers = self.headers,proxies = self.proxies)
		except Exception as e:
			print(e)
			return None
		#判断是否到了最后一页
		'''
		if response.status_code !=200:
			return	'error'
		return response.content.decode()

	def save_html(self,html,page_number):
		file_path = self.tieba_name+"第{}页.html".format(page_number)
		with open(file_path,'w',encoding = "utf-8") as f:
			f.write(html)
		print("保存成功")

	def run(self):
		for i in range(self.spider_nums):
			print("spider_now {} pages".format(i))

			temp_html = self.spider_now(self.spider_url)

			self.save_html(temp_html,i)
			time.sleep(2)
		print("game over")

if __name__ == '__main__':

	#对网站爬取5次
	spider_nsr = Spider_nsr(5)
	spider_nsr.run()
