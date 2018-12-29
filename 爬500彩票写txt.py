import requests
from bs4 import BeautifulSoup
import re

#获取网页数据，伪装成浏览器
def gethtml(url):
    headers = {
        "Use-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }
    req = requests.get(url,headers = headers)
    req.encoding = "GBK"
    html = req.text
    bf = BeautifulSoup(html, "html.parser")
    return bf

#爬取标题
def gettitle(html):
    titlehtml = html.find_all("td", class_="td_title01")
    titletxt = str(titlehtml).strip()
    p1 = r'shtml">(.*?)<f.*?<strong>(.*?)</strong>.*?</font>(.*?)</a>.*?right">(.*?)</span>'
    titles = re.compile(p1, re.S).findall(titletxt)
    qi = list(titles[0])
    qi[2] = ('期')
    return ''.join(qi)

#爬取红色球
def getred(html):
    redhtml = html.find_all("li", class_="ball_red")
    redtxt = str(redhtml).strip()
    p1 = r'red">(.*?)</li>'
    reds = re.compile(p1, re.S).findall(redtxt)
    return '红球:' + ' '.join(reds)

#爬取蓝色球
def getbule(html):
    bulehtml = html.find_all("li", class_="ball_blue")
    buletxt = str(bulehtml).strip()
    p1 = r'blue">(.*?)</li>'
    bules = re.compile(p1, re.S).findall(buletxt)
    return '蓝球:' + ' '.join(bules)

#获取所有url
def getlistnum(html):
    listnumhtml = html.find_all("span", class_="iSelectBox")
    p1 = r'href="(.*?)">'
    listnums = re.compile(p1, re.S).findall(str(listnumhtml))
    return listnums[1:]

url = 'http://kaijiang.500.com/shtml/ssq/18131.shtml'
def main():
    html = gethtml(url)
    htmlurls = getlistnum(html)
    for htmlurl in htmlurls:
        ssqhtml = gethtml(htmlurl)
        a = gettitle(ssqhtml)
        b = getred(ssqhtml)
        c = getbule(ssqhtml)
        #写入txt文件
        with open(r'D:\1.txt','a') as f:
            print(htmlurl)
            f.write(a + '\n'+ b + '\n'+ c + '\n')
            f.close()

if __name__ == "__main__":
    main()