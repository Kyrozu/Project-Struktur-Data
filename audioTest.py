"""
pip install yt-dlp python-vlc
"""

import vlc
import yt_dlp as youtube_dl
import time

def play_youtube_audio(youtube_url, initial_volume=50):
    # Setup options for yt-dlp to extract audio
    ydl_opts = {
        'format': 'bestaudio/best',  # Choose the best available audio format
        'noplaylist': True,          # Don't download playlists
        'quiet': True,               # Suppress unnecessary output
    }

    # Use yt-dlp to extract the audio URL
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        audio_url = info_dict.get('url', None)

        if audio_url:
            # Initialize VLC and play the audio stream
            instance = vlc.Instance()
            player = instance.media_player_new()
            media = instance.media_new(audio_url)
            player.set_media(media)
            
            print(f"Playing: {info_dict.get('title')}")
            player.audio_set_volume(initial_volume)  # Set initial volume
            player.play()

            # Wait until the audio starts playing
            time.sleep(2)  # Allow time for the player to start

            # Keep the script alive while the audio plays
            while True:
                state = player.get_state()

                if state in [vlc.State.Ended, vlc.State.Error]:
                    print("Playback finished.")
                    break

# Input YouTube URL (tidak bisa yang dalam playlist private)
# youtube_url = "https://www.youtube.com/watch?v=-pHfPJGatgE"    # Sparkle | Your Name AMV
# play_youtube_audio(youtube_url, initial_volume=50)
