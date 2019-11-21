import requests

class TiebaSpider(object):
	def __init__(self,tieba_name,numbers):
		self.tieba_name = tieba_name
		self.numbers = numbers
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
		#找到url规律，获取每一页的url地址
		self.url_list = []
		temp_url = "http://tieba.baidu.com/f?kw="+self.tieba_name+"&ie=utf-8&pn={}"
		#循环获取url规律
		for i in range(self.numbers):
			url = temp_url.format(i*50)
			self.url_list.append(url)
	#3.判断是否请求成功		
	def parse_url(self,url):
		print("now parse",url)
		try:
			response = requests.get(url,headers = self.headers)
		except Exception as e:
			print(e)
			return None
		#判断是否到了最后一页
		if response.status_code !=200:
			return	'error'
		return response.content.decode()

	#4.保存
	def save_html(self,html,page_number):
		file_path = self.tieba_name+"第{}页.html".format(page_number)
		with open(file_path,'w',encoding = "utf-8") as f:
			f.write(html)
		print("保存成功")

	def run(self):
		#1.找到url规律，获取每一页的url地址
		for url in self.url_list:
			#2.发送请求获取响应
			html = self.parse_url(url)
			#3.判断是否请求成功
			if html == 'error':
				break
			if html is not None:
				#4.保存
				page_number = int(int(url.split("=")[-1])/50) +1 #获取页码数
		
				self.save_html(html,page_number)

if __name__ == '__main__':
	tieba = TiebaSpider("南阳师范学院",10)
	tieba.run()


