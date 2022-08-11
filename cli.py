import sys, getopt
from videocreation import render_video
from util import check_and_create_dir, convert_time
from youtube import download_video

def run_cli():
    argv = sys.argv[1:]
    caption, timestamp, credit = "", "", ""
    youtube_link = None
    try:
        opts, args = getopt.getopt(argv, "h:c:t:b:y:")
    except getopt.GetoptError:
        print('test.py -c "<caption>" -t "<00:00-00:00>" -cr "credit" (optional) -y <link>')
        sys.exit(2)
    for opt, arg in opts:
        print(opt, arg)
        if opt in ("-h", "-help"):
            print('test.py -c "<caption>" -t "<00:00-00:00>" -cr "credit" (optional) -y <link>')
            sys.exit(0)
        elif opt in ('-c', '-caption'):
            caption = arg
        elif opt in ("-t", "-timestamp"):
            timestamp = arg
        elif opt in ("-b", "-credit"):
            credit = arg
        elif opt in ("-y", "-youtube"):
            youtube_link = arg

    timestamp = (convert_time(time) for time in timestamp.split("-"))
    check_and_create_dir("input")
    if youtube_link is not None:
        download_video(youtube_link)
    render_video("input", caption, timestamp, credit)



if __name__ == "__main__":
    run_cli()