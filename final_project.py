import re
import requests
import webbrowser
from bs4 import BeautifulSoup

class Music():
    def __init__(self, song_name, artist):
        self.song_name = song_name
        self.artist = artist

    def youtube_search(self):
        song = self.song_name + " " + self.artist
        new_song = song.split()

        num_words = [len(new_song)]
        ii = num_words[0]
        i = 0
        j = 1

        for word in new_song:
            i = i + 1
            if i > 1 and i < ii + 1:
                new_song.insert(j, "+")
                j = j + 2
                
        search = ["https://www.youtube.com/results?search_query="]
        url_list = search + new_song

        url_string = " ".join(url_list)
        youtube_search_url = ''.join(url_string.split())
 
        result = requests.get(youtube_search_url)
        data = result.text
        soup = BeautifulSoup(data, "html.parser")

        for link in soup.find_all('a', href=re.compile('/watch')):
            r = link.get('href')
            webbrowser.open("https://www.youtube.com"+r)
            break


    def sheet_music(self):
        addition = "sheet music"
        song = self.song_name + " " + self.artist + " " + addition
        new_song = song.split()

        num_words = [len(new_song)]
        ii = num_words[0]
        i = 0
        j = 1

        for word in new_song:
            i = i + 1
            if i > 1 and i < ii + 1:
                new_song.insert(j, "+")
                j = j + 2
                
        search = ["https://www.google.com/#q="]
        url_list = search + new_song

        url_string = " ".join(url_list)
        sheet_music_search_url = ''.join(url_string.split())
        webbrowser.open(sheet_music_search_url)

        
        
        



        





            
        
            
