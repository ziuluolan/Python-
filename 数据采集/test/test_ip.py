from bs4 import BeautifulSoup
import requests
import random
import time
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip}
    return proxies
def spider_nsr(ip_list,headers,proxies):
    for ip in ip_list:
        response = requests.get(url = "http://nsr.wiki",headers = headers,proxies = proxies)
 
if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers={
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.9',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Upgrade-Insecure-Requests':'1' }
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17'}
    ip_list = get_ip_list(url, headers=headers)
    for ip in ip_list:
        proxies = get_random_ip(ip_list)
        response = requests.get(url = "http://nsr.wiki",headers = headers,proxies = proxies ,timeout = 2)
        
        print(proxies)
        time.sleep(2)


