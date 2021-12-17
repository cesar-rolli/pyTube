import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog 

from pytube import YouTube 

import os
import shutil

from moviepy.editor import *

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

#Layout
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



#Browse file 
def Browse(): 
  download_Directory = filedialog.askdirectory(initialdir = "YOUR DIRECTORY PATH") 
  download_Path.set(download_Directory) 



#Download video
def Download():
  #Create a folder for temporary archives
  os.chdir(download_Path.get())
  os.mkdir("Temporary Folder from PyTube")


  #Responsible to initializate download, getting URL and path
  Youtube_link = video_Link.get() 
  download_Folder = download_Path.get() + "/Temporary Folder from PyTube"
  getVideo = YouTube(Youtube_link) 


  #Download video that will be used as audio
  videoStream = getVideo.streams.filter(
    res = "360p", 
    file_extension = "mp4").first()
  videoStream.download(download_Folder) 
  

  #Rename video that will be used as audio
  videoTitle = videoStream.title
  removable = '|'

  for letra in removable:
    if letra in videoTitle:
      videoTitle = videoTitle.replace(letra, '')

  os.chdir(download_Path.get() + "/Temporary Folder from PyTube")
  os.rename(f'{videoTitle}' + ".mp4", "audioFile.mp4")


  #Download video in preset quality
  videoResolution = setResolution.get()
  videoStream = getVideo.streams.filter(
    only_video = True, 
    res = videoResolution, 
    file_extension = "mp4").first()
  videoStream.download(download_Folder) 
  

  #Join the audio to video 
  clip = VideoFileClip(f'{videoTitle}' + ".mp4")
  audioclip = AudioFileClip("audioFile.mp4")
  videoclip = clip.set_audio(audioclip)

  os.chdir(download_Path.get())
  videoclip.write_videofile(f'{videoTitle}' + ".mp4")


  #Remove temporary folder
  shutil.rmtree("Temporary Folder from PyTube")


  #Display a message informing download has been completed
  messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_Folder) 

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
