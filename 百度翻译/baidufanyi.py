'''
import requests
import json
class Baidutra:
	"""docstring for Baidutra"""
	def __init__(self,query_string):
                                #self.query_string = query_string
		self.url = "https://fanyi.baidu.com/v2transapi"
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
		self.post_data = {
			"from": "zh",
			'to': 'en',
			'query': query_string,
			'simple_means_flag': 3
		}
	#发送post请求
	def parse_url(self):
		response = requests.post(self.url,data = self.post_data,headers = self.headers)
		return response.content.decode()

	#转换数据,利用loads将string转换成dictionary
	def get_result(self,temp_string):
		temp_dict = json.loads(temp_string)
		result = temp_dict["trans_result"]['data'][0]["dst"]
		return result
	def run(self):
		#1.找到post的地址和需要post的数据
		#2.发送url请求，拿到响应
		temp_string = self.parse_url()
		#3.转化为Python类型，提取数据
		result = self.get_result(temp_string)
		print("翻译结果为：",result)
if __name__ == '__main__':
    baidu= Baidutra("我爱你")
    baidu.run()

'''
import requests
import json
import sys
 
 
class BaiduFanyi:
    def __init__(self, tran_str):
        self.tran_str = tran_str
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
 
    def parse_url(self, url, data):  # 1.2 发送post请求，获取响应
        r = requests.post(url, data=data, headers=self.headers)
        return json.loads(r.content.decode())
 
    def get_url(self, dict_response):
        ret = dict_response["trans"][0]["dst"]
        print("result is :", ret)
 
    def run(self):  # 实现主要逻辑
        # 1.获取语言类型
        # 1.1 准备post的url地址，post_data
        lang_detect_data = {"query": self.tran_str}
        # 1.2 发送post请求，获取响应
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
        # 1.3 提取语言类型
        # 2.准备post的数据
        trans_data = {"query": self.tran_str, "from": "zh", "to": "en"} if lang == "zh" else {"query": self.tran_str,
                                                                                              "from": "en", "to": "zh"}
        # 3.发送请求，获取响应
        dict_response = self.parse_url(self.trans_url, trans_data)
        # 4.提取翻译的结果
        self.get_url(dict_response)
 
 
if __name__ == "__main__":
    trans_str = sys.argv[1]
    baidu_fanyi = BaiduFanyi(trans_str)
    baidu_fanyi.run()

        
