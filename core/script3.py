import urllib3

if __name__ == "__main__":
    
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.google.com')
    print (r.status)
    print (r.data)
