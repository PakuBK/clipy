import os
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"
from moviepy.editor import *
from moviepy.video.fx.resize import resize
from console import *
from util import check_and_create_dir


def render_video(folder: str, caption: str, timestamp: tuple, credit: str):
    """
    :param folder: path to the video folder
    :param caption: caption put on the video
    :param timestamp: a tuple of timestamps in seconds to cut the clip
    :param credit: bottom text of the video
    """
    begin, end = timestamp
    if end - begin > 60:
        print_substep("[red]Video is over 60 seconds long and cannot be posted on Reels[/red]")

    video_files = [video for video in os.listdir(folder) if video.endswith(".mp4")]
    if len(video_files) == 0:
        print_error("no input file found")
        sys.exit(0)

    path = folder + "/" + video_files[0]

    video = VideoFileClip(path).subclip(t_start=begin, t_end=end)
    video = resize(video, width=1024)
    video = video.set_position(("center", "center"))

    caption_text_clip = TextClip(caption, fontsize=110, color='white', method="caption", size=(900, None))
    caption_text_clip = caption_text_clip.set_position(("center", (video.size[1]-50)-caption_text_clip.size[1]))

    credit_text = TextClip(credit, fontsize=90, color='white', method="caption", size=(900, None))
    credit_text = credit_text.set_position(("center", 1300))

    result = CompositeVideoClip([video, caption_text_clip, credit_text], size=(1024, 1920))
    result.duration = end-begin

    check_and_create_dir("output")

    print_step("[cyan]video is rendering, please wait[/cyan]")
    file_name = caption.replace(" ", "_")+f"_{str(begin)}-{str(end)}"
    try:
        result.write_videofile(f"output/{file_name}_clip.mp4", fps=25)
    except: # this is fine in this case and I will die on this hill if necessary
        print_error("something went wrong while rendering the video")

    video.close()

    check_and_create_dir("storage")
    print_step("moved input file in storage folder")
    os.rename(path, "storage/" + video_files[0])
