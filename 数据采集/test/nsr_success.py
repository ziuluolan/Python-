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
		self.ip_url = 'http://www.xicidaili.com/nn/'
		self.headers={
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.9',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Upgrade-Insecure-Requests':'1' }
    #获取IP 代理池
	def get_ip_list(self):
	    web_data = requests.get(self.ip_url, headers=self.headers)
	    soup = BeautifulSoup(web_data.text, 'lxml')
	    ips = soup.find_all('tr')
	    ip_list = []
	    for i in range(1, len(ips)):
	        ip_info = ips[i]
	        tds = ip_info.find_all('td')
	        ip_list.append(tds[1].text + ':' + tds[2].text)
	    return ip_list
	#从代理池中随机获取 代理ip
	def get_random_ip(self,ip_list):
	    proxy_list = []
	    for ip in ip_list:
	        proxy_list.append('http://' + ip)
	        proxy_ip = random.choice(proxy_list)
	        proxies = {'http': proxy_ip}
	    return proxies

	def spider_now(self,url,proxies):
		print("now parse",self.spider_url)
		response = requests.get(self.spider_url ,headers = self.headers,proxies = proxies)
		try:
			response = requests.get(self.spider_url,headers = self.headers,proxies = proxies)
		except Exception as e:
			print(e)
			return None
		#判断是否到了最后一页
		if response.status_code !=200:
			return	'error'
		return response.content.decode()

	def save_html(self,html,page_number):
		file_path = self.tieba_name+"第{}页.html".format(page_number)
		with open(file_path,'w',encoding = "utf-8") as f:
			f.write(html)
		print("保存成功")

	def run(self):
		#获取ip代理池
		ip_list = self.get_ip_list()
		for i in range(self.spider_nums):
			#随机抽取代理ip
			proxies = self.get_random_ip(ip_list)

			print("spider_now {} pages".format(i))

			temp_html = self.spider_now(self.spider_url,proxies)

			self.save_html(temp_html,i)
			time.sleep(2)
		print("game over")

if __name__ == '__main__':

	#对网站爬取5次
	spider_nsr = Spider_nsr(5)
	spider_nsr.run()
