import requests
class Spider_58:
	def __init__(self):
		self.temp_url = "https://ny.58.com/chuzu/pn{}/"
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
		self.parse_times = 0
	#1.发现url规律
	def parse_url(self,url):
		response = requests.get(self.temp_url,headers = self.headers)
		if response.status_code !=200: #如果没有获取响应
			print("parse fail")
			if self.parse_times<3:
				self.parse_times+=1
				return self.parse_url(url)
			else:
				return None       #三次请求都未获得响应，可能是到了最后一页，也可能是被发现

				self.parse_times = 0
		else:
			return response.content.decode() #获取了响应
			print("parse succeful")
			self.parse_times = 0

	def save_html(self,html,page_number):
		save_path = "58同城第{}页.html".format(page_number)
		with open(save_path,"w",encoding = "utf-8") as f:
			f.write(html)
			print("save succeful")


	def run(self):
		#1.发现url规律
		for i in range(1,11):#获取前10 页的HTML信息
			url = self.temp_url.format(i)
			#2.发送请求,获取响应
			#3.判断是否到了最后一页
			temp_html = self.parse_url(url)
			#4.保存html信息
			self.save_html(temp_html,i)


if __name__ == '__main__':
	spider = Spider_58()
	spider.run()

		
