import urllib2
import urllib
import re
import socket
import random
socket.setdefaulttimeout(2)
#http://www.56ads.com/article/7112.html
#http://www.56ads.com/proxy/
def spider(url):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib2.build_opener()
    opener.addheaders = [headers]
    try:
        match = '[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\:[0-9]{2,5}'
        page = opener.open(url).read()
        ans = re.findall(match,page)
        return ans
    except Exception,e:
        print e
        return []

def findIP():
    F = open('list.txt','w')
    urls = ['http://www.56ads.com/article/7112.html','http://www.56ads.com/article/7112_2.html']
    for url in urls:
        ips = spider(url)
        #print ips
        for ip in ips:
            if(testIP(ip)):
                F.write('http://'+ip+'/\n')
        
def testIP(ip):
    url = 'http://'+ip+'/'
    pro = urllib2.ProxyHandler({'http':url})
    opener = urllib2.build_opener(pro,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    try:
        content = urllib2.urlopen('http://www.baidu.com').read()
        return True
    except Exception,e:
        print e
        return False
    return False

if __name__=="__main__":
    findIP()
