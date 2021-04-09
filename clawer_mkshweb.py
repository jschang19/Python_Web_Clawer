import requests

from bs4 import BeautifulSoup

mksh = requests.get("http://www.mksh.phc.edu.tw/Default.aspx")
#將網頁資料GET下來

soup = BeautifulSoup(mksh.text,"html.parser")
#將網頁資料以html.parser

#tag_td =soup.find_all( href = re.compile("Anonymous/NewsDetail"))

tag_td = soup.select("td.gvdot a")

for s in tag_td :
    title_news = s.text

    link_news = s.get("href")

    if "NewsDetail" in link_news:

        print(title_news)
        print("http://www.mksh.phc.edu.tw/Default.aspx/" + link_news)
        print("-"*45)