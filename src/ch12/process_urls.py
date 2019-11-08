from src.ch12.url_utils import gen_from_urls

urls = ('http://facebook.com', 'http://oreilly.com', 'http://google.com')

for len, status, url in gen_from_urls(urls):
    print(len, status, url, sep="->")