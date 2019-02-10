import urllib.request
import urllib.parse
import json

content = input("请输入要翻译的内容: ")

url ='http://fanyi.youdao.com/translate'


Form_Data = {}
Form_Data['type'] = 'AUTO'
Form_Data['i'] = content
Form_Data['from'] = 'AUTO' #自动检测语言
#Form_Data['to'] = 'AUTO'
#Form_Data['smartresult'] = 'dict'
Form_Data['doctype'] = 'json'
Form_Data['version']  = '2.1'
Form_Data['keyfrom'] = 'fanyi.web'
Form_Data['action'] = 'FY_BY_REALTIME'
Form_Data['ue'] = 'UTF-8'
Form_Data['typeResult'] = 'true'


Form_Data = urllib.parse.urlencode(Form_Data).encode("utf-8") 
response = urllib.request.urlopen(url,Form_Data)
html =response.read().decode("utf-8")
#print(html)

taget = json.loads(html)
result=taget['translateResult'][0][0]['tgt']
print("翻译结果为:{}".format(result))



