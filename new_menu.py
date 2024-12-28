from syncQueueStack import SyncQueueStack
# from graph_algorithm import MusicGraph 
from new_graph_algorithm import Graph

class MusicApp:
    def __init__(self):
        self.graph = Graph()        # Initialize the music graph
        self.playlist = SyncQueueStack()  # Initialize the playlist

    def searchbar_music(self):
        search = input("Masukkan judul / penyanyi / atau genre musik: ").lower()
        results = []

        # Cari di graph
        for node in self.graph.nodes.items():
            if (search in node.judul.lower() or 
                search in node.artist.lower() or 
                search in node.genre.lower()):
                results.append(node)

        # Tampilkan hasil
        if results:
            print("\nHasil pencarian:")
            nomor = 1
            for song in results:
                print(f"{nomor}. {song.judul} - {song.artist} ({song.genre})")
                nomor += 1

            # Pilih musik untuk ditambahkan ke playlist
            choice = input("Pilih nomor musik untuk ditambahkan ke antrean (0 untuk batal): ")
            if choice == "0":
                print("Batal menambahkan ke antrean.")
            elif choice.isdigit() and 1 <= int(choice) <= len(results):
                selected_song = results[int(choice) - 1]
                self.playlist.addMusicToPlaylist(
                    selected_song.judul, 
                    selected_song.artist, 
                    selected_song.link, 
                    selected_song.genre
                )
                print(f"'{selected_song.judul}' telah ditambahkan ke playlist.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Musik tidak ditemukan.")


    def add_music_to_graph(self):
        title = input("Masukkan judul musik: ")
        artist = input("Masukkan nama penyanyi: ")
        genre = input("Masukkan genre musik: ")
        link = input("Masukkan link musik: ")
        self.graph.add_node(title,artist,link,genre)
        print(f"'{title}' by {artist} added to the graph.")

    def play_music_from_queue(self):
        self.playlist.play_music()

    def show_menu(self):
        while True:
            print("\nMenu:")
            print("1. Tambah musik baru ke grafik")
            print("2. Cari musik")
            print("3. Masukkan pilihan rekomendasi musik ke Playlist")

            if self.playlist.player.isPlaying() == False:
                print("4. Mainkan musik dari antrean")
            else:
                print("4. Mainkan musik selanjutnya")
            
            print("5. Mainkan musik sebelumnya")
            print("6. Display graph musik")
            print("0. Keluar")

            choice = input("Pilih opsi: ")

            if choice == "1":
                self.add_music_to_graph()

            elif choice == "2":
                # TODO: not tested
                self.searchbar_music()

            elif choice == "3":
                print("Rekomendasi musik: ")
                # TODO: insert function display pilihan recomendasi
                result = []

                # pilihan = input("Press '0' to cancel or 'the index' to add into playlist: ")
                # if pilihan != 0:
                #     song = node.get_judul()
                #     artist = node.get_artist()
                #     link = node.get_link()
                #     genre = node.get_genre()
                #     self.playlist.addMusicToPlaylist(song, artist, link, genre)

            elif choice == "4":
                if self.playlist.player.isPlaying() == False:
                    self.play_music_from_queue()
                else:
                    self.playlist.skipSong()

            elif choice == "5":
                self.playlist.prevSong()
            
            elif choice == "6":
                self.graph.display_graph()

            elif choice == "0":
                print("\n\nKeluar dari aplikasi.")
                raise SystemExit(0)

            else:
                print("Opsi tidak valid. Silakan coba lagi.")

app = MusicApp()

# isi graph awal
app.graph.add_node('Amazing', 'Amazing', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop')
app.graph.add_node('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop')
app.graph.add_node("Die With A Smile", "Lady Gaga and Bruno Mars", "https://www.youtube.com/watch?v=kPa7bsKwL-c", "Pop")
app.graph.add_node("APT", "ROSÉ and Bruno Mars", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop")

# anggap sudah ada playlist sebelumnya
app.playlist.addMusicToPlaylist('Amazing', 'Amazing', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop')
app.playlist.addMusicToPlaylist('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop')
app.playlist.addMusicToPlaylist("Die With A Smile", "Lady Gaga and Bruno Mars", "https://www.youtube.com/watch?v=kPa7bsKwL-c", "Pop")
app.playlist.addMusicToHistory("APT", "ROSÉ and Bruno Mars", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop")

app.show_menu()