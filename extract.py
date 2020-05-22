import sys
import urllib
from bs4 import BeautifulSoup
sys_type = sys.getfilesystemencoding()


def gethtml(url):
    page = urllib.urlopen(url)
    html= page.read()
    html.decode('utf-8').encode(sys_type)
    return html


def extract(url):
    pass


urls = [
    ("jazz", "https://music.apple.com/us/playlist/smooth-jazz-essentials/pl.cbefd5b0db0e4d9698da967311cb811c"),
    ("top100", "https://music.apple.com/us/playlist/top-100-france/pl.6e8cfd81d51042648fa36c9df5236b8d"),
    ("puer_french", "https://music.apple.com/us/playlist/pure-french/pl.cf50d6eaeb6c4badbe72d93466694995")
]

for arg in sys.argv[1:]:
    urls.append(arg)

for (name, url) in urls:
    print("Downloading " + url)

    html = gethtml(url)

    page = BeautifulSoup(html, features="html.parser")
    tracks = page.body.findAll('div', attrs={'class': 'row web-preview song'})

    # print(tracks)
    result = ''
    for track in tracks:
        track_name = track.find('div', attrs={'class': 'song-name typography-label'}).text.strip().encode('utf-8')
        artist = track.find('div', attrs={'class': 'by-line typography-caption'}).text.strip().encode('utf-8')
        album = track.find('div', attrs={'class': 'col col-album'}).text.strip().encode('utf-8')

        # print("Name: {}, Artist: {}, Album: {}\n".format(track_name, artist, album))
        # print('"{}","{}","{}"'.format(track_name, artist, album))

        result += '"{}","{}","{}"\n'.format(track_name, artist, album)

    with open("{}.csv".format(name), "w+") as f:
        f.write(result)