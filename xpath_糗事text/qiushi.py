import requests
from lxml import etree
import json

class Qiubai:
	def __init__(self):
		self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
		self.parse_times = 2

	def get_url_list(self): #获取url列表
		url_list = []
		for i in range (1,14):
			url = self.url_temp.format(i)
			url_list.append(url)
		return url_list

	def parse_url(self,url): #发送请求，获取HTML，转化为elements对象
		print("now parsing:",url)
		response = requests.get(url,headers = self.headers,timeout = self.parse_times)
		html = etree.HTML(response.content) #用etree方法进行训练
		return html  #此时的html可以使用xpath 了 elements对象

	def get_content(self,html):
		div_list = html.xpath("//div[contains(@id,'qiushi_tag')]")
		item_list = []
		for div in div_list:#遍历div列表，继续写xpath
			author_img = div.xpath("./div[@class='author clearfix']/a[1]/img/@src")
			author_img = "https:"+author_img[0] if len(author_img)>0 else None
			author_name = div.xpath("./div[@class = 'author clearfix']/a[1]/img/@alt")
			author_name = author_name[0] if len(author_name)>0 else None
			author_gender = div.xpath("./div[@class = 'author clearfix']/div[contains(@class,'articleGender')]/@class")
			author_gender = author_gender[0].split(" ")[-1].replace("Icon",'') if len(author_gender)>0 else None
			author_age = div.xpath("./div[@class = 'author clearfix']/div[contains(@class,'articleGender')]/text()")
			author_age = author_age[0] if len(author_age)>0 else None
			#段子内容
			content = div.xpath(".//div[@class='content']/span/text()")
			content = [i.replace("\n", "") for i in content]
			#好笑数量
			stats_vote = div.xpath(".//span[@class = stats-vote]/i/text()")
			stats_vote = stats_vote[0] if len(stats_vote)>0 else None
			#评论数量
			stats_comments = div.xpath(".//span[@class='stats-comments']/a/i/text()")
			stats_comments =stats_comments[0] if len (stats_comments)>0 else None
			#最佳评论作者
			cmt_name = div.xpath(".//div[@class='cmtMain']/span[@class='cmt-name']/text()")
			cmt_name = cmt_name[0].replace("：","") if len (cmt_name)>0 else None
			#最佳评论内容
			cmt_comment = div.xpath(".//div[@class= 'cmtMain']/div[@class ='main-text']/text()")
			cmt_comment = cmt_comment[0].replace("\n", "") if len(cmt_comment) > 0 else None
			#最佳评论点赞数
			cmt_comment_likenum = div.xpath(".//div[@class='cmtMain']//div[@class='likenum']/text()")
			cmt_comment_likenum = [i.replace("\n","") for i in cmt_comment_likenum ]
			cmt_comment_likenum = [i for i in cmt_comment_likenum if i ][0] if len([i for i in cmt_comment_likenum if i ])>0 else None


			item = dict(author_img = author_img,
			author_name = author_name,
			author_gender = author_gender,
			author_age = author_age,
			content = content,
			stats_vote = stats_vote,
			stats_comments = stats_comments,
			cmt_name = cmt_name,
			cmt_comment = cmt_comment,
			cmt_comment_likenum = cmt_comment_likenum
			)
			item_list.append(item)
		return item_list
	def save_item_list(self,item_list):
		with open ("qiubai.txt","a",encoding = "utf-8") as f:
			for item in item_list:
				f.write(json.dumps(item, ensure_ascii=False, indent=2))
				f.write("\n"+"*"*100+"\n")
		print("save success")

	def run(self):
		#1.构造url地址
		url_list = self.get_url_list()
		#2.发送请求，获取响应
		for url in url_list:
			#获取html
			html = self.parse_url(url)
			#3.提取数据
			item_list = self.get_content(html)
			#4.保存
			self.save_item_list(item_list)
if __name__ == '__main__':
	qiubai = Qiubai()
	qiubai.run()

