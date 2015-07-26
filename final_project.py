import requests
import webbrowser

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
        final_url = ''.join(url_string.split())
        webbrowser.open(final_url)


#    def sheet_music(self):
#        song = self.song_name + " " + self.artist
#        new_song = song.split()

#        num_words = [len(new_song)]
#        ii = num_words[0]
#        i = 0
#        j = 1

#        for word in new_song:
#            i = i + 1
#            if i > 1 and i < ii + 1:
#                new_song.insert(j, "+")
#                j = j + 2
                
#        search = ["https://www.google.com/#q="]
#        url_list = search + new_song

#        url_string = " ".join(url_list)
#        final_url = ''.join(url_string.split())
#        webbrowser.open(final_url+'sheet'+'music')
        
        



        





            
        
            
