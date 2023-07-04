from pytube  import YouTube
from sys import argv

#Test
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)