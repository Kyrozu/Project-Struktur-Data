from node import Node

class MusicGraph:
    def __init__(self):
        # Root node for the music graph
        self.graph = {"music": {}}

    def add_genre(self, genre):
        """Add a new genre to the graph."""
        if genre not in self.graph["music"]:
            self.graph["music"][genre] = []
            print(f"Genre '{genre}' added.")
        else:
            print(f"Genre '{genre}' already exists.")

    def add_song(self, genre, song):
        """Add a song to a specific genre."""
        if genre in self.graph["music"]:
            if song not in self.graph["music"][genre]:
                self.graph["music"][genre].append(song)
                print(f"Song '{song}' added to genre '{genre}'.")
            else:
                print(f"Song '{song}' already exists in genre '{genre}'.")
        else:
            print(f"Genre '{genre}' does not exist. Please add it first.")

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


music_graph = MusicGraph()

genres = ["pop", "rock", "jazz", "hip-hop", "country", "heavy-metal", "classical", "punk", "soundtrack", "kpop", "jpop"]
for genre in genres:
    music_graph.add_genre(genre)

# Adding songs inside the genre graph
music_graph.add_song("pop", "Blinding Lights")
music_graph.add_song("rock", "Bohemian Rhapsody")
music_graph.add_song("jazz", "Take Five")
music_graph.add_song("hip-hop", "Sicko Mode")
music_graph.add_song("country", "Jolene")
music_graph.add_song("heavy-metal", "Master of Puppets")
music_graph.add_song("classical", "Symphony No. 5")
music_graph.add_song("kpop", "Dynamite")
music_graph.add_song("jpop", "Gurenge")

# Display
music_graph.display_graph()

# Search
music_graph.search("rock")
music_graph.search("Dynamite")
music_graph.search("Symphony")
music_graph.search("blinding")
