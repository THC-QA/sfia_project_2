import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://localhost:80/")

def test_negative():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://localhost:80/daemon")
    assert r.status == 404