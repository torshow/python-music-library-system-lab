class Song:
# class attributes shared by every Song instance
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

# update all the tracking infomation everytime a song is made.
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        Song.count += 1

 # add the genre if never seen before
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

#add the artist if never seen before
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

#increment genre's count
    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

#increment artist's count
    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1                                   
