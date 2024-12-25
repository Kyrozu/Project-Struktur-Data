"""
install libary pemutar lagu lewat link youtube
pip install yt-dlp python-vlc
"""

import vlc
import yt_dlp as youtube_dl
import time

# Nathanael / c14230178
def play_youtube_audio(youtube_url, initial_volume=50, max_duration=20):

    # setting untuk extract audio dari yt
    ydl_opts = {
        'format': 'bestaudio/best',  # audio format
        'noplaylist': True,          # no download playlists
        'quiet': True,               # no unnecessary output
        'no_warnings': True,         # no warnings
    }

    # extract audio dari URL youtube nya
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        audio_url = info.get('url', None)

        if audio_url:
            # initialize VLC
            instance = vlc.Instance()
            player = instance.media_player_new()
            media = instance.media_new(audio_url)
            player.set_media(media)
            
            player.audio_set_volume(initial_volume)  # setting volume audio
            player.play()

            # waktu mulai lagu
            start_time = time.time() 

            while True:
                state = player.get_state()

                # stop kalo musik selesai / muncul error
                if state in [vlc.State.Ended, vlc.State.Error]:
                    print("Playback finished.")
                    break

                # stop musik kalo sudah sampai waktu maksimal
                elapsed_time = time.time() - start_time
                if elapsed_time >= max_duration:
                    print(f"Music stop after {max_duration} second!")
                    player.stop()
                    break

# test
# youtube_url = "https://www.youtube.com/watch?v=-pHfPJGatgE"    # Sparkle | Your Name AMV

# template YouTube URL (tidak bisa yang dalam playlist private)
# play_youtube_audio(youtube_url, initial_volume=50)
