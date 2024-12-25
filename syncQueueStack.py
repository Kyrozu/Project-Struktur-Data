from audioTest import play_youtube_audio
from queuee import MusicQueue
from stack import stack
from node import Node

"""
pip install yt-dlp python-vlc
"""

class SyncQueueStack:
    def __init__(self):
        self.queue = MusicQueue()
        self.stack = stack()

    def get_queue(self):
        return self.queue

    def get_stack(self):
        return self.stack

    def play_music(self):
        if self.queue.isEmpty():
            print("No songs in the playlist.")
            return

        self.displayQueueStack()

        # Ambil lagu dari queue
        current_song = self.queue.pop()
        # print(f"Playing: {current_song.get_judul()} by {current_song.get_artist()}")

        # Putar lagu (simulasi dengan audioTest)
        play_youtube_audio(current_song.get_link())

        # Tambahkan ke stack TODO: some how kalo gk ada stack di awal bugged
        self.stack.push(current_song)

    def prev_music(self):
        if self.stack.is_empty():
            print("No previous song to go back to.")
            return

        # Ambil lagu terakhir dari stack
        curr_song = self.stack.pop()

        # Masukkan kembali ke awal playlist 
        self.queue.addToFront(curr_song)

        print(f"Re-added {curr_song.get_judul()} by {curr_song.get_artist()} to the playlist as the next song.")

    def displayQueueStack(self):
        self.queue.display_queue()
        index = self.queue.getIndex()
        if self.stack.is_empty() != True:
            self.stack.print_stack(index)
            
        self.queue.setIndex(1)
        

# Inisialisasi Queue dan Stack
playlist = SyncQueueStack()

# # Tambahkan lagu ke playlist
# playlist.get_queue().push(Node('Amazing', 'Amazing', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop'))
playlist.get_queue().push(Node('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop'))
playlist.get_queue().push(Node("Die With A Smile", "Lady Gaga and Bruno Mars", "https://www.youtube.com/watch?v=kPa7bsKwL-c", "Pop"))
playlist.get_stack().push(Node("APT", "ROSÉ and Bruno Mars", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop"))
# playlist.get_stack().push(Node('APT', 'ROSÉ and Bruno Mars', '', 'Pop'))



# # Operasi
# playlist.play_music() # Amazing
playlist.play_music() # HISTORY
playlist.play_music() # Die With A Smile

playlist.prev_music()  # Undo ke lagu sebelumnya
playlist.play_music()  # HISTORY
# playlist.displayQueueStack() 

