import urllib.request
import socket
import urllib.error

def proxy(ip):
    import os ; proxy = f'http://{ip}/' ; os.environ['http_proxy'] = proxy ; os.environ['HTTP_PROXY'] = proxy ; os.environ['https_proxy'] = proxy ; os.environ['HTTPS_PROXY'] = proxy

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.example.com')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
#         print('Error code: ', e.code,end='\r')
        return e.code
    except Exception as detail:
#         print("ERROR:", detail,end='\r')
        return True
    return False

def main(timeout):
    socket.setdefaulttimeout(timeout)
    goods=[]
    # two sample proxy IPs
    proxyList = open('freeproxylist','r').read().split('\n')

    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
#             print("Bad Proxy %s" % (currentProxy),end='\r')
            err=1
        else:
#             print("%s is working" % (currentProxy))
            goods.append(currentProxy)
    return(goods)

if __name__ == '__main__':
    timeout=10
    goodips = main(timeout)
    print('good proxies list:\n',goodips)
    with open('goodproxies','w') as proxies:
        for ip in goodips:
            proxies.writelines(f'{ip}\n')
