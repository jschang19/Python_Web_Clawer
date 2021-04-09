# @Date : 109.7.24
# @Author :Jun Shawn
# 主題：Web crawler - 換頁
# 設計抓取 PTT 3C版有關 iOS 的貼文
# 參考網址： https://ithelp.ithome.com.tw/articles/10202493

import requests as rq  # 引入 requsest 模組
from bs4 import BeautifulSoup  # 引入 BeautifulSoup 模組
url = "https://www.ptt.cc/bbs/MobileComm/index.html"  # 爬蟲網址為 PTT 3c版

p = input("輸入爬蟲的頁數： ")

try:
    # 用往上爬 p 頁
    for x in range(int(p)):
        r = rq.get(url)  # 擷取 url 中的內容, r 代表 ptt 的 code
        soup = BeautifulSoup(r.text,"html.parser")  # 解析 HTML 編碼
        r1 = soup.select("div.title a")  # 抓取 div class = title 的標題文字
        r_next = soup.select("div.btn-group.btn-group-paging a")  # 抓取下一頁的網址
        url = "https://www.ptt.cc" + r_next[1]["href"]  # 更新 url 網址，在下一次回圈時換頁

        # 輸出迴圈
        for s in r1:
            r_title = s.text
            r_url = "https://www.ptt.cc/" + s["href"]  # 宣告前一頁的連結

            # 輸出標題含有 iPhone 的貼文
            if "iPhone" in r_title or "iphone" in r_title:
                device = "iPhone"
                print(device)
                print(r_title,r_url)
                print("-" * 55)

            # 輸出標題含有 iPad 的貼文
            elif "iPad" in r_title or "ipad" in r_title:
                device = "iPad"
                print(device)
                print(r_title, r_url)
                print("-"*55)

            # 輸出標題含有 AirPods 的貼文
            elif "airpods" in r_title or "Airpods" in r_title or "airpod" in r_title:
                device = "Airpods"
                print(device)
                print(r_title, r_url)
                print("-"*55)

            # 輸出標題含有 iOS 的貼文
            elif "ios" in r_title or "iOS" in r_title:
                device = "iOS"
                print(device)
                print(r_title, r_url)
                print("-"*55)

# 當輸入的頁數並非正確數字，抓取錯誤
except ValueError:
    print("請輸入正確的數值")
