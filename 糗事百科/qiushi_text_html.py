import requests

class Qiu:
	def __init__(self):
		self.temp_url = "https://www.qiushibaike.com/text/page/{}/"
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
		self.parse_times = 2
	#获取url列表
	def get_url_list(self):
		url_list = []
		for i in range(1,14):
			url = self.temp_url.format(i)
			url_list.append(url)
		return url_list
	#2.发送响应并获得响应
	#3.判读是否到了最后一页
	def parse_url(self,url):
		print("now parsing")
		response = requests.get(self.temp_url,headers = self.headers)
		#判断响应是否成功
		#响应失败
		if response.status_code != 200:
			print("parse fail")
			if self.parse_times<4:
				self.parse_times+=1
				return self.parse_url(url)
			else:
				return None
				self.parse_times = 0
		#响应成功
		else:
			print("parse sucessful")
			return response.content.decode()
	#保存html
	def save_html(self,html,page_number):
		save_path = "糗事笑话第{}页.html".format(page_number) 
		with open(save_path,"a",encoding = "utf-8") as f :
			f.write(html)
			print('save successful')
	#主函数
	def run(self):
		#1.找到url规律
		url_list = self.get_url_list()
		for url in url_list:
			temp_html = self.parse_url(url)
			self.save_html(temp_html,int(url_list.index(url))+1)
if __name__ == '__main__':
	qiu = Qiu()
	qiu.run()