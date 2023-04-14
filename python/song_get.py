import requests
from bs4 import BeautifulSoup

# アーティストページのURL
artist_url = f"https://www.uta-net.com/artist/10739/"

# ページの取得
response = requests.get(artist_url)

# ページの解析
soup = BeautifulSoup(response.text, "html.parser")

# 曲一覧を取得
temp = soup.select(".fw-bold.songlist-title.pb-1.pb-lg-0")

temtemp = []
for item in temp:
    temtemp.append(item.text.strip())

song_links = [x for x in temtemp if "TVサイズ" not in x]
print(song_links)

# ファイル名
artist_name = "μ's"
filename = f"./songlist/{artist_name}_songlist.txt"

# ファイルに書き込み
with open(filename, "w") as f:
    for item in song_links:
        f.write("%s\n" % item)
