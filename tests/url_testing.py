import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.230.152.96/")

def test_negative():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.230.152.96/daemon")
    assert r.status == 404