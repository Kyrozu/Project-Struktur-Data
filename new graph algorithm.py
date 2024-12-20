import random
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    """A class representing a node in the graph (could be Genre, Artist, or Song)."""
    def __init__(self, name, node_type):
        """
        Initialize the Node.
        :param name: Name of the node (e.g., genre, artist, or song name).
        :param node_type: Type of node ('genre', 'artist', 'song').
        """
        self.name = name
        self.node_type = node_type

    def __repr__(self):
        return f"Node({self.name}, {self.node_type})"


class Graph:
    """A class representing a Graph with genres, artists, and songs."""
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = nx.Graph()
        self.nodes = {}  # Dictionary to hold nodes by name for easy access

    def add_node(self, node):
        """Add a node to the graph."""
        if node.name not in self.nodes:
            self.nodes[node.name] = node
            self.graph.add_node(node.name, type=node.node_type)
            print(f"Node '{node.name}' of type '{node.node_type}' added.")
        else:
            print(f"Node '{node.name}' already exists.")

    def add_edge(self, node1, node2, relation):
        """Add an edge between two nodes in the graph with a relation."""
        self.graph.add_edge(node1.name, node2.name, relation=relation)
        print(f"Edge between '{node1.name}' and '{node2.name}' with relation '{relation}' added.")

    def display_graph(self):
        """Visualize the graph using matplotlib and networkx."""
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
        edge_labels = nx.get_edge_attributes(self.graph, 'relation')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title('Music Graph Visualization')
        plt.show()

# Example usage

# Create the Graph object
music_graph = Graph()



# Add some nodes (Genres, Artists, and Songs)
song_Master_of_Puppets = Node("Master of Puppets", "song")
song_Symphony_No_5 = Node("Symphony No. 5", "song")
song_Dynamite = Node("Dynamite", "song")
song_Strategy = Node("Strategy", "song")
song_TT = Node("TT", "song")
song_Lovesick_Girls = Node("Lovesick Girls", "song")
song_Whiplash = Node("Whiplash", "song")
song_Last_Festival = Node("Last Festival", "song")
song_Why_Why = Node("Why Why", "song")
song_Gurenge = Node("Gurenge", "song")
song_Candy_Pop = Node("Candy Pop", "song")
genre_pop = Node("Pop", "genre")
genre_rock = Node("Rock", "genre")
artist_the_weeknd = Node("The Weeknd", "artist")
artist_queen = Node("Queen", "artist")
song_blinding_lights = Node("Blinding Lights", "song")
song_bohemian_rhapsody = Node("Bohemian Rhapsody", "song")
genre_jazz = Node("Jazz", "genre")
genre_hiphop = Node("Hiphop", "genre")
genre_country = Node("Country", "genre")
genre_heavy_metal = Node("Heavy metal", "genre")
genre_classical = Node("classical", "genre")
genre_punk = Node("Punk", "genre")
genre_soundtrack = Node("soundtrack", "genre")
genre_kpop = Node("Kpop", "genre")
genre_jpop = Node("Jpop", "genre")
artist_Dave_Brubeck_Quartet = Node("Dave Brubeck Quartet", "artist")
artist_Travis_Scott = Node("Travis Scott", "artist")
artist_Dolly_Parton = Node("Dolly Parton", "artist")
artist_Metallica = Node("Metallica", "artist")
artist_Ludwig_van_Beethoven = Node("Ludwig van Beethoven", "artist")
artist_BTS = Node("BTS", "artist")
artist_Twice = Node("Twice", "artist")
artist_Aespa = Node("Aespa", "artist")
artist_TWS = Node("TWS", "artist")
artist_Shannon = Node("Shannon", "artist")
artist_LiSA = Node("LiSA", "artist")
artist_Blackpink = Node("Blackpink", "artist")
song_Light_Switch = Node("Light Switch", "song")
artist_Charlie_Puth = Node("Charlie Puth", "artist")
song_Espresso = Node("Espresso", "song")
artist_Sabrina_Carpenter = Node("Sabrina Carpenter", "artist")
song_Yellow = Node("Yellow", "song")
artist_Coldplay = Node("Coldplay", "artist")
song_Take_Five = Node("Take Five", "song")
song_Sicko_Mode = Node("Sicko Mode", "song")
song_Jolene = Node("Jolene", "song")



music_graph.add_node(genre_pop)
music_graph.add_node(genre_rock)
music_graph.add_node(artist_the_weeknd)
music_graph.add_node(artist_queen)
music_graph.add_node(song_blinding_lights)
music_graph.add_node(song_bohemian_rhapsody)
music_graph.add_node(song_Master_of_Puppets)
music_graph.add_node(song_Symphony_No_5)
music_graph.add_node(song_Dynamite)
music_graph.add_node(song_Strategy)
music_graph.add_node(song_TT)
music_graph.add_node(song_Lovesick_Girls)
music_graph.add_node(song_Whiplash)
music_graph.add_node(song_Last_Festival)
music_graph.add_node(song_Why_Why)
music_graph.add_node(song_Gurenge)
music_graph.add_node(song_Candy_Pop)
music_graph.add_node(genre_jazz)
music_graph.add_node(genre_hiphop)
music_graph.add_node(genre_country)
music_graph.add_node(genre_heavy_metal)
music_graph.add_node(genre_classical)
music_graph.add_node(genre_punk)
music_graph.add_node(genre_soundtrack)
music_graph.add_node(genre_kpop)
music_graph.add_node(genre_jpop)
music_graph.add_node(artist_Dave_Brubeck_Quartet)
music_graph.add_node(artist_Travis_Scott)
music_graph.add_node(artist_Dolly_Parton)
music_graph.add_node(artist_Metallica)
music_graph.add_node(artist_Ludwig_van_Beethoven)
music_graph.add_node(artist_BTS)
music_graph.add_node(artist_Twice)
music_graph.add_node(artist_Aespa)
music_graph.add_node(artist_TWS)
music_graph.add_node(artist_Shannon)
music_graph.add_node(artist_LiSA)
music_graph.add_node(artist_Blackpink)
music_graph.add_node(song_Light_Switch)
music_graph.add_node(artist_Charlie_Puth)
music_graph.add_node(song_Espresso)
music_graph.add_node(artist_Sabrina_Carpenter)
music_graph.add_node(song_Yellow)
music_graph.add_node(artist_Coldplay)
music_graph.add_node(song_Take_Five)
music_graph.add_node(song_Sicko_Mode)
music_graph.add_node(song_Jolene)








# Create edges (relationships between nodes)
music_graph.add_edge(song_blinding_lights, genre_pop, "in")
music_graph.add_edge(song_blinding_lights, artist_the_weeknd, "by")
music_graph.add_edge(song_bohemian_rhapsody, genre_rock, "in")
music_graph.add_edge(song_bohemian_rhapsody, artist_queen, "by")
music_graph.add_edge(song_Light_Switch, genre_pop, "in")
music_graph.add_edge(song_Light_Switch, artist_Charlie_Puth, "by")
music_graph.add_edge(song_Take_Five, genre_jazz, "in")
music_graph.add_edge(song_Take_Five, artist_Dave_Brubeck_Quartet, "by")
music_graph.add_edge(song_bohemian_rhapsody, genre_rock, "in")
music_graph.add_edge(song_bohemian_rhapsody, artist_queen, "by")
music_graph.add_edge(song_Espresso, genre_pop, "in")
music_graph.add_edge(song_Espresso, artist_Sabrina_Carpenter, "by")
music_graph.add_edge(song_Yellow, genre_pop, "in")
music_graph.add_edge(song_Yellow, artist_Coldplay, "by")
music_graph.add_edge(song_Sicko_Mode, genre_hiphop, "in")
music_graph.add_edge(song_Sicko_Mode, artist_Travis_Scott, "by")
music_graph.add_edge(song_Jolene, genre_country, "in")
music_graph.add_edge(song_Jolene, artist_Dolly_Parton, "by")
music_graph.add_edge(song_Master_of_Puppets, genre_heavy_metal, "in")
music_graph.add_edge(song_Master_of_Puppets, artist_Metallica, "by")
music_graph.add_edge(song_Symphony_No_5, genre_classical, "in")
music_graph.add_edge(song_Symphony_No_5, artist_Ludwig_van_Beethoven, "by")
music_graph.add_edge(song_Dynamite, genre_kpop, "in")
music_graph.add_edge(song_Dynamite, artist_BTS, "by")
music_graph.add_edge(song_Strategy, genre_kpop, "in")
music_graph.add_edge(song_Strategy, artist_Twice, "by")
music_graph.add_edge(song_TT, genre_kpop, "in")
music_graph.add_edge(song_TT, artist_Twice, "by")
music_graph.add_edge(song_Lovesick_Girls, genre_kpop, "in")
music_graph.add_edge(song_Lovesick_Girls, artist_Blackpink, "by")
music_graph.add_edge(song_Last_Festival, genre_kpop, "in")
music_graph.add_edge(song_Last_Festival, artist_TWS, "by")
music_graph.add_edge(song_Whiplash, genre_kpop, "in")
music_graph.add_edge(song_Whiplash, artist_Aespa, "by")
music_graph.add_edge(song_Why_Why, genre_kpop, "in")
music_graph.add_edge(song_Why_Why, artist_Shannon, "by")
music_graph.add_edge(song_Gurenge, genre_jpop, "in")
music_graph.add_edge(song_Gurenge, artist_LiSA, "by")
music_graph.add_edge(song_Candy_Pop, genre_jpop, "in")
music_graph.add_edge(song_Candy_Pop, artist_Twice, "by")

# music_graph.add_song("kpop", "Whiplash", "Aespa")
# music_graph.add_song("kpop", "Last Festival", "TWS")
# music_graph.add_song("kpop", "Why Why", "Shannon")
# music_graph.add_song("jpop", "Gurenge", "LiSA")
# music_graph.add_song("jpop", "Candy Pop", "Twice")

# Display the graph
music_graph.display_graph()

# Recommend songs based on "Blinding Lights"
# music_graph.recommend_songs("Blinding Lights")