# Subtitles

Simple script to download subtitles for multiple video files from opensubtitles.org.
##### Usage

Change the following lines with valid credential for opensubtitles.org
```sh
USERNAME = "" # Fill with username
PASSWORD = "" # Fill with password
```

Execute the file with the desired video files or directories as arguments
```sh
$ python subtitles.py movie.mp4
$ python subtitles.py C:\Movies\Movie1
$ python subtitles.py C:\Movies\Movie1 movie.avi
```

Required dependency: python-opensubtitles
```sh
pip install python-opensubtitles
```
