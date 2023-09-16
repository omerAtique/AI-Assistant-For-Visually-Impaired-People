import os
import time
from pytube import YouTube

from pydub import AudioSegment

url = "https://www.youtube.com/watch?v=TJYY1IMpx5k&list=PLC2RC6xxDj2efWJjsD9ry4TSiH4pU4hHE"

youtube = YouTube(url)

video = youtube.streams.filter(only_audio=True).first()
out_file = video.download(output_path="./content/")

time.sleep(10)

audio = AudioSegment.from_file(out_file, format="mp4")
sliced_audio = audio[:1*60*1000]

os.makedirs("./content/chunk2")

sliced_audio.export("./content/chunk2/audio.wav", format= "wav")

