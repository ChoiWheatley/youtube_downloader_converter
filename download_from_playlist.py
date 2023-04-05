from pytube import YouTube, Playlist
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
import sys

if len(sys.argv) == 1:
    print("usage: python download_from_playlist.py <link of playlist>")
    exit(2)


def download_video(video):
    print(f"Downloading: {video.title}")
    video.streams.filter(
        progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


LINK = sys.argv[1]

p = Playlist(LINK)
p._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")  # type: ignore

processes = []
with ThreadPoolExecutor() as executor:
    for video in p.videos:
        processes.append(executor.submit(download_video, video))