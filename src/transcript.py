import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"
client = Groq()
filename = os.path.dirname(__file__) + "\splitted\part1.webm" 
with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
    file=(filename, file.read()),
    model="whisper-large-v3-turbo",
    prompt="make me a transcript of the audio file ",
    response_format="verbose_json",
    )
    print(transcription.segments)
    #save in a txt file 
    with open('transcript.txt', 'w') as f:
        for item in transcription.segments:
            f.write("%s\n" % item)
    with open('text_transcript.txt', 'w') as f:
        f.write(transcription.text)