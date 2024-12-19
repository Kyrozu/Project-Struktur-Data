from audioTest import play_youtube_audio
from queuee import MusicQueue
from stack import stack
from node import *

class SyncQueueStack:
    def __init__(self, queue, stack):
        self.queue = queue
        self.stack = stack

    def get_queue(self):
        return self.queue

    def get_stack(self):
        return self.stack

    def play_music(self):
        if self.queue.isEmpty():
            print("No songs in the playlist.")
            return

        # Ambil lagu dari queue
        current_song = self.queue.pop()
        print(f"Playing: {current_song.get_judul()} by {current_song.get_artist()}")

        # Tambahkan ke stack
        self.stack.push(current_song)

        # Putar lagu (simulasi dengan audioTest)
        play_youtube_audio(current_song.get_link())

    def prev_music(self):
        if self.stack.is_empty():
            print("No previous song to go back to.")
            return

        # Ambil lagu terakhir dari stack
        curr_song = self.stack.pop()
        last_song = self.stack.pop()

        # Masukkan kembali ke awal playlist 
        self.queue.addToFront(last_song)

        print(f"Re-added {last_song.get_judul()} by {last_song.get_artist()} to the playlist as the next song.")


# Inisialisasi Queue dan Stack
queue = MusicQueue()
stack = stack()

# Sinkronisasi queue dan stack
playlist = SyncQueueStack(queue, stack)

# Tambahkan lagu ke playlist

queue.push(Node('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop'))
queue.push(Node('Digital Circus', 'Amazing', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop'))


# # Operasi
playlist.play_music()  # Putar lagu pertama
playlist.play_music()  # Putar lagu kedua
playlist.prev_music()  # Undo ke lagu sebelumnya
playlist.play_music()  # Putar lagu berikutnya

