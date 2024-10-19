import os
import glob
from pytubefix import YouTube
from pytubefix.cli import on_progress

def get_best_audio(yt):
    max_audio = 0
    audio_value = 0
    for audio_stream in yt.streams.filter(only_audio=True):
        abr = int(audio_stream.abr.replace('kbps', ''))
        if abr > max_audio:
            max_audio = abr
            audio_value = audio_stream.itag
    return audio_value

output_directory = 'audio'
if os.path.exists(output_directory):
    files = glob.glob(f'{output_directory}/*')
    for f in files:
        os.remove(f)
os.makedirs(output_directory, exist_ok=True)

def audio_extractor(link):
    yt = YouTube(link, on_progress_callback=on_progress)
    audio_itag = get_best_audio(yt)
    yt.streams.get_by_itag(audio_itag).download(output_path=output_directory)