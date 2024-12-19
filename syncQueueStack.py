from audioTest import play_youtube_audio
# from queuee import MusicQueue
from stack import stack
from node import *

# untuk test sementara
class MusicQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.que = [None] * self.capacity
        self.front = 0
        self.rear = -1

    def isEmpty(self):
        return self.front == self.rear + 1
    
    def isFull(self):
        return self.rear == self.capacity - 1
    
    def push(self, node):
        if not self.isFull():
            self.que[self.rear + 1] = node
            self.rear += 1
            # print(f"'{node.get_artist()}' has been added to the Queue!")
        else:
            print("Queue is Full")

    def pop(self):
        if not self.isEmpty():
            val = self.que[self.front]
            self.que[self.front] = None
            self.front += 1
            # print(f"'{val.get_judul()}' has been removed from the Queue!")
            return val
        else:
            print("Queue is Empty")
            return None


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
        play_youtube_audio(current_song.get_link(),initial_volume=50)

    def prev_music(self):
        if self.stack.is_empty():
            print("No previous song to go back to.")
            return

        # Ambil lagu terakhir dari stack
        last_song = self.stack.pop()

        # Masukkan kembali ke awal playlist TODO: ganti function di file asli blm ada
        self.queue.push(last_song)

        print(f"Re-added {last_song.get_judul()} by {last_song.get_artist()} to the playlist as the next song.")


# Inisialisasi Queue dan Stack
queue = MusicQueue(capacity=5)
stack = stack()

# Sinkronisasi queue dan stack
playlist = SyncQueueStack(queue, stack)

# Tambahkan lagu ke playlist

stack.push(Node('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop'))
stack.push(Node('Digital Circus', 'Amazing', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop'))


# Operasi
# playlist.play_music()  # Putar lagu pertama
# playlist.play_music()  # Putar lagu kedua
playlist.prev_music()  # Undo ke lagu sebelumnya
playlist.play_music()  # Putar lagu berikutnya

