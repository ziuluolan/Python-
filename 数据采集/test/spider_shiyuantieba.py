import requests
import random
class Tieba(object):
	"""docstring for Tieba"""
	def __init__(self, tieba_name,numbers):
		self.tieba_name = tieba_name
		self.numbers = numbers
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
		self.url_list = []
		#self.proxies={'http':'http://123.169.103.7:9999','https':'https://117.69.200.193:9999'}
		temp_url = "http://tieba.baidu.com/f?kw="+self.tieba_name+"&ie=utf-8&pn={}"
		#获得url 规律
		for i in range(self.numbers+1):
			url = temp_url.format(i*50)
			self.url_list.append(url)
	#判断url是否请求服务器成功
	def panduan(self,url):
		print ("正在爬取")
		try:
			response = requests.get(url,headers = self.headers)#,proxies = self.proxies
		except Exception as error:
			print(error)
			return None
		#判断是否到了最后一页
		if response.status_code != 200:
			return "已经到了最后一页了"
		return response.content.decode()
	#保存
	def save_html(self,html,page_number):
		file_path = self.tieba_name+"第{}页.html".format(page_number)
		with open (file_path,"w",encoding = "utf-8") as f:
			f.write(html)
		print("save successful")
	def run(self):
		for url in self.url_list:
			html = self.panduan(url)
			if html == 'error':
				break
			if html is not None:
				#获取页码数
				page_number = int(int(url.split("=")[-1])/50)+1
				self.save_html(html,page_number)
if __name__ == '__main__':
	tieba = Tieba("南阳师范学院",10)
	tieba.run()