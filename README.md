# ytdl
Ytdl is a quick and dirty command line tool for downloading Youtube-videos as audio or video streams.

### Dependencies
- Python 3.x
- pytube module
- tkinter module

To install these modules, simply run the following command:
	pip install pytube
	pip install tkinter

### Usage
To use the script, run the following command:
	python ytdl.py URL [-o PATH] [-v]
where URL is the YouTube video URL, -o PATH is an optional argument specifying the output directory,
and -v is an optional argument specifying whether to download the video instead of just the audio.

If -o PATH is not specified, a file dialog will be shown where the user can select the output directory.

### Example
	python ytdl.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -o C:/Users/Matti/Desktop -v

