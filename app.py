from src.audio_scraper import audio_extractor
from src.splitter import split_file
from src.transcript import transcribe_audio
import os 
youtube_link = "https://www.youtube.com/watch?v=2QRlvKSzyVw&list=PLD80i8An1OEGqqXeNZ5w0IBmeZcxpZEYL"
audio_extractor(youtube_link)
audio_file = os.listdir('audio')[0]
file_dir = "audio/" + audio_file
split_file(file_dir)
transcribe_audio()
print("Transcription complete")
