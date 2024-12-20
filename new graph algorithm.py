import random
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    """A class representing a node in the graph (could be Genre, Artist, or Song)."""
    def __init__(self, judul=None, artist=None, link=None, genre=None):
        """
        Initialize the Node with song details.
        :param judul: Title of the song.
        :param artist: Artist of the song.
        :param link: A link to the song (could be a URL or other reference).
        :param genre: Genre of the song.
        """
        self.judul = judul
        self.artist = artist
        self.link = link
        self.genre = genre
        self.next = None

    def get_judul(self):
        return self.judul

    def get_artist(self):
        return self.artist

    def get_link(self):
        return self.link

    def get_genre(self):
        return self.genre

    def __repr__(self):
        # If the node represents a song, display its details
        if self.judul:
            return f"Node({self.judul}, {self.artist}, {self.genre})"
        # If it's a genre or artist node, display only the relevant details
        elif self.artist:
            return f"Node(Artist: {self.artist})"
        elif self.genre:
            return f"Node(Genre: {self.genre})"
        else:
            return "Node(Empty)"


class Graph:
    """A class representing a Graph with genres, artists, and songs."""
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = nx.Graph()
        self.nodes = {}  # Dictionary to hold nodes by name for easy access

    def add_node(self, node):
        """Add a node to the graph."""
        if node.judul and node.judul not in self.nodes:
            self.nodes[node.judul] = node
            self.graph.add_node(node.judul, type="song")
            print(f"Node '{node.judul}' of type 'song' added.")
        elif node.artist and node.artist not in self.nodes:
            self.nodes[node.artist] = node
            self.graph.add_node(node.artist, type="artist")
            print(f"Node 'Artist: {node.artist}' added.")
        elif node.genre and node.genre not in self.nodes:
            self.nodes[node.genre] = node
            self.graph.add_node(node.genre, type="genre")
            print(f"Node 'Genre: {node.genre}' added.")
        else:
            print(f"Node '{node.judul if node.judul else node.artist}' already exists.")

    def add_edge(self, node1, node2, relation):
        """Add an edge between two nodes in the graph with a relation."""
        
        # Check if node1 exists in the graph
        node1_id = node1.judul if node1.judul else node1.artist if node1.artist else node1.genre
        if node1_id not in self.nodes:
            print(f"Node '{node1}' does not exist in the graph.")
            return

        # Check if node2 exists in the graph
        node2_id = node2.judul if node2.judul else node2.artist if node2.artist else node2.genre
        if node2_id not in self.nodes:
            print(f"Node '{node2}' does not exist in the graph.")
            return

        # Add the edge with the appropriate relation
        self.graph.add_edge(node1_id, node2_id, relation=relation)
        print(f"Edge between '{node1_id}' and '{node2_id}' with relation '{relation}' added.")



    def display_graph(self):
        """Visualize the graph using matplotlib and networkx."""
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
        edge_labels = nx.get_edge_attributes(self.graph, 'relation')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title('Music Graph Visualization')
        plt.show()

    def recommend_songs(self, song_judul):
        """
        Recommends 5 songs based on the given song's artist and genre.
        """
        if song_judul not in self.nodes:
            print(f"Song '{song_judul}' not found in the graph.")
            return
        
        # Retrieve the song node and its related genre and artist
        song = self.nodes[song_judul]
        artist = None
        genre = None
        
        # Find the artist and genre of the given song
        for neighbor in self.graph.neighbors(song_judul):
            if self.graph[song_judul][neighbor]["relation"] == "by":
                artist = self.nodes[neighbor]
            elif self.graph[song_judul][neighbor]["relation"] == "in":
                genre = self.nodes[neighbor]
        
        if not artist or not genre:
            print(f"Couldn't find artist or genre for song '{song_judul}'.")
            return
        
        # Helper function to get songs by the same artist and genre
        def find_songs_by_artist_and_genre(artist, genre):
            return [
                n for n in self.graph.neighbors(genre.judul)
                if self.graph[genre.judul][n]["relation"] == "in" and
                any(self.graph[n][a]["relation"] == "by" for a in self.graph.neighbors(n))
                and self.nodes[n].get_genre() == genre.get_genre() and n != song_judul
            ]
        
        # Helper function to get songs by the same genre but different artists
        def find_songs_by_genre_diff_artists(genre):
            return [
                n for n in self.graph.neighbors(genre.judul)
                if self.graph[genre.judul][n]["relation"] == "in" and
                self.nodes[n].get_genre() == genre.get_genre() and n != song_judul
            ]
        
        # Helper function to get songs by the same artist but different genre
        def find_songs_by_artist_diff_genre(artist):
            return [
                n for n in self.graph.neighbors(artist.judul)
                if self.graph[artist.judul][n]["relation"] == "by" and
                self.nodes[n].get_artist() == artist.get_artist() and n != song_judul
            ]
        
        # 1. Two songs from the same artist and the same genre
        same_artist_genre_songs = find_songs_by_artist_and_genre(artist, genre)
        
        # 2. Two songs from the same genre but different artists
        same_genre_diff_artists = find_songs_by_genre_diff_artists(genre)
        
        # 3. One song from the same artist but a different genre
        same_artist_diff_genre = find_songs_by_artist_diff_genre(artist)
        
        # Track already recommended songs to avoid overlap
        recommended_songs = set()

        # Prepare the recommendations list
        recommendations = []
        
        # Add 2 songs from the same artist and the same genre
        for song in random.sample(same_artist_genre_songs, 2) if len(same_artist_genre_songs) >= 2 else []:
            if song not in recommended_songs:
                recommendations.append(song)
                recommended_songs.add(song)

        # Add 2 songs from the same genre but different artists
        for song in random.sample(same_genre_diff_artists, 2) if len(same_genre_diff_artists) >= 2 else []:
            if song not in recommended_songs:
                recommendations.append(song)
                recommended_songs.add(song)
        
        # Add 1 song from the same artist but a different genre
        for song in random.sample(same_artist_diff_genre, 1) if len(same_artist_diff_genre) >= 1 else []:
            if song not in recommended_songs:
                recommendations.append(song)
                recommended_songs.add(song)
        
        # Output recommendations
        print(f"Recommendations based on '{song_judul}':")
        for rec in recommendations:
            print(f"- {rec}")



# Initialize the graph
music_graph = Graph()

# Add genres
genre_pop = Node(genre="Pop")
genre_rock = Node(genre="Rock")

# Add artists
artist_the_weeknd = Node(artist="The Weeknd")
artist_queen = Node(artist="Queen")

# Add songs
song_blinding_lights = Node(judul="Blinding Lights", artist="The Weeknd", link="https://link-to-blinding-lights", genre="Pop")
song_bohemian_rhapsody = Node(judul="Bohemian Rhapsody", artist="Queen", link="https://link-to-bohemian-rhapsody", genre="Rock")

# Add nodes to the graph
music_graph.add_node(genre_pop)
music_graph.add_node(genre_rock)
music_graph.add_node(artist_the_weeknd)
music_graph.add_node(artist_queen)
music_graph.add_node(song_blinding_lights)
music_graph.add_node(song_bohemian_rhapsody)

music_graph.add_edge(song_blinding_lights, song_bohemian_rhapsody, "same genre")

music_graph.display_graph()
# Recommend songs based on 'Blinding Lights'
music_graph.recommend_songs("Blinding Lights")
