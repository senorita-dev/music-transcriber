from sys import argv
from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context
# this import allows us to access the link to the youtube video

link = argv[1]
yt = YouTube(link)

print(f"You are downloading {yt.title}")

yt.streams.get_highest_resolution().download('./data')
