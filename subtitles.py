import os, sys, filetype, time
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File

USERNAME = "" # Fill with username
PASSWORD = "" # Fill with password
LANGUAGE = "en"

def end(msg):
    print("    " + msg)
    exit(0)

def videosFromDir(dir):
    videos = []
    for path, subdirs, files in os.walk(dir):
        for name in files:
            fullPath = os.path.join(path, name)
            guess = filetype.guess(fullPath)
            if guess and guess.mime.startswith("video/"):
                videos.append(fullPath)
    return videos

def main():
    if len(sys.argv) < 2:
        end("Specify at least one file or directory ie: > python subtitles.py movie.mp4")
    ost = OpenSubtitles() 
    ost.login(USERNAME, PASSWORD)
    paths = sys.argv
    paths.pop(0)
    files = []
    for path in paths:
        if os.path.isdir(path):  
            files += videosFromDir(path)
        elif os.path.isfile(path):
            files.append(os.path.abspath(path))
        else:  
            end("Error reading file or directory '" + path + "'")

    if not files:
        end("No video files were found")

    for i in files:
        f = File(i)
        hash = f.get_hash()
        size = f.size
        data = ost.search_subtitles([{"sublanguageid": LANGUAGE, "moviehash": hash, "moviebytesize": size}])
        time.sleep(1)
        if data:
            split = i.split(".")
            split.pop()
            srtDir = ".".join(split) + ".srt"
            srtDir = srtDir.split(os.path.sep)
            srtName = srtDir.pop()
            srtDir = os.path.sep.join(srtDir)
            idSubFile = data[0].get("IDSubtitleFile")
            ost.download_subtitles([idSubFile], override_filenames={idSubFile: srtName}, output_directory=srtDir, extension="srt")
            time.sleep(1)
            print("    Added " + srtDir + os.path.sep + srtName)
    
    ost.logout()

main()