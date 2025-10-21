from pytubefix import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import threading

import time

def on_progress(stream, chunk, bites_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bites_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progressbar["value"] = percentage
    app.update()


def download_video():
    link = entry_display.get()
    yt = YouTube(link, on_progress_callback=on_progress)
    yd = yt.streams.filter(res="720p").first()
    yd.download("/Users/aleee/OneDrive/Desktop/videos")

    messagebox.showinfo('Notification', 'Video has been downloaded.')

def start_download():
    threading.Thread(target=download_video).start()

app = Tk()

app.geometry("820x600")

app.title("YouTube Downloader")

app.resizable(False, False)

app.configure(bg="gray20")

progressbar = ttk.Progressbar(app, orient='horizontal', length=300, mode='determinate')
progressbar.pack(pady=20)

top_panel=Frame(app, bd = 1, relief=FLAT)
top_panel.pack(side=TOP)

frame1 = Frame(app, bg="white", width=100, height=100)
frame1.place(x=220, y=250)

button1 = Button(frame1, text="Download", command=start_download)
button1.pack(side=RIGHT)

title_tag = Label(top_panel, text="YouTube Downloder", fg='white',
                  font=('Dosis', 38),bg="gray20", width=23)
title_tag.grid(row=0, column=1)

entry_panel = Frame(frame1, bd = 1, relief=FLAT, bg='burlywood')
entry_panel.pack()

entry_display = Entry(entry_panel,
                           font=('Dosis', 16, 'bold'),
                           width=32,
                           bd=1)
entry_display.grid(row=0, column=0, columnspan=4)




app.mainloop()
