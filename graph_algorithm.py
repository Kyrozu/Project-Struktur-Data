import random

class MusicGraph:
    def __init__(self):
        # Root node for the music graph
        self.graph = {"music": {}}  # This will hold genres and songs
        self.artist = {}  # This will hold artists and their songs

    def add_genre(self, genre):
        """Add a new genre to the graph."""
        if genre not in self.graph["music"]:
            self.graph["music"][genre] = []
            print(f"Genre '{genre}' added.")
        else:
            print(f"Genre '{genre}' already exists.")

    def add_artist(self, artist):
        """Add a new artist to the artist dictionary."""
        if artist not in self.artist:
            self.artist[artist] = []  # Initialize the artist with an empty list of songs
            print(f"Artist '{artist}' added.")
        else:
            print(f"Artist '{artist}' already exists.")

    def add_song(self, genre, song, artist):
        """Add a song to a specific genre and artist."""
        # Check if genre exists
        if genre not in self.graph["music"]:
            print(f"Genre '{genre}' does not exist. Please add it first.")
            return

        # Check if artist exists
        if artist not in self.artist:
            print(f"Artist '{artist}' does not exist. Please add it first.")
            return

        # Add song to genre
        if song not in self.graph["music"][genre]:
            self.graph["music"][genre].append(song)
            print(f"Song '{song}' added to genre '{genre}'.")
        else:
            print(f"Song '{song}' already exists in genre '{genre}'.")

        # Add song to artist's list
        if song not in self.artist[artist]:
            self.artist[artist].append(song)
            print(f"Song '{song}' added to artist '{artist}'.")
        else:
            print(f"Song '{song}' already exists in artist '{artist}'.")

    def search(self, query):
        """Search for a genre or song in the graph."""
        result = []
        # Search in genres
        for genre, songs in self.graph["music"].items():
            if query.lower() in genre.lower():
                result.append(f"Genre: {genre}")
            # Search in songs within the genre
            for song in songs:
                if query.lower() in song.lower():
                    result.append(f"Song: '{song}' in Genre: '{genre}'")
        
        if result:
            print("Search Results:")
            for r in result:
                print(f"- {r}")
        else:
            print(f"No results found for '{query}'.")

    def display_graph(self):
        """Display the music graph."""
        print("\nMusic Graph:")
        for genre, songs in self.graph["music"].items():
            print(f"- {genre}:")
            for song in songs:
                print(f"  - {song}")
        print()

    def recommend_songs(self, song):
        """Provide 10 song recommendations based on the following:
        - 5 songs from the same artist and genre (excluding the selected song)
        - 3 songs from the same genre but different artists
        - 2 songs from the same artist but different genres
        - 2 random songs with no overlap with others
        """
        recommendations = []
        found_song = False
        same_artist_genre = []
        same_genre = []
        same_artist_diff_genre = []
        random_songs = []
        genre_of_song = None
        artist_of_song = None
        recommended_songs = set()  # To track the recommended songs and prevent duplicates
        
        # Step 1: Find the song's genre and artist
        for genre, songs in self.graph["music"].items():
            if song.lower() in [s.lower() for s in songs]:
                genre_of_song = genre
                # Find the artist for the song
                for artist, artist_songs in self.artist.items():
                    if song.lower() in [s.lower() for s in artist_songs]:
                        artist_of_song = artist
                        break
                if not artist_of_song:
                    print(f"Artist for song '{song}' not found.")
                    return
                
                found_song = True
                break
        
        if not found_song:
            recommendations.append(f"Song '{song}' not found in any genre.")
            print(f"Song '{song}' not found in the graph.")
            return

        # **1. 5 songs from the same artist and genre (excluding the selected song)**
        if genre_of_song and artist_of_song:
            same_artist_genre = [s for s in self.graph["music"][genre_of_song] 
                                 if s.lower() != song.lower() 
                                 and s.lower() in [s.lower() for s in self.artist[artist_of_song]]
                                 and s.lower() not in recommended_songs]
            if same_artist_genre:
                recommendations.append(f"5 songs by artist '{artist_of_song}' in Genre '{genre_of_song}':")
                selected_songs = random.sample(same_artist_genre, min(5, len(same_artist_genre)))
                recommendations.extend(selected_songs)
                recommended_songs.update([s.lower() for s in selected_songs])

        # **2. 3 songs from the same genre, but by different artists (excluding the selected song)**
        if genre_of_song:
            same_genre = [s for s in self.graph["music"][genre_of_song] 
                          if s.lower() != song.lower() 
                          and s.lower() not in recommended_songs]
            if same_genre:
                recommendations.append(f"3 songs from Genre '{genre_of_song}' by different artists:")
                selected_songs = random.sample(same_genre, min(3, len(same_genre)))
                recommendations.extend(selected_songs)
                recommended_songs.update([s.lower() for s in selected_songs])

        # **3. 2 songs by the same artist but in different genres (excluding the selected song)**
        if artist_of_song:
            for other_genre, songs in self.graph["music"].items():
                if other_genre != genre_of_song:  # Exclude the current genre
                    same_artist_diff_genre.extend([s for s in songs 
                                                   if s.lower() != song.lower() 
                                                   and s.lower() in [s.lower() for s in self.artist[artist_of_song]]
                                                   and s.lower() not in recommended_songs])
            if same_artist_diff_genre:
                recommendations.append(f"2 songs by artist '{artist_of_song}' in different genres:")
                selected_songs = random.sample(same_artist_diff_genre, min(2, len(same_artist_diff_genre)))
                recommendations.extend(selected_songs)
                recommended_songs.update([s.lower() for s in selected_songs])

        # **4. 2 random songs with no overlap**
        all_songs = [s for genre, songs in self.graph["music"].items() for s in songs]
        random_songs = [s for s in all_songs if s.lower() != song.lower() and s.lower() not in recommended_songs]
        if random_songs:
            recommendations.append(f"2 random songs with no overlap:")
            selected_songs = random.sample(random_songs, min(2, len(random_songs)))
            recommendations.extend(selected_songs)
            recommended_songs.update([s.lower() for s in selected_songs])

        # Display recommendations
        if recommendations:
            print("Recommendation List:")
            for r in recommendations:
                print(f"- {r}")
        else:
            print(f"No recommendations for song '{song}'.")




# Example usage:

# Create a MusicGraph object
music_graph = MusicGraph()
genres = ["pop", "rock", "jazz", "hip-hop", "country", "heavy-metal", "classical", "punk", "soundtrack", "kpop", "jpop"]
for genre in genres:
    music_graph.add_genre(genre)
artists = ["The Weeknd", "Queen", "Dave Brubeck Quartet", "Travis Scott", "Dolly Parton", "Metallica", "Ludwig van Beethoven", "BTS", "Twice", "Aespa", "TWS", "Shannon", "LiSA", "Blackpink"]
for artist in artists:
    music_graph.add_artist(artist)

# Adding songs inside the genre graph
music_graph.add_song("pop", "Blinding Lights", "The Weeknd")
music_graph.add_song("pop", "Light Switch", "Charlie Puth")
music_graph.add_song("pop", "Espresso", "Sabrina Carpenter")
music_graph.add_song("pop", "Yellow", "Coldplay")
music_graph.add_song("rock", "Bohemian Rhapsody", "Queen")
music_graph.add_song("jazz", "Take Five", "Dave Brubeck Quartet")
music_graph.add_song("hip-hop", "Sicko Mode", "Travis Scott")
music_graph.add_song("country", "Jolene", "Dolly Parton")
music_graph.add_song("heavy-metal", "Master of Puppets", "Metallica")
music_graph.add_song("classical", "Symphony No. 5", "Ludwig van Beethoven")
music_graph.add_song("kpop", "Dynamite", "BTS")
music_graph.add_song("kpop", "Strategy", "Twice")
music_graph.add_song("kpop", "TT", "Twice")
music_graph.add_song("kpop", "Lovesick girls", "Blackpink")
music_graph.add_song("kpop", "Whiplash", "Aespa")
music_graph.add_song("kpop", "Last Festival", "TWS")
music_graph.add_song("kpop", "Why Why", "Shannon")
music_graph.add_song("jpop", "Gurenge", "LiSA")
music_graph.add_song("jpop", "Candy Pop", "Twice")

# Display the music graph
music_graph.display_graph()

# Get song recommendations based on a song
music_graph.recommend_songs("Strategy")  # Example song for recommendation
