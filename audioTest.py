"""
pip install yt-dlp python-vlc
"""
import vlc
import yt_dlp as youtube_dl
import time

def play_youtube_audio(youtube_url, initial_volume=50, max_duration=20):

    # setup untuk extract audio
    ydl_opts = {
        'format': 'bestaudio/best',  # audio format
        'noplaylist': True,          # no download playlists
        'quiet': True,               # no unnecessary output
        'no_warnings': True,         # no warnings
    }

    # extract audio dari URL youtube
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        audio_url = info.get('url', None)

        if audio_url:
            # Initialize VLC and play audio
            instance = vlc.Instance()
            player = instance.media_player_new()
            media = instance.media_new(audio_url)
            player.set_media(media)
            
            player.audio_set_volume(initial_volume)  # setting volume audio
            player.play()

            # Keep the script alive while the audio plays
            start_time = time.time()  # record the start time

            while True:
                state = player.get_state()

                # Check if playback has finished or encountered an error
                if state in [vlc.State.Ended, vlc.State.Error]:
                    print("Playback finished.")
                    break

                # Break the loop after max_duration seconds
                elapsed_time = time.time() - start_time
                if elapsed_time >= max_duration:
                    print(f"Music stop after {max_duration} second!")
                    player.stop()
                    break

# youtube_url = "https://www.youtube.com/watch?v=-pHfPJGatgE"    # Sparkle | Your Name AMV

# template YouTube URL (tidak bisa yang dalam playlist private)
# play_youtube_audio(youtube_url, initial_volume=50)
