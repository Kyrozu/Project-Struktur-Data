#code menu mario
class MusicApp:
    def __init__(self):
        self.graph = []  # Grafik musik (daftar musik)
        self.queue = []  # Antrean musik

    def search_music(self, query):
        """
        Fungsi untuk mencari musik berdasarkan query.
        
        Parameter:
        query (str): Kata kunci pencarian musik.

        Return:
        list: Daftar hasil pencarian musik.
        """
        # Simulasi hasil pencarian musik (bisa diintegrasikan dengan API)
        available_music = ["Song A", "Song B", "Song C", "Song D"]
        results = [song for song in available_music if query.lower() in song.lower()]
        return results

    def add_new_music_to_graph(self, music):
        """Menambahkan musik baru ke grafik."""
        if music not in self.graph:
            self.graph.append(music)
            print(f"'{music}' berhasil ditambahkan ke grafik.")
        else:
            print(f"'{music}' sudah ada di grafik.")

    def add_music_to_queue(self, music):
        """Menambahkan musik ke antrean."""
        self.queue.append(music)
        print(f"'{music}' berhasil ditambahkan ke antrean.")

    def play_music_from_queue(self):
        """Memainkan musik pertama dalam antrean."""
        if self.queue:
            playing = self.queue.pop(0)
            print(f"Sedang memainkan: {playing}")
        else:
            print("Antrean kosong. Tidak ada musik yang bisa dimainkan.")

    def show_menu(self):
        """Menampilkan menu untuk pengguna."""
        while True:
            print("\nMenu:")
            print("1. Tambah musik baru ke grafik")
            print("2. Masukkan pilihan rekomendasi musik")
            print("3. Tambah musik menggunakan pencarian ke antrean")
            print("4. Mainkan musik dari antrean")
            print("5. Keluar")

            choice = input("Pilih opsi: ")

            if choice == "1":
                music = input("Masukkan nama musik baru: ")
                self.add_new_music_to_graph(music)

            elif choice == "2":
                print("Rekomendasi musik: Song X, Song Y, Song Z")
                music = input("Pilih musik dari rekomendasi: ")
                self.add_music_to_queue(music)

            elif choice == "3":
                query = input("Masukkan kata kunci pencarian musik: ")
                results = self.search_music(query)
                if results:
                    print("Hasil pencarian:")
                    for i, song in enumerate(results, start=1):
                        print(f"{i}. {song}")
                    
                    choice = int(input("Pilih nomor musik untuk ditambahkan ke antrean: "))
                    if 1 <= choice <= len(results):
                        self.add_music_to_queue(results[choice - 1])
                    else:
                        print("Pilihan tidak valid.")
                else:
                    print("Tidak ada hasil yang ditemukan.")

            elif choice == "4":
                self.play_music_from_queue()

            elif choice == "5":
                print("Keluar dari aplikasi.")
                break

            else:
                print("Opsi tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    app = MusicApp()
    app.show_menu()
