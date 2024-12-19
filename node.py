class Node:
    def __init__(self, judul, artist, link, genre):
        self.judul = judul
        self.artist = artist
        self.link = link
        self.genre = genre
        self.next = None

    def get(self, attribute=None):
        # If no specific attribute is requested, return the entire node's data
        if attribute is None:
            return {
                'judul': self.judul,
                'artist': self.artist,
                'link': self.link,
                'genre': self.genre
            }
        # Otherwise, return the requested attribute
        elif attribute == 'judul':
            return self.judul
        elif attribute == 'artist':
            return self.artist
        elif attribute == 'link':
            return self.link
        elif attribute == 'genre':
            return self.genre
        else:
            print("Invalid attribute requested!")
            return None

# Create a new node
song_node = Node("Song Title", "Artist Name", "https://link.com", "Pop")

# Get all attributes
print(song_node.get())  # Returns all attributes as a dictionary

# Get a specific attribute
print(song_node.get('judul'))  # Returns: 'Song Title'
print(song_node.get('artist'))  # Returns: 'Artist Name'
