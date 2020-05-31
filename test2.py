import mysql.connector
from mysql.connector import Error
import urllib.request as req
import bs4
import ssl
try:
    def getData():
        connection = mysql.connector.connect(
        host='localhost',          
        database='Jo', 
        user='root',       
        password='') 

        sql = "INSERT INTO gossip (TITLE) VALUES (%s);"
        ssl._create_default_https_context = ssl._create_unverified_context
        
        
        request=req.Request('https://www.ptt.cc/bbs/Gossiping/index.html', headers={
            'cookie':'over18=1',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        })
        with req.urlopen(request) as response:
            data=response.read().decode('utf-8')
       
       
        root=bs4.BeautifulSoup(data, 'html.parser')
        titles=root.find_all('div',class_='title')
        for title in titles:
            if title.a != None:
                new_data = (title.a.string,)
                cursor = connection.cursor()
                cursor.execute(sql, new_data)
        connection.commit() 
    getData()


except Error as e:
    print(e)