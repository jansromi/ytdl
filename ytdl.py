import argparse
import os
import sys
from tkinter import filedialog, Tk

from moviepy.editor import VideoFileClip
from pytube import YouTube


def Download(link, path):
    """
     Downloads the YouTube video from the given link 
     and saves it in the specified path. Returns the filename of the downloaded video.
     
     link = link to Youtube-video, as in https://www.youtube.com/watch?v=6uHPHn5Zwmo
     path = desired filepath where to save.
    """
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        print(f"Downloading {youtubeObject.title}...")
        youtubeObject.download(output_path=path)
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    return youtubeObject.title + ".mp4"


def ConvertMP4toMP3(filepath):
    """
    Converts the video file at the specified filepath from MP4 format to MP3 format using moviepy.
    Returns the filename of the converted audio file.

    filepath : path of the .mp4 file
    """
    print(f"Converting {filepath} to .mp3")
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
parser = argparse.ArgumentParser(
    description="Download and convert YouTube videos to MP3",
    epilog="Example usage: python youtube_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

# add the arguments
parser.add_argument("url", metavar="URL", help="the YouTube video URL")
parser.add_argument(
    "-o",
    "--output",
    metavar="PATH",
    help="the output directory. If not specified, a file dialog will be shown.",
)

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