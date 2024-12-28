import random
import matplotlib.pyplot as plt
import networkx as nx
from node import Node

class Graph:
    def __init__(self):
        self.graph = nx.Graph()
        self.nodes = {}

    # Add a node to the graph
    def add_node(self, judul, artist, link, genre):
        node = Node(judul, artist, link, genre)

        if node.judul and node.judul not in self.nodes:
            self.nodes[node.judul] = node
            self.graph.add_node(node.judul, type="song")
            print(f"Node '{node.judul}' of type 'song' added.")
            self._add_edges_for_new_node(node)  # Add edges based on same artist or genre
        elif node.artist and node.artist not in self.nodes:
            self.nodes[node.artist] = node
            self.graph.add_node(node.artist, type="artist")
            print(f"Node 'Artist: {node.artist}' added.")
            self._add_edges_for_new_node(node)  # Add edges based on same artist or genre
        elif node.genre and node.genre not in self.nodes:
            self.nodes[node.genre] = node
            self.graph.add_node(node.genre, type="genre")
            print(f"Node 'Genre: {node.genre}' added.")
            self._add_edges_for_new_node(node)  # Add edges based on same artist or genre
        else:
            print(f"Node '{node.judul if node.judul else node.artist}' already exists.")

    # Helper function to add edges based on same artist or genre
    def _add_edges_for_new_node(self, node):
        # If the node has an artist, add edges with songs by the same artist
        if node.artist:
            for existing_node in self.nodes.values():
                if existing_node != node and existing_node.artist == node.artist:
                    self.add_edge(existing_node, node, "same artist")
        
        # If the node has a genre, add edges with songs in the same genre
        if node.genre:
            for existing_node in self.nodes.values():
                if existing_node != node and existing_node.genre == node.genre:
                    self.add_edge(existing_node, node, "same genre")

    # Add an edge between two nodes in the graph with a relation
    def add_edge(self, node1, node2, relation):
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

    # Visualize the graph using matplotlib and networkx
    def display_graph(self):
        
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
        edge_labels = nx.get_edge_attributes(self.graph, 'relation')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title('Music Graph Visualization')
        plt.show()

    # Recommends 5 songs based on the given song's artist and genre
    def recommend_songs(self, song_judul):
        if song_judul not in self.nodes:
            print(f"Song '{song_judul}' not found in the graph.")
            return
        
        # Retrieve the song node and its related artist and genre
        song = self.nodes[song_judul]
        artist = None
        genre = None
        
        # Find the artist and genre of the given song using 'same artist' and 'same genre' relations
        for neighbor in self.graph.neighbors(song_judul):
            if self.graph[song_judul][neighbor]["relation"] == "same artist":
                artist = self.nodes[neighbor]
            elif self.graph[song_judul][neighbor]["relation"] == "same genre":
                genre = self.nodes[neighbor]
        
        if not artist or not genre:
            print(f"Couldn't find artist or genre for song '{song_judul}'.")
            return
        
        # Helper function to get songs by the same artist and genre
        def find_songs_by_artist_and_genre(artist, genre):
            return [
                n for n in self.graph.neighbors(genre.judul)
                if self.graph[genre.judul][n]["relation"] == "same genre" and
                any(self.graph[n][a]["relation"] == "same artist" for a in self.graph.neighbors(n)) and
                self.nodes[n].genre == genre.genre and n != song_judul
            ]
        
        # Helper function to get songs by the same genre but different artists
        def find_songs_by_genre_diff_artists(genre):
            return [
                n for n in self.graph.neighbors(genre.judul)
                if self.graph[genre.judul][n]["relation"] == "same genre" and
                self.nodes[n].genre == genre.genre and n != song_judul
            ]
        
        # Helper function to get songs by the same artist but different genre
        def find_songs_by_artist_diff_genre(artist):
            return [
                n for n in self.graph.neighbors(artist.judul)
                if self.graph[artist.judul][n]["relation"] == "same artist" and
                self.nodes[n].artist == artist.artist and n != song_judul
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
        for song in random.sample(same_artist_genre_songs, 2) if len(same_artist_genre_songs) >= 2 else same_artist_genre_songs:
            if song not in recommended_songs:
                recommendations.append(song)
                recommended_songs.add(song)

        # Add 2 songs from the same genre but different artists
        for song in random.sample(same_genre_diff_artists, 2) if len(same_genre_diff_artists) >= 2 else same_genre_diff_artists:
            if song not in recommended_songs:
                recommendations.append(song)
                recommended_songs.add(song)
        
        # Add 1 song from the same artist but a different genre
        for song in random.sample(same_artist_diff_genre, 1) if len(same_artist_diff_genre) >= 1 else same_artist_diff_genre:
            if song not in recommended_songs:
                recommendations.append(song)
                recommended_songs.add(song)
        
        # Output recommendations
        print(f"Recommendations based on '{song_judul}':")
        for rec in recommendations:
            print(f"- {rec}")



# Initialize the graph
music_graph = Graph()

# Add songs nodes
music_graph.add_node("Blinding Lights", "The Weeknd", "https://www.youtube.com/watch?v=fHI8X4OXluQ", "Pop")
music_graph.add_node("Bohemian Rhapsody", "Queen", "https://www.youtube.com/watch?v=fJ9rUzIMcZQ", "Rock")
music_graph.add_node("APT", "rose", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop")
music_graph.add_node("Espresso", "Sabrina Carpenter", "https://www.youtube.com/watch?v=eVli-tstM5E", "Pop")
music_graph.add_node("On The Ground", "rose", "https://www.youtube.com/watch?v=CKZvWhCqx1s", "kPop")


# Recommend songs based on 'Blinding Lights'
music_graph.recommend_songs("Blinding Lights")

music_graph.display_graph()


