import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog 

from pytube import YouTube 

import os
import shutil

from moviepy.editor import *


import time

resolutionList = [
  "144p", 
  "240p", 
  "360p", 
  "480p", 
  "720p", 
  "1080p", 
  "1440p", 
  "2160p", 
  "4320p"]

# Layout
def Widgets(): 
  #row 1: input label
  link_label = Label(
    root, 
    text = "YouTube link:", 
    font = ("Arial", 15, "bold"), 
    bg = "#202124", 
    fg = "#fff")
  link_label.grid(
    row = 1, 
    column = 0, 
    pady = 5, 
    padx = 5) 
   
  root.linkText = Entry(
    root, 
    width = 55, 
    textvariable = video_Link) 
  root.linkText.grid(
    row = 1, 
    column = 1, 
    pady = 5, 
    padx = 5, 
    columnspan = 2) 
   

  #row 2: destination label
  destination_label = Label(
    root, 
    text = "Destination:", 
    font = ("Arial", 15, "bold"), 
    bg = "#202124", 
    fg = "#fff") 
  destination_label.grid(
    row = 2, 
    column = 0, 
    pady = 5, 
    padx = 5) 
   
  root.destinationText = Entry(
    root, 
    width = 40, 
    textvariable = download_Path) 
  root.destinationText.grid(
    row = 2, 
    column = 1, 
    pady = 5, 
    padx = 5) 

  browse_B = Button(
    root, 
    text = "Browse", 
    cursor = "hand2", 
    highlightthickness = 0, 
    borderwidth = 0, 
    command = Browse,
    width = 10, 
    bg = "#661313", 
    fg = "#fff") 
  browse_B.grid(
    row = 2, 
    column = 2, 
    pady = 1, 
    padx = 1) 


  #row 3: set resolution

  resolutionLabel = Label(
    root, 
    text = "Resolution", 
    font = ("Arial", 15, "bold"), 
    bg = "#202124", 
    fg = "#fff")
  resolutionLabel.grid(
    row = 3, 
    column = 0) 
    
  selectLabel = Label(
    root, 
    text = "(select between 720p, 1080p, 1440p, 2160p):", 
    font = ("Arial", 12, "bold"), 
    bg = "#202124", 
    fg = "#fff")
  selectLabel.grid(
    row = 3, 
    column = 1) 


  root.setResolutionLabel = Entry(
    root, 
    width = 12, 
    textvariable = setResolution) 
  root.setResolutionLabel.grid(
    row = 3, 
    column = 2) 


  #row 3: download button
  Download_B = Button(
    root, 
    text = "Download", 
    cursor = "hand2", 
    highlightthickness = 0, 
    command = Download, 
    borderwidth = 0,
    width = 10, 
    bg = "#661313", 
    fg = "#fff") 
  Download_B.grid(
    row = 4, 
    column = 1, 
    pady = 1, 
    padx = 1)



# Browse file 
def Browse(): 
  download_Directory = filedialog.askdirectory(initialdir = "YOUR DIRECTORY PATH") 
  download_Path.set(download_Directory) 



# Download video
def Download():
  # Create a folder for temporary archives
  os.chdir(download_Path.get())
  os.mkdir("temp")


  # Responsible to initializate download, getting URL and path
  Youtube_link = video_Link.get() 
  download_Folder = download_Path.get() + "/temp"
  getVideo = YouTube(Youtube_link) 


  # Download video that will be used as audio
  videoStream = getVideo.streams.filter(
    res = "360p", 
    file_extension = "mp4").first()
  videoStream.download(download_Folder) 
  

  # Rename video that will be used as audio
  videoTitle = videoStream.title
  removable = '|'

  for letra in removable:
    if letra in videoTitle:
      videoTitle = videoTitle.replace(letra, '')

  os.chdir(download_Path.get() + "/temp")
  os.rename(f'{videoTitle}' + ".mp4", "audioFile.mp4")


  # Download video in preset quality
  videoResolution = setResolution.get()
  videoStream = getVideo.streams.filter(
    only_video = True, 
    res = videoResolution, 
    file_extension = "mp4").first()
  videoStream.download(download_Folder) 

  os.chdir(download_Path.get() + "/temp")
  os.rename(f'{videoTitle}' + ".mp4", "video.mp4")

  # Join the audio to video
  os.system("ffmpeg -i audioFile.mp4 -codec:a libmp3lame audio.mp3")
  os.system("ffmpeg -hwaccel_output_format cuda -y -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4")

  # Move file to path preset
  os.rename(download_Path.get() + "/temp/output.mp4", download_Path.get() + f'/{videoTitle}')
  
  # Remove temporary folder
  shutil.rmtree(download_Path.get() + "/temp")

root = tk.Tk() 

root.geometry("610x150") 
root.resizable(False, False) 
root.title("PyTube") 
root.config(background="#202124") 
    
   
video_Link = StringVar() 
download_Path = StringVar() 
resolution = StringVar()
setResolution = StringVar()
   
   
Widgets() 
   
root.mainloop()
