import random
import matplotlib.pyplot as plt
import networkx as nx
from node import Node

class Graph:
    def __init__(self):
        self.graph = nx.Graph()
        self.nodes = {}
        
    # Yovan / C14230068
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
        
    # Kenneth Leonard / C142300
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

    # Yovan / C14230068
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

    # Yovan / C14230068
    # Visualize the graph using matplotlib and networkx
    def display_graph(self):
        
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
        edge_labels = nx.get_edge_attributes(self.graph, 'relation')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title('Music Graph Visualization')
        plt.show()

    # Kenneth Leonard / C142300
    # Recommends 5 songs berdasarkan artist dan genre menggunakan BFS
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

        # (tidak perlu loop while karena hanya perlu return node yg terhubung dgn lagu)
        # while queue and len(recommendations) < 5:
        current = queue.pop(0)
        visited.add(current)

        for neighbor in self.graph.neighbors(current):
                if len(recommendations) >= 5:
                    break

                if neighbor not in visited:
                    relation = self.graph[current][neighbor]["relation"]
                    node = self.nodes[neighbor]

                    # utamakan opsi artist yg sama
                    if relation == "same artist" and node.genre == genre and len(recommendations) < 2:
                        if neighbor not in recommended_songs:
                            recommendations.append(node)
                            recommended_songs.add(neighbor)
                    
                    # utamakan opsi genre yg sama
                    elif relation == "same genre" and node.artist != artist and len(recommendations) < 4:
                        if neighbor not in recommended_songs:
                            recommendations.append(node)
                            recommended_songs.add(neighbor)

                    # jika memiliki sisa tempat di array
                    elif (relation == "same artist" and node.genre != genre) or (relation == "same genre" and node.artist != artist):
                        if neighbor not in recommended_songs:
                            recommendations.append(node)
                            recommended_songs.add(neighbor)
                    
                    # (berhubungan dgn while loop)
                    # queue.append(neighbor)

        return recommendations

# # Test
# music_graph = Graph()

# # Add songs nodes
# music_graph.add_node("Blinding Lights", "The Weeknd", "https://www.youtube.com/watch?v=fHI8X4OXluQ", "Pop")
# music_graph.add_node("Bohemian Rhapsody", "Queen", "https://www.youtube.com/watch?v=fJ9rUzIMcZQ", "Rock")
# music_graph.add_node("APT", "rose", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop")
# music_graph.add_node("Espresso", "Sabrina Carpenter", "https://www.youtube.com/watch?v=eVli-tstM5E", "Pop")
# music_graph.add_node("On The Ground", "rose", "https://www.youtube.com/watch?v=CKZvWhCqx1s", "kPop")
# music_graph.add_node('Amazing', 'GLITCH', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop')
# music_graph.add_node('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop')
# music_graph.add_node("Die With A Smile", "Lady Gaga and Bruno Mars", "https://www.youtube.com/watch?v=kPa7bsKwL-c", "Pop")

# music_graph.display_graph()


