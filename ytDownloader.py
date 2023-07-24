import tkinter
import customtkinter
from pytube import YouTube

showProgress = False

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)

        pathLink = folder_link.get()
        pathLink = str(pathLink)

        vid = ytObject.streams.get_highest_resolution()

        showProgress = True

        if pathLink=="":
            vid.download()
        else:
            vid.download(pathLink)

        finishLabel.configure(text="Download Complete!", text_color="green")


        vidTitle = ytObject.title
        vidViews = ytObject.views
        vidAuthor = ytObject.author
        vidDate = ytObject.publish_date
        finalDate = str(vidDate)
        finalDate = finalDate[:10]

        #vidPicture = ytObject.thumbnail_url
        finalInfo = "Title: " + str(vidTitle) + "\nChannel: " + str(vidAuthor) + "\nViews: " + str(vidViews) + "\nDate Released: " + finalDate
        downloadInfo.configure(text=finalInfo, text_color="white")

    except:
        finishLabel.configure(text="Download Failed. Try Again.", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    p_of_completion = bytes_downloaded / total_size

    progressBar.set(p_of_completion)
    progressBar.update()

    per = str(int(p_of_completion*100))

    pPercentage.configure(text=per+'%')
    pPercentage.update()


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")

# Adding UI Elements
header = customtkinter.CTkLabel(app, text = "YouTube Downloader", font=('', 40))
header.pack(padx=5, pady=25)

title = customtkinter.CTkLabel(app, text="Paste YouTube link here:")
title.pack(padx=10, pady=10)

# Link URL input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height=30, textvariable=url_var)
link.pack()

# Link file system input
file_title = customtkinter.CTkLabel(app, text="Paste file path here:")
file_title.pack(padx=10, pady=10)

folder_var = tkinter.StringVar()
folder_link = customtkinter.CTkEntry(app, width = 350, height=30, textvariable=folder_var)
folder_link.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", height=40, width=160, corner_radius=30, hover_color="red", fg_color="grey", command=startDownload)
download.pack(padx=15, pady=15)

# Complete message
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%", )
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400, progress_color="red")
progressBar.set(0)
progressBar.pack()


# Add download info
downloadInfo = customtkinter.CTkLabel(app, text="")
downloadInfo.pack(padx=20, pady=20)

# Run app
app.mainloop()

#python -m YTDownloader.py --noconsol --onefile --icon="C:\Users\asdf\Desktop\Python Projects\ytDownloader\YTDownloader.ico"