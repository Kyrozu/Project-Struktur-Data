"""
install libary pemutar lagu lewat link youtube
pip install yt-dlp python-vlc
"""

import vlc
import yt_dlp as youtube_dl
import time

class YouTubeAudioPlayer:
    def __init__(self, sync, initial_volume=50):
        self.sync = sync
        self.initial_volume = initial_volume
        self.player = None

    def play(self, youtube_url):
        # Setting untuk extract audio dari YouTube
        ydl_opts = {
            'format': 'bestaudio/best',  # Audio format
            'noplaylist': True,          # Tidak download playlists
            'quiet': True,               # Tidak output yang tidak perlu
            'no_warnings': True,         # Tidak ada warning
        }

        # Extract audio dari URL YouTube nya
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            audio_url = info.get('url', None)

            if audio_url:
                # Initialize VLC nya
                instance = vlc.Instance()
                self.player = instance.media_player_new()
                media = instance.media_new(audio_url)
                self.player.set_media(media)
                
                self.player.audio_set_volume(self.initial_volume)  # Setting volume
                self.player.play()

                # Loop untuk perubahan player state
                while not self.isPlaying():
                    time.sleep(0.5)         # Check setiap 0.5 detik

                # # untuk player yang berjalan bersamaan dengan menu tapi terpisah
                # while True:
                #     state = self.player.get_state()

                #     # TODO: harus di pindah
                #     self.sync.control_input()

                #     # Berhenti jika musik selesai atau error
                #     if state in [vlc.State.Ended, vlc.State.Error]:
                #         print("Music finished")
                #         break

                #     # Berhenti jika playlist habis
                #     if self.sync.get_queue().isEmpty():
                #         print("Playlist empty. Stopping playback.")
                #         break

    def stop(self):
        if self.player:
            self.player.stop()

    def isPlaying(self):
        if self.player != None:
            state = self.player.get_state()
            if state == vlc.State.Playing:
                return True
            
        return False


# # test run
# youtube_url = "https://www.youtube.com/watch?v=-pHfPJGatgE"    # Sparkle | Your Name AMV
# player = YouTubeAudioPlayer(sync=None)
# player.play(youtube_url)
            




# test
# youtube_url = "https://www.youtube.com/watch?v=-pHfPJGatgE"    # Sparkle | Your Name AMV

# template YouTube URL (tidak bisa yang dalam playlist private)
# play_youtube_audio(youtube_url, initial_volume=50)
