# coding=utf-8
import requests
import json

class BaiduTrans:
    def __init__(self,query_string):
        self.headers = {"User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
        self.url = "http://fanyi.baidu.com/v2transapi"
        self.post_data = {
            "from":"zh",
            "to": "en",
            "query": query_string,
            "simple_means_flag": 3
        }


    def parse_url(self):  # 发送请求获取响应
        response = requests.post(self.url,data=self.post_data,headers=self.headers)
        return response.content.decode()

    def get_result(self,temp_string):#转化为字典，提取数据
        temp_dict = json.loads(temp_string)
        result = temp_dict["trans_result"]["data"][0]["dst"]
        return result

    def run(self):
        #1、找到post的地址和需要post的数据
        #2、发送url请求，拿到响应
        temp_string = self.parse_url()
        #3、转化为python类型，提取数据
        result = self.get_result(temp_string)
        print("翻译结果为:",result)

        
baidu_trans = BaiduTrans("我爱你")
baidu_trans.run()

