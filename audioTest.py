"""
install libary pemutar lagu lewat link youtube
pip install yt-dlp python-vlc
"""

import vlc
import yt_dlp as youtube_dl

# Nathanael / c14230178
def play_youtube_audio(youtube_url, sync, initial_volume=50):

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

            while True:
                state = player.get_state()

                # stop kalo musik selesai / muncul error
                if state in [vlc.State.Ended, vlc.State.Error]:
                    print("Music finished")
                    break

                # kalo ada interrupt dari user
                sync.control_input(player)

                # stop kalo playlist habis
                if sync.get_queue().isEmpty() == True:
                    break
                
                    




# test
# youtube_url = "https://www.youtube.com/watch?v=-pHfPJGatgE"    # Sparkle | Your Name AMV

# template YouTube URL (tidak bisa yang dalam playlist private)
# play_youtube_audio(youtube_url, initial_volume=50)
