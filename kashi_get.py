import requests
from bs4 import BeautifulSoup


def get_lyrics(song_title):
    # 曲名で検索ページの HTML 取得
    base_url = f"https://www.uta-net.com/"
    search_url = base_url + f"search/?Keyword={song_title}&Aselect=2&Bselect=3"
    search_res = requests.get(search_url)
    search_soup = BeautifulSoup(search_res.text, "html.parser")

    temp = search_soup.select(".py-2.py-lg-0")
    for item in temp:
        target = item.contents[0].text.strip()
        if target == song_title:
            song_url = base_url + item.get("href")

    # 曲ページの HTML 取得
    song_res = requests.get(song_url)
    song_soup = BeautifulSoup(song_res.text, "html.parser")

    # 歌詞部分のみ取得
    lyric_div = song_soup.find("div", {"id": "kashi_area"})
    lyrics = [s for s in lyric_div.stripped_strings]
    lyrics = "\n".join(lyrics)

    # 歌詞をファイルに保存
    song_title = song_title.replace("?", "？")
    with open(f"./songlist/{artist_name}/{song_title}.txt", "w", encoding="utf-8") as f:
        f.write(lyrics)


if __name__ == '__main__':
    # μ's？Aqours？
    artist_name = "Aqours"
    with open(f"./songlist/{artist_name}_songlist.txt", 'r') as file:
        for line in file:
            print(line.strip())
            get_lyrics(line.strip())
