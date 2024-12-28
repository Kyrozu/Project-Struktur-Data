from syncQueueStack import SyncQueueStack
from new_graph_algorithm import Graph

# Nathanael / C14230178 (membatu connect semua class dengan class menu)
# Mario / C14230194 (pembuat class menu)
class MusicApp:
    def __init__(self):
        self.musicGraph = Graph()         # Initialize the music graph
        self.playlist = SyncQueueStack()  # Initialize the playlist

    # Mario / C14230194
    def searchbar_music(self):
        search = input(" ❓ Masukkan judul / penyanyi / atau genre musik: ").lower()
        results = [] 

        # Cari di graph
        for key, node in self.musicGraph.nodes.items():
            if (search in node.judul.lower() or 
                search in node.artist.lower() or 
                search in node.genre.lower()):
                results.append((key, node))

        # Tampilkan hasil
        if results:
            while True:
                print("\n 🔍  Hasil pencarian  🔍")
                nomor = 1
                for _, song in results:     # tdk pakai key krn hanya perlu liat node
                    print(f"{nomor}. {song.judul} - by {song.artist} ({song.genre})")
                    nomor += 1
            
                # Pilih musik untuk ditambahkan ke playlist
                choice = input("\n ❓ Pilih nomor musik untuk ditambahkan ke playlist (0 untuk close): ")
                if choice == "0":
                    print("\n ❌ Batal menambahkan musik ke playlist ❌")
                    break
                elif choice.isdigit() and 1 <= int(choice) <= len(results):
                    selected_song = results[int(choice) - 1][1] 
                    self.playlist.addMusicToPlaylist(selected_song.judul, selected_song.artist, selected_song.link, selected_song.genre)
                    # print(f"\n'{selected_song.judul}' telah ditambahkan ke playlist.")
                else:
                    print("\n❗ Pilihan tidak valid❗")
        else:
            print("\n 🚫 Musik tidak ditemukan 🚫")

    # Mario / C14230194
    # (JANGAN DI HAPUS) Function search awal pakai BFS (tdk digunakan krn ada node yg bisa sendirian)
    # def searchbar_music(self):
    #     search = input("Masukkan judul / penyanyi / atau genre musik: ").lower()
    #     results = []

    #     # BFS dimulai dari node pertama (head)
    #     if not self.musicGraph.nodes:
    #         print("\nGraph kosong. Tidak ada musik untuk dicari.")
    #         return

    #     visited = set()  # Untuk melacak node yang sudah dikunjungi
    #     queue = []       # Queue untuk BFS

    #     # Ambil node pertama dari graph (sebagai head)
    #     head = list(self.musicGraph.nodes.keys())[0]
    #     queue.append(head)

    #     while queue:
    #         current_key = queue.pop(0)
    #         if current_key in visited:
    #             continue
    #         visited.add(current_key)

    #         # Akses node dari nodes
    #         current_node = self.musicGraph.nodes.get(current_key)
    #         if not current_node:
    #             continue

    #         # Cek apakah node sesuai dengan query pencarian
    #         if (search in current_node.judul.lower() or
    #             search in current_node.artist.lower() or
    #             search in current_node.genre.lower()):
    #             results.append((current_key, current_node))

    #         # Tambahkan semua tetangga ke queue (pakai neighbors bawaan networkx)
    #         for neighbor in self.musicGraph.graph.neighbors(current_key):
    #             if neighbor not in visited:
    #                 queue.append(neighbor)

    #     # Tampilkan hasil
    #     if results:
    #         while True:
    #             print("\nHasil pencarian:")

    #             # tdk pakai key krn hanya perlu liat node
    #             for num, (_, song) in enumerate(results, start=1):                     
    #                 print(f"{num}. {song.judul} - by {song.artist} ({song.genre})")

    #             # Pilih musik untuk ditambahkan ke playlist
    #             choice = input("\nPilih nomor musik untuk ditambahkan ke playlist (0 untuk close): ")
    #             if choice == "0":
    #                 print("\nBatal menambahkan musik ke playlist.")
    #                 break
    #             elif choice.isdigit() and 1 <= int(choice) <= len(results):
    #                 selected_song = results[int(choice) - 1][1]  # Ambil node
    #                 self.playlist.addMusicToPlaylist(
    #                     selected_song.judul,
    #                     selected_song.artist,
    #                     selected_song.link,
    #                     selected_song.genre
    #                 )
    #                 print(f"\n'{selected_song.judul}' telah ditambahkan ke playlist.")
    #             else:
    #                 print("\nPilihan tidak valid.")
    #     else:
    #         print("\nMusik tidak ditemukan.")


    def add_music_to_graph(self):
        title = input(" 🏷️   Masukkan judul musik: ")
        artist = input(" 🎤  Masukkan nama penyanyi: ")
        genre = input(" 🎧  Masukkan genre musik: ")
        link = input(" 🔗  Masukkan link musik: ")
        self.musicGraph.add_node(title,artist,link,genre)
        print(f" ✅ '{title}' by {artist} added to the graph.")

    def play_music_from_queue(self):
        self.playlist.play_music()
    
    def getRecommendation(self):
        # get musik yg sedang di putar
        current_song = self.playlist.get_stack().head.get_judul()

        # get rekomendasi berdasarkan musik yg sedang di putar
        results = self.musicGraph.recommend_songs(current_song)
        
        if results:

            while True:
                print("\n 🎧  Hasil Rekomendasi  🎧")
                nomor = 1
                for song in results:
                        print(f"{nomor}. {song.judul} - by {song.artist} ({song.genre})")
                        nomor += 1
                    
                # Pilih musik untuk ditambahkan ke playlist
                choice = input("\n ❓ Pilih nomor musik untuk ditambahkan ke playlist (0 untuk close): ")
                if choice == "0":
                    print("\n ❌ Batal menambahkan musik ke playlist ❌")
                    break
                elif choice.isdigit() and 1 <= int(choice) <= len(results):
                    selected_song = results[int(choice) - 1]
                    self.playlist.addMusicToPlaylist(selected_song.judul, selected_song.artist, selected_song.link, selected_song.genre)
                    # print(f"\n'{selected_song.judul}' telah ditambahkan ke playlist.")
                else:
                    print("\n❗Pilihan tidak valid ❗")

        else:
            print("\n 🚫 Rekomendasi Musik tidak ditemukan 🚫")

    # Mario / C14230194
    def show_menu(self):
        while True:
            print("\n---------------------------------")
            print("Menu:")
            print("1. Tambah musik baru ke grafik ➕")
            print("2. Cari musik 🔍")
            print("3. Rekomendasi musik 🎧")

            if self.playlist.player.isPlaying() == False:
                print("4. Mainkan musik dari antrean ▶️")
            else:
                print("4. Mainkan musik selanjutnya ⏭️")
                
            print("5. Mainkan musik sebelumnya ⏮️")
            print("6. Display graph musik 🖼️")
            print("0. Keluar ❌")
            print("---------------------------------")
            choice = input("❓ Pilih opsi: ")
            print("---------------------------------\n")

            if choice == "1":
                self.add_music_to_graph()

            elif choice == "2":
                self.searchbar_music()

            elif choice == "3":
                self.getRecommendation()

            elif choice == "4":
                if self.playlist.player.isPlaying() == False:
                    self.play_music_from_queue()
                else:
                    self.playlist.skipSong()

            elif choice == "5":
                self.playlist.prevSong()
            
            elif choice == "6":
                self.musicGraph.display_graph()

            elif choice == "0":
                print("\n Keluar dari aplikasi 👋 \n\n")
                raise SystemExit(0)

            else:
                print("❌ Opsi tidak valid. Silakan coba lagi.")

app = MusicApp()

# isi graph awal
app.musicGraph.add_node("Blinding Lights", "The Weeknd", "https://www.youtube.com/watch?v=fHI8X4OXluQ", "Pop")
app.musicGraph.add_node("Bohemian Rhapsody", "Queen", "https://www.youtube.com/watch?v=fJ9rUzIMcZQ", "Rock")
app.musicGraph.add_node("APT", "rose", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop")
app.musicGraph.add_node("Espresso", "Sabrina Carpenter", "https://www.youtube.com/watch?v=eVli-tstM5E", "Pop")
app.musicGraph.add_node("On The Ground", "rose", "https://www.youtube.com/watch?v=CKZvWhCqx1s", "kPop")
app.musicGraph.add_node('Amazing', 'GLITCH', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop')
app.musicGraph.add_node('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop')
app.musicGraph.add_node("Die With A Smile", "Lady Gaga and Bruno Mars", "https://www.youtube.com/watch?v=kPa7bsKwL-c", "Pop")

# anggap sudah ada playlist sebelumnya
app.playlist.addMusicToPlaylist('Amazing', 'GLITCH', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop')
app.playlist.addMusicToPlaylist('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop')
app.playlist.addMusicToPlaylist("Die With A Smile", "Lady Gaga and Bruno Mars", "https://www.youtube.com/watch?v=kPa7bsKwL-c", "Pop")
app.playlist.addMusicToHistory("APT", "ROSÉ and Bruno Mars", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop")

app.show_menu()