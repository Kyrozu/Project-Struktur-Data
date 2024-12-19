class MusicApp:
    def __init__(self):
        self.graph = []  # Grafik musik (daftar musik)
        self.queue = []  # Antrean musik

    def search_music(self, start, target):
        """
        Fungsi untuk mencari musik menggunakan metode graph traversal.

        Parameter:
        start (str): Musik awal untuk memulai pencarian.
        target (str): Musik yang dicari.

        Return:
        list: Jalur menuju musik yang dicari, atau pesan jika tidak ditemukan.
        """
        from collections import deque

        if start not in self.graph:
            print(f"Musik '{start}' tidak ditemukan dalam grafik.")
            return []

        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current, path = queue.popleft()

            if current == target:
                print(f"Musik '{target}' ditemukan dengan jalur: {' -> '.join(path)}")
                return path

            visited.add(current)

            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        print(f"Musik '{target}' tidak ditemukan dalam grafik.")
        return []

    # def add_new_music_to_graph(self, music):
    #     """Menambahkan musik baru ke grafik."""
    #     if music not in self.graph:
    #         self.graph.append(music)
    #         print(f"'{music}' berhasil ditambahkan ke grafik.")
    #     else:
    #         print(f"'{music}' sudah ada di grafik.")

    # def add_music_to_queue(self, music):
    #     """Menambahkan musik ke antrean."""
    #     self.queue.append(music)
    #     print(f"'{music}' berhasil ditambahkan ke antrean.")

    # def play_music_from_queue(self):
    #     """Memainkan musik pertama dalam antrean."""
    #     if self.queue:
    #         playing = self.queue.pop(0)
    #         print(f"Sedang memainkan: {playing}")
    #     else:
    #         print("Antrean kosong. Tidak ada musik yang bisa dimainkan.")

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
                # Punya Kenneth

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
                        # self.add_music_to_queue(results[choice - 1]) Punya Joice
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
