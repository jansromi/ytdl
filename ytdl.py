import argparse
import os
import sys
from tkinter import filedialog, Tk

from pytube import YouTube

def CreateArgParser():
    parser = argparse.ArgumentParser(
        description="Download and convert YouTube videos to MP3",
        epilog="Example usage: python youtube_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("url", metavar="URL", help="the YouTube video URL")
    parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        help="the output directory. If not specified, a file dialog will be shown.",
    )
    parser.add_argument(
        "-v",
        action="store_true",
        help="downloads the youtube-link as a video",
    )

    return parser

def DownloadMP3(link, path):
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
        # Get the default filename from pytube and add the ".mp3" extension
        filename = youtubeObject.default_filename.replace(".mp4", ".mp3")
        filepath = os.path.join(path, filename)
        youtubeObject.download(output_path=path, filename=filename)
        return filepath
    except Exception as e:
        print(f"An error has occurred: {e}")
        sys.exit(0)

def DownloadVideo(link, path):
    """
    Downloads the YouTube video from the given link and saves it in the specified path.
    Returns the filename of the downloaded video.

    link = link to Youtube-video, as in https://www.youtube.com/watch?v=6uHPHn5Zwmo
    path = desired filepath where to save.
    """
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print(f"Downloading {youtubeObject.title}...")
        filename = youtubeObject.default_filename
        filepath = os.path.join(path, filename)
        youtubeObject.download(output_path=path, filename=filename)
        return filepath
    except Exception as e:
        print(f"An error has occurred: {e}")
        sys.exit(0)

if __name__ == "__main__":
    # hide the main window
    root = Tk()
    root.withdraw()

    parser = CreateArgParser()

    # parse the arguments and check if the user requested help
    args = parser.parse_args()
    if "--help" in sys.argv or "-h" in sys.argv:
        parser.print_help()
        sys.exit(0)

    # get the YouTube URL and output directory
    link = args.url
    filepath = args.output
    asVideo = args.v  
    downloaded = None
    if not filepath:
        filepath = filedialog.askdirectory()
    if not asVideo:
        downloaded = DownloadMP3(link, filepath)
    else:
        downloaded = DownloadVideo(link, filepath)

    if downloaded is not None:
        print(f"Conversion completed successfully. File saved at {downloaded}")








