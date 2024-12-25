from audioTest import play_youtube_audio
from queuee import MusicQueue
from stack import stack
from node import Node

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
            print("Playlist Ended")
            return

        self.displayQueueStack()

        # Ambil lagu dari queue
        current_song = self.queue.pop()

        # Tambahkan ke stack
        self.stack.push(current_song)

        # Putar lagu (dengan audioTest)
        play_youtube_audio(current_song.get_link(), self)

    def prev_music(self):
        if self.stack.is_empty():
            print("No previous song to go back to")
            return

        # Ambil lagu terakhir dari stack
        curr_song = self.stack.pop()

        # Jika ada lagu sebelumnya, kembalikan ke queue
        if not self.stack.is_empty():
            last_song = self.stack.pop()
            self.queue.addToFront(last_song)

        # lagu tadi ke stack (di tuker sama lagu sebelum) 
        self.stack.push(curr_song)

        # Putar musik
        self.play_music()

    def playAll(self):
        while not self.queue.isEmpty():
            self.play_music()

    def displayQueueStack(self):
        self.queue.display_queue()
        if not self.stack.is_empty():
            self.stack.print_stack()
        print()

    def control_input(self, player):
        control = input("Press 's' to skip song or 'p' to previous song: ")

        if control.lower() == 's':
            print("Music skipped")
            player.stop()
            self.play_music()

        if control.lower() == 'p' and not self.stack.is_empty():
            print("Previous Music")
            player.stop()
            self.prev_music()


# Test
# Inisialisasi Queue dan Stack
playlist = SyncQueueStack()

# Tambahkan lagu ke playlist
playlist.get_queue().push(Node('Amazing', 'Amazing', 'https://www.youtube.com/watch?v=NAZE98P6NvY&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=2', 'Pop'))
playlist.get_queue().push(Node('HISTORY', 'Whale Taylor', 'https://www.youtube.com/watch?v=ejC-4FBs4_w&list=PLl9rPoFrwA56scu3xTguJpbHpP8Sd2r1_&index=16', 'Pop'))
playlist.get_queue().push(Node("Die With A Smile", "Lady Gaga and Bruno Mars", "https://www.youtube.com/watch?v=kPa7bsKwL-c", "Pop"))
playlist.get_stack().push(Node("APT", "ROSÉ and Bruno Mars", "https://www.youtube.com/watch?v=ekr2nIex040", "Pop"))

playlist.playAll()
