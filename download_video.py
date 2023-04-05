from pytube import YouTube
import sys

if len(sys.argv) == 1:
    print("usage: python download_video.py <link of video>")
    exit(2)

LINK = sys.argv[1]

yt = YouTube(LINK)

print(f"Downloading... {yt.title}")

stream = yt.streams.filter(progressive=True,
                  file_extension='mp4').order_by('resolution').desc().first()

if stream != None:
    stream.download()
else:
    print("Video download failed")
    exit(2)
