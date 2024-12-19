class Node:
    def __init__(self, judul, artist, link, genre):
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


# Create a new node
# song_node = Node("Song Title", "Artist Name", "https://link.com", "Pop")

# Get specific attributes
# print(song_node.get_judul())  # Returns: 'Song Title'
# print(song_node.get_artist())  # Returns: 'Artist Name'
# print(song_node.get_link())  # Returns: 'https://link.com'
# print(song_node.get_genre())  # Returns: 'Pop'
