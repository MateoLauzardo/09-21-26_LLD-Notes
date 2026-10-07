# Concepts: aggregation, composition, nested class, class method, static method

# Design a playlist system.

# Songs exist on their own and can appear in many playlists. 

# Each playlist also keeps its own private history log, which only exists as long as the playlist does.


# https://claude.ai/share/5d4aac69-4dbb-46d1-a487-125c908e4b38

#! aggregation -> when you pass in object in parameter so opposite of constructor ("has a")
#! composition -> when you create object inside constructor ("owns a")
#! nested class -> a class within a class. You tend to call nested class from within first (comp)
#! class method -> to keep count of how many times instance was created OR to create an instance of the class it is CLS
#! static method -> a method where anyone call it and doesnt need to make object 


class Song():
    def __init__(self, title, author, duration):
        self.title = title 
        self.author = author 
        self.duration = duration



class Playlist():
    
    # class method varaibles 
    playlist_count = 0 
    
    
    #TODO - is a list of events such as, "added beat it", "removed beat it"
    class History():
        def __init__(self):
            self.history_list = []
        
        def log(self, action):
            self.history_list.append(action)
        
        
    
    def __init__(self, name):
        self.name = name
        
        Playlist.playlist_count += 1 
        
        # we do .self cuz it lives inside playlist aka "self"
        #! for comp, you create the object within the constructor. 
        self.history = self.History()
         
        self.list = []

    
    def add_song(self, song):        
        self.list.append(song)
        
        self.history.log(f"added {song.title}")
        
    
    def remove_song(self, title):
        self.list = [song for song in self.list if song.title != title]

        self.history.log(f"removed {title}")
    
    

    def get_history(self):
        return self.history.history_list

    
    def return_playlist_songs(self):
        song_names = []
        
        for songs in self.list:
            song_names.append(songs.title)

        return song_names
    
    
    @classmethod
    def total_playlists(cls):
        return cls.playlist_count
    
    
    @staticmethod
    def format_duration(seconds):
        # 120 seconds -> 2.00 
        result = seconds / 60
        return f"{result:.2f}"
    
    
    
song1 = Song("come as you are", "Nirvana", 2.00)
song2 = Song("beat it", "MJ", 3.00)
song3 = Song("let it be", "beatels", 2.50)

playlist = Playlist("yolo")
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)
print(playlist.return_playlist_songs())












    