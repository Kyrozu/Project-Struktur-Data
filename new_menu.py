from syncQueueStack import SyncQueueStack
from graph_algorithm import MusicGraph  # Assuming this is the file with the MusicGraph class

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
                # TODO: perlu dicek sama kenneth + mario
                song = results[choice - 1].get_judul()
                artist = results[choice - 1].get_artist()
                link = results[choice - 1].get_link()
                genre = results[choice - 1].get_genre()
                self.playlist.addMusicToPlaylist(song, artist, link, genre)
            else:
                print("Pilihan tidak valid.")
        else:
            print("Musik tidak ditemukan.")

    def add_music_to_graph(self):
        # TODO: perlu dicek sama kenneth
        title = input("Masukkan judul musik: ")
        artist = input("Masukkan nama penyanyi: ")
        genre = input("Masukkan genre musik: ")
        link = input("Masukkan link musik: ")
        self.music_graph.add_song(genre, title, artist)
        print(f"'{title}' by {artist} added to the graph under genre '{genre}'.")

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
            print("0. Keluar")

            choice = input("Pilih opsi: ")

            if choice == "1":
                # TODO: not tested
                self.add_music_to_graph()

            elif choice == "2":
                # TODO: not tested
                self.searchbar_music()

            elif choice == "3":
                print("Rekomendasi musik: ")
                # TODO: insert function display pilihan recomendasi

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
            

            elif choice == "0":
                print("\n\nKeluar dari aplikasi.")
                raise SystemExit(0)

            else:
                print("Opsi tidak valid. Silakan coba lagi.")

app = MusicApp()

app.playlist.addMusicToPlaylist('Amazing', 'Amazing', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop')
app.playlist.addMusicToPlaylist('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop')
app.playlist.addMusicToPlaylist("Die With A Smile", "Lady Gaga and Bruno Mars", "https://www.youtube.com/watch?v=kPa7bsKwL-c", "Pop")
app.playlist.addMusicToHistory("APT", "ROSÉ and Bruno Mars", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop")

app.show_menu()