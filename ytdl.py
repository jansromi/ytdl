import argparse
import os
import sys
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

# create the parser for command-line arguments
parser = argparse.ArgumentParser(description="Download and convert YouTube videos to MP3")

# add the arguments
parser.add_argument("url", metavar="URL", help="the YouTube video URL")
parser.add_argument("-o", "--output", metavar="PATH", help="the output directory")

# parse the arguments
args = parser.parse_args()

# check if the user requested help
if "help" in args:
    parser.print_help()
    sys.exit(0)

# get the YouTube URL and output directory
link = args.url
filepath = args.output

if not filepath:
    filepath = filedialog.askdirectory()

mp4_filename = Download(link, filepath)
mp4_filepath = os.path.join(filepath, mp4_filename)

mp3_filename = ConvertMP4toMP3(mp4_filepath)
os.remove(mp4_filepath)

print(f"Conversion completed successfully. MP3 file saved at {mp3_filename}")