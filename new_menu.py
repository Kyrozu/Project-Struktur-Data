from syncQueueStack import SyncQueueStack
from graph_algorithm import MusicGraph  # Assuming this is the file with the MusicGraph class
from node import Node

class MusicApp:
    def __init__(self):
        self.music_graph = MusicGraph()  # Initialize the music graph
        self.playlist = SyncQueueStack()  # Initialize the playlist

    def searchbar_music(self):
        # Function to search music by title, artist, or album
        search = input("Masukkan judul musik, penyanyi, atau album musik: ")
        results = []
        for genre, songs in self.music_graph.graph["music"].items():
            for song in songs:
                if search.lower() in song.lower():
                    results.append(song)
                    print(f"Judul: {song}, Genre: {genre}")
        
        if results:
            choice = int(input("Pilih nomor musik untuk ditambahkan ke antrean: "))
            if 1 <= choice <= len(results):
                # Assuming we have a way to get the artist and link for the song
                # Here we just use a placeholder for the artist and link
                artist = "Unknown Artist"
                link = "https://example.com"  # Placeholder link
                self.playlist.get_queue().push(Node(results[choice - 1], artist, link, "Unknown Genre"))
            else:
                print("Pilihan tidak valid.")
        else:
            print("Musik tidak ditemukan.")

    def add_music_to_graph(self):
        title = input("Masukkan judul musik: ")
        artist = input("Masukkan nama penyanyi: ")
        genre = input("Masukkan genre musik: ")
        link = input("Masukkan link musik: ")
        self.music_graph.add_song(genre, title, artist)
        print(f"'{title}' by {artist} added to the graph under genre '{genre}'.")

    def play_music_from_queue(self):
        self.playlist.play_music()

    def play_prev_music(self):
        self.playlist.prev_music()

    def show_menu(self):
        """Display the menu for the user."""
        while True:
            print("\nMenu:")
            print("1. Tambah musik baru ke grafik")
            print("2. Cari musik")
            print("3. Masukkan pilihan rekomendasi musik ke Playlist")
            print("4. Mainkan musik dari antrean")
            print("5. Mainkan musik sebelumnya")
            print("6. Keluar")

            choice = input("Pilih opsi: ")

            if choice == "1":
                self.add_music_to_graph()

            elif choice == "2":
                self.searchbar_music()

            elif choice == "3":
                print("Rekomendasi musik: ")
                # Here you can implement a method to show recommendations
                # For now, we will just prompt the user to choose a song
                song = input("Masukkan judul musik untuk ditambahkan ke antrean: ")
                # Assuming we have a way to get the artist and link for the song
                artist = "Unknown Artist"
                link = "https://example.com"  # Placeholder link
                self.playlist.get_queue().push(Node(song, artist, link, "Unknown Genre"))

            elif choice == "4":
                self.play_music_from_queue()

            elif choice == "5":
                self.play_prev_music()

            elif choice == "6":
                print("Keluar dari aplikasi.")
                break

            else:
                print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    app = MusicApp()
    app.show_menu()