from pytubefix import YouTube
from pytubefix.cli import on_progress

url = 'https://www.youtube.com/watch?v=0JUN9aDxVmI'
yt = YouTube(url, on_progress_callback=on_progress)

def get_best_audio():
    max_audio = 0
    audio_value = 0
    for audio_stream in yt.streams.filter(only_audio=True):
        abr = int(audio_stream.abr.replace('kbps', ''))
        if abr > max_audio:
            max_audio = abr
            audio_value = audio_stream.itag
    return audio_value

audio_itag = get_best_audio()
yt.streams.get_by_itag(audio_itag).download()