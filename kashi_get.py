import requests
from bs4 import BeautifulSoup

artist = "Aqours"
song_name = ""

search_url = f"https://www.uta-net.com/search/?Aselect=1&Keyword={artist}+{song_name}&Bselect=3&x=0&y=0"
response = requests.get(search_url)

soup = BeautifulSoup(response.content, "html.parser")

# 検索結果の最初のページの最初の曲を取得
song_link = soup.select_one(
    "div#ichiran > div#kashi_search_list > table > tbody > tr > td.side.td1 > a")

# 曲の詳細ページのURLを取得
song_url = song_link["href"]

# 曲の詳細ページにアクセスしてHTMLを取得
response = requests.get(song_url)
soup = BeautifulSoup(response.content, "html.parser")

# 歌詞を含むHTML要素を取得
lyrics_div = soup.select_one("div#kashi_area")

# 歌詞を抽出
lyrics = lyrics_div.text.strip()

print(lyrics)
