import argparse
import os
import sys
from tkinter import filedialog, Tk

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
        youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
        print(f"Downloading {youtubeObject.title}...")
        return youtubeObject.download(output_path=path)
    except:
        print("An error has occurred")
    print("Download is completed successfully")


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
file = Download(link, filepath)
base, ext = os.path.splitext(file)
new_file = base + '.mp3'
os.rename(file, new_file)
print(f"Conversion completed successfully. MP3 file saved at {new_file}")




