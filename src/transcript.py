import os
from groq import Groq
import dotenv

dotenv.load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = groq_api_key

client = Groq()

cwd = os.getcwd()
print(cwd)
audio_dir = os.path.join(cwd, 'splitted')  
filename = os.path.join(audio_dir, 'part1.webm')  
script_dir = cwd

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
        file=(filename, file.read()),
        model="whisper-large-v3-turbo",
        prompt="make me a transcript of the audio file",
        language="ja" , 
        response_format="verbose_json",
    )
    transcript_path = os.path.join(script_dir, 'transcript.txt')
    text_path = os.path.join(script_dir, 'text.txt')
    with open(transcript_path, 'w', encoding='utf-8') as f:
        for item in transcription.segments:
            f.write("%s\n" % item)
    with open(text_path, 'w', encoding='utf-8') as f :
        f.write(transcription.text)