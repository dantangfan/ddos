import urllib2
import re
import socket
import random
socket.setdefaulttimeout(1)

def findIP():
    i = 6564
    match = '[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\:[0-9]{2,5}'
    F = open('list.txt','w')
    while i>6000:
        tar = open('result.txt')
        ips = tar.read().split('\n')
        index = random.randint(0,len(ips))
        proxy = urllib2.ProxyHandler({'http':ips[index]})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        try:
        	page = urllib2.urlopen('http://www.56ads.com/article/'+str(i)+'.html').read()
        except:
        	continue
        ans = re.findall(match,page)
        for url in ans:
            F.write(url+'\n')
        i = i-1
    F.close()

def testIP():

    url = ''
    content = ''
    F = open('list.txt')
    ips = F.read().split('\n')
    #print ips[0]
    res = open('on.txt','w+')
    for i in ips:
        url = 'http://'+i+'/'
        pro = urllib2.ProxyHandler({'http':url})
        opener = urllib2.build_opener(pro,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        try:
            content = urllib2.urlopen('http://pennyjob.net/').read()
        except:
            pass
        if len(content)>3:
            if content[0:4]=='test':
                print url,' ',content[0:4]
                res.write(url+'\n')
    res.close()

if __name__=="__main__":
    findIP()
    testIP()