from src.audio_scraper import audio_extractor
from src.splitter import split_file
import os 
youtube_link = "https://www.youtube.com/watch?v=Tt4_enX63K0"
audio_extractor(youtube_link)
audio_file = os.listdir('audio')[0]
file_dir = "audio/" + audio_file
split_file(file_dir)
