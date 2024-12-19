from node import Node

class MusicQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def push(self, node):
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        print(f"'{node.get_judul()}' by {node.get_artist()} has been added to the Queue!")

    def pop(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None

        val = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"'{val.get_judul()}' by {val.get_artist()} has been removed from the Queue!")
        return val

    def addToFront(self, node):
        if self.isEmpty():
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front = node
        print(f"'{node.get_judul()}' by {node.get_artist()} has been added to the front of the Queue!")

    def display_queue(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Music in Queue:")
            current = self.front
            index = 1
            while current:
                print(f"{index}. {current.get_judul()} ({current.get_genre()}) by {current.get_artist()}")
                current = current.next
                index += 1

# Contoh Penggunaan Queue
# music1 = Node("Die With A Smile", "Lady Gaga and Bruno Mars", "https://music.youtube.com/watch?v=RVDCeVG90Rg&si=gtn46KrEXj01Da6O", "Pop")
# music2 = Node("APT", "ROSÉ and Bruno Mars", "https://music.youtube.com/watch?v=58-AKkNMZNQ&si=pRT9xgwATww9wfE_", "Pop")
# music3 = Node("TOUCH", "KATSEYE", "https://music.youtube.com/watch?v=H5tO_9wZ0hg&si=vgK3xNs7qQv2WWgg", "K-Pop")
# music4 = Node("Sunflower", "Post Malone and Swae Lee", "https://music.youtube.com/watch?v=r7Rn4ryE_w8&si=irp2dsjusjfBzqEn", "Hip-Hop")

# playlist = MusicQueue()

# playlist.push(music1)
# playlist.push(music2)
# playlist.push(music3)

# playlist.display_queue()

# playlist.addToFront(music4)

# playlist.display_queue()

# playlist.pop()

# playlist.display_queue()