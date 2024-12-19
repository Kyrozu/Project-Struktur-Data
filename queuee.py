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

    def reset(self):
        self.front = 0
        self.rear = -1

    def push(self, data):
        if not self.isFull():
            self.que[self.rear + 1] = data
            self.rear += 1
            print(f"'{data['title']}' has been added to the Queue!")
        else:
            print("Queue is Full")

    def pop(self):
        if not self.isEmpty():
            val = self.que[self.front]
            self.que[self.front] = None
            self.front += 1
            print(f"'{val['title']}' has been removed from the Queue!")
            return val
        else:
            print("Queue is Empty")
            return None

    def peek(self):
        return self.que[self.front]

    def display_queue(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Music in Queue:")
            for indx, music in enumerate(self.que[self.front:self.rear + 1], start=1):
                if music:
                    print(f"{indx}. {music['title']} ({music['genre']}) by {music['singer']}")

# Contoh Penggunaan Queue
music1 = {'title': 'Shape of You', 'genre': 'Pop', 'singer': 'Ed Sheeran'}
music2 = {'title': 'Blinding Lights', 'genre': 'Synth-Pop', 'singer': 'The Weeknd'}
music3 = {'title': 'Your Name AMV', 'genre': 'Anime', 'singer': 'Radwimps'}

playlist = MusicQueue(capacity=5)

playlist.push(music1)
playlist.push(music2)
playlist.push(music3)

playlist.display_queue()

playlist.pop()

playlist.display_queue()