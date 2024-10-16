# Target Interface (Expected by the client)
class MediaPlayer:
    def play(self, audio_type, file_name):
        pass


# Adaptee 1: VLC Player (Incompatible media player)
class VLCPlayer:
    def play_vlc(self, file_name):
        print(f"Playing VLC file: {file_name}")


# Adaptee 2: MP4 Player (Incompatible media player)
class MP4Player:
    def play_mp4(self, file_name):
        print(f"Playing MP4 file: {file_name}")


# Adapter 1: VLC Adapter
class VLCPlayerAdapter(MediaPlayer):
    def __init__(self, vlc_player):
        self.vlc_player = vlc_player

    def play(self, audio_type, file_name):
        if audio_type == "vlc":
            self.vlc_player.play_vlc(file_name)
        else:
            print(f"Unsupported format: {audio_type}")


# Adapter 2: MP4 Adapter
class MP4PlayerAdapter(MediaPlayer):
    def __init__(self, mp4_player):
        self.mp4_player = mp4_player

    def play(self, audio_type, file_name):
        if audio_type == "mp4":
            self.mp4_player.play_mp4(file_name)
        else:
            print(f"Unsupported format: {audio_type}")


# Client Code
class AudioPlayer:
    def play_audio(self, audio_type, file_name):
        if audio_type == "vlc":
            player = VLCPlayerAdapter(VLCPlayer())
            player.play(audio_type, file_name)
        elif audio_type == "mp4":
            player = MP4PlayerAdapter(MP4Player())
            player.play(audio_type, file_name)
        else:
            print(f"Unsupported audio type: {audio_type}")


# Example Usage
if __name__ == "__main__":
    audio_player = AudioPlayer()
    audio_player.play_audio("mp4", "song.mp4")  # Playing MP4 file: song.mp4
    audio_player.play_audio("vlc", "movie.vlc")  # Playing VLC file: movie.vlc
    audio_player.play_audio("avi", "video.avi")  # Unsupported audio type: avi


#OUTPUT:
# Playing MP4 file: song.mp4
# Playing VLC file: movie.vlc
# Unsupported audio type: avi
