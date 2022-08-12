# clipy
a command line interface that can creates clips targeted at mobile plattforms.

### intention of clipy
as a modern content creator you cannot come around tiktok, reels and youtube shorts. clipys intention is to make it easier for content creators to clip funny or interesting parts of their content and make it tiktok ready in seconds.

### what clipy automates
you have to tell clipy the caption and where to cut the clip, thats it!
clipy can than cut a clip from the video, put text onto it and change it aspect ratio to 9:16
<br/>

### set up imagemagick
download Imagemagick from https://imagemagick.org/script/download.php <br/>
in videocreation.py one line 2 replace the path with your path to magick
```Python
os.environ["IMAGEMAGICK_BINARY"] = r"C:\your\path\magick.exe"
```

### installation for windows

1. clone the repo
2. open cmd and type 'python -m venv venv' to create a virtual environment
3. navigate to 'venv/Scripts' and type 'activate.bat' to activate the venv
4. navigate back to the main directory
5. pip install -r requirements.txt

### usage
put the video file in the input folder
start main.py, specify the caption and the timestamps you want to clip from
wait for clipy to put the rendered videos in the output folder

### using true cli(py)
this method is recommended if you want to only create a single clip
use ```cli.py -h``` to display help
place your file in the input folder or add the flag -y <link>
```
cli.py -c "<caption>" -t "<00:00-00:00>" -cr "credit" (optional) -y <link>
```
executing this command will generate a clip in the output folder

### issues and limitations
- only .mp4 files are currently supported
- sometimes the youtube download fails
- font size, color or position cannot be modified



