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

        if node.judul and node.judul in self.nodes:
            print(f"Node Music '{node.judul}' already exists.")
            return

        if node.judul and node.judul not in self.nodes:
            self.nodes[node.judul] = node
            self.graph.add_node(node.judul, type="song")
            # print(f"Node '{node.judul}' of type 'song' added.")
            self._add_edges_for_new_node(node)  # Add edges based on same artist or genre
        elif node.artist and node.artist not in self.nodes:
            self.nodes[node.artist] = node
            self.graph.add_node(node.artist, type="artist")
            # print(f"Node 'Artist: {node.artist}' added.")
            self._add_edges_for_new_node(node)  # Add edges based on same artist or genre
        elif node.genre and node.genre not in self.nodes:
            self.nodes[node.genre] = node
            self.graph.add_node(node.genre, type="genre")
            # print(f"Node 'Genre: {node.genre}' added.")
            self._add_edges_for_new_node(node)  # Add edges based on same artist or genre
        

    # Helper function to add edges based on same artist or genre
    def _add_edges_for_new_node(self, node):
        # If the node has an artist, add edges with songs by the same artist
        if node.artist:
            for existing_node in self.nodes.values():
                if existing_node != node and existing_node.artist.lower() == node.artist.lower():
                    self.add_edge(existing_node, node, "same artist")
        
        # If the node has a genre, add edges with songs in the same genre
        if node.genre:
            for existing_node in self.nodes.values():
                if existing_node != node and existing_node.genre.lower() == node.genre.lower():
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
        # print(f"Edge between '{node1_id}' and '{node2_id}' with relation '{relation}' added.")

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
            return []
        
        song = self.nodes[song_judul]
        artist = song.artist
        genre = song.genre

        if not artist or not genre:
            print(f"Song '{song_judul}' does not have valid artist or genre information.")
            return []

        # BFS initialization
        visited = set()
        queue = [song_judul]
        recommendations = []
        recommended_songs = set()

        while queue and len(recommendations) < 5:
            current = queue.pop(0)
            visited.add(current)

            for neighbor in self.graph.neighbors(current):
                if neighbor not in visited:
                    relation = self.graph[current][neighbor]["relation"]
                    node = self.nodes[neighbor]

                    if relation == "same artist" and node.genre == genre and len(recommendations) < 2:
                        if neighbor not in recommended_songs:
                            recommendations.append(node)
                            recommended_songs.add(neighbor)
                    
                    elif relation == "same genre" and node.artist != artist and len(recommendations) < 4:
                        if neighbor not in recommended_songs:
                            recommendations.append(node)
                            recommended_songs.add(neighbor)
                    
                    elif relation == "same artist" and node.genre != genre and len(recommendations) < 5:
                        if neighbor not in recommended_songs:
                            recommendations.append(node)
                            recommended_songs.add(neighbor)
                    
                    queue.append(neighbor)

        return recommendations






music_graph = Graph()

# Add songs nodes
music_graph.add_node("Blinding Lights", "The Weeknd", "https://www.youtube.com/watch?v=fHI8X4OXluQ", "Pop")
music_graph.add_node("Bohemian Rhapsody", "Queen", "https://www.youtube.com/watch?v=fJ9rUzIMcZQ", "Rock")
music_graph.add_node("APT", "rose", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop")
music_graph.add_node("Espresso", "Sabrina Carpenter", "https://www.youtube.com/watch?v=eVli-tstM5E", "Pop")
music_graph.add_node("On The Ground", "rose", "https://www.youtube.com/watch?v=CKZvWhCqx1s", "kPop")


rec = music_graph.recommend_songs("Blinding Lights")

if rec:
    print("Recommended Songs:")
    for idx, song in enumerate(rec, start=1):
        print(f"{idx}. Title: {song.judul}, Artist: {song.artist}, Genre: {song.genre}, Link: {song.link}")
else:
    print("No recommendations found.")


music_graph.display_graph()


