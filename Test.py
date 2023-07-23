from pytube import YouTube

url = 'https://www.youtube.com/watch?v=C7OQHIpDlvA' # The Wait - 1 Minute Short Film | Award Winning
my_video = YouTube(url)

vidTitle = my_video.title
vidViews = my_video.views
vidAuthor = my_video.author
vidDate = my_video.publish_date
finalDate = str(vidDate)
finalDate = finalDate[:10]
#vidPicture = my_video.thumbnail_url
finalInfo = "Title: " + str(vidTitle) + "\nAuthor: " + str(vidAuthor) + "\nViews: " + str(vidViews) + "\nDate Released: " + finalDate
print(finalInfo)
print(finalDate[:10])

my_video = my_video.streams.get_highest_resolution()
#my_video.download('C:\\Users\\asdf\\Desktop\\YTDownloads')