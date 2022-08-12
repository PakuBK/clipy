from pytube import YouTube
from urllib.error import HTTPError
import sys
from datetime import datetime


def download_video(url: str):
    try:
        date = datetime.now()
        video = YouTube(url=url)
        video.streams.filter(progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(output_path="input", filename=f"input_{date.hour}_{date.minute}.mp4")
    except HTTPError:
        print("Something went wrong while downloading >:(")
        sys.exit(-1)

