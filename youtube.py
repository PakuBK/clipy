from pytube import YouTube
from urllib.error import HTTPError
import sys


def download_video(url: str):
    try:
        video = YouTube(url=url)
        video.streams.filter(progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(output_path="input", filename="input.mp4")
    except HTTPError:
        print("Something went wrong while downloading >:(")
        sys.exit(-1)

