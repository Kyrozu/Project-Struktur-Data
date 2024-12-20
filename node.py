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