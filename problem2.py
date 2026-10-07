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
    
    count = 0 
    playlist_count = 0 
    
    class History():
        def __init__(self):
            pass 
        
        def log(self, action):
            pass
        
        
    
    def __init__(self, name):
        self.name = name
        self.playlist_count += 1 
        self.list = []
    
    
    #NOTE: song will be a "Song" object from the class above  
    def add_song(self, song):        
        self.list.append(song)
    
    
    def remove_song(self, title):
        for song in self.list:
            if title in self.list:
                self.list.remove(title)
    
    
    @classmethod
    def total_playlists(cls):
        return cls.playlist_count
    
    @staticmethod
    def get_history(seconds):
        pass 
    
    
    
song1 = Song("come as you are", "Nirvana", 2.00)
song2 = Song("beat it", "MJ", 3.00)
song3 = Song("let it be", "beatels", 2.50)















    