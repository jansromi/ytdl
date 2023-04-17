import os
from tkinter import filedialog, Tk

from moviepy.editor import VideoFileClip
from pytube import YouTube

def Download(link, path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("Starting download...")
        youtubeObject.download(output_path=path)
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    return youtubeObject.title + ".mp4"


def ConvertMP4toMP3(filepath):
    video_file = VideoFileClip(filepath)
    audio_file = video_file.audio
    mp3_filename = filepath.replace(".mp4", ".mp3")
    audio_file.write_audiofile(mp3_filename)
    video_file.close()
    audio_file.close()
    return mp3_filename


# hide the main window
root = Tk()
root.withdraw()

link = input("Enter the YouTube video URL: ")
filepath = filedialog.askdirectory()

mp4_filename = Download(link, filepath)
mp4_filepath = os.path.join(filepath, mp4_filename)

mp3_filename = ConvertMP4toMP3(mp4_filepath)
os.remove(mp4_filepath)

print(f"Conversion completed successfully. MP3 file saved at {mp3_filename}")