from pytube  import YouTube
from sys import argv

#Test
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

vid = yt.streams.get_highest_resolution()

print(link)

vid.download('/Users/asdf/Desktop/YT Downloads')