
class Song:
    # Class attributes
    
    # Keeping track of the total count of songs
    count = 0
    
    #  storing  unique genres,artists
    genres = []
    artists = []
    
    #  attribute to store the count of songs for each genre
    genre_count = {}
    
    # attribute to store the count of songs for each artist
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes 
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Incrementing the total count of songs
        Song.count += 1
        
        # Adding the genre to the list of unique genres
        Song.add_to_genres(genre)
        
        # Adding an artist to the list of unique artists
        Song.add_to_artists(artist)
        
        # Updating the count of songs for the genre
        Song.add_to_genre_count(genre)
        
        # Updating the count of songs for the artist
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_to_genres(cls, genre):
        # Checking if the genre is not already present in the genres list
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        # Check if the artist is not already present in the artists list
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        # Check if the genre already exists as a key in the genre_count dictionary
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            # Adding a new key-value pair with the genre as the key set to 1 as the initial value
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        # Check if the artist already exists as a key in the artist_count dictionary
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            # Adding a new key-value pair with the artist as the key and 1 as the initial value
            cls.artist_count[artist] = 1