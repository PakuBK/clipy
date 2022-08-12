from videocreation import render_video
from youtube import download_video
from console import *
from util import convert_time, check_and_create_dir


def gather_clips_information() -> list:
    def get_clip_information() -> tuple:
        caption = ask_user("caption")
        timestamp = ask_user("timestamp", default="hh:mm:ss-hh:mm:ss")
        timestamp = (convert_time(time) for time in timestamp.split("-"))
        credit = ask_user("credit (placed at the bottom)")
        return caption, timestamp, credit

    multiple_clips = confirm_by_user(" do you want to create multiple clips?")

    if multiple_clips:
        clips = []
        while True:
            clips.append(get_clip_information())
            if not confirm_by_user(" continue?"):
                return clips
    else:
        return [get_clip_information()]


def prepare():
    print_step("[red]you can choose a video file or download one from youtube later")
    clips = gather_clips_information()
    clear_console()

    should_download_video = confirm_by_user(" do you want download the video from youtube?")

    check_and_create_dir("input")
    if should_download_video:
        url = ask_user(" paste the youtube link here")
        print_substep(" downloading video...")
        download_video(url)
    else:
        confirm_by_user(" is your video file in the input folder?")

    clip_id = 0
    for caption, timestamp, credit in clips:
        render_video("input/", caption, timestamp, credit)
        clip_id += 1


if __name__ == "__main__":
    clear_console()
    print_title("AutoPyClip")
    prepare()
