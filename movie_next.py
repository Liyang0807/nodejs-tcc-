import urllib.request as req
def getData(url):
    request=req.Request(url, headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data=response.read().decode('utf-8')
    #print(data)
    import bs4
    root=bs4.BeautifulSoup(data, 'html.parser')
    titles=root.find_all('div',class_='title')
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextPage=root.find('a',string='‹ 上頁')
    return nextPage['href']
pageUrl='https://www.ptt.cc/bbs/movie/index.html'
count=0
while count<10:
    pageUrl='https://www.ptt.cc'+getData(pageUrl)
    count+=1