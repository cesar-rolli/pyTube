from flask import Flask, request, json
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def api():
  return {
    'userId': 1,
    'title': 'Flask React Application',
    'completed': False
  }

@app.route('/youtube', methods=["POST"])
def create():
  request_link = request.json['link']
  request_resolution = request.json['resolution']
  return {request_link, request_resolution}



# Youtube_link = "https://www.youtube.com/watch?v=7LNl2JlZKHA" 
# getVideo = YouTube(Youtube_link)
# videoTitle = getVideo.streams.first().title


# # Download video
# # def Download():
# # To discover the right path
# os.chdir("/home/cesar/Documentos/Code/pyTube/server")
# path = os.getcwd()

# # Responsible to initializate download, getting URL and path
# Youtube_link = "https://www.youtube.com/watch?v=eVvIZ3f2tSU" 
# getVideo = YouTube(Youtube_link)

# # Download video that will be used as audio
# videoStream = getVideo.streams.filter(
#   res = "360p", 
#   file_extension = "mp4").first()

# # Rename video title
# videoTitle = videoStream.title
# removable = '|#!?'
# for letra in removable:
#   if letra in videoTitle:
#     videoTitle = videoTitle.replace(letra, '')

# # Changing path
# download_Folder = path + "/temp"
# os.chdir(download_Folder)
# videoStream.download(download_Folder) 

# os.rename(f"{videoTitle}" + ".mp4", "audioFile.mp4")

# # Download video in preset quality
# videoResolution = "1080p"
# videoStream = getVideo.streams.filter(
#   only_video = True, 
#   res = videoResolution, 
#   file_extension = "mp4").first()
# videoStream.download(download_Folder) 
# os.rename(f'{videoTitle}' + ".mp4", "video.mp4")

# # Join the audio to video
# os.system("ffmpeg -i audioFile.mp4 -codec:a libmp3lame audio.mp3")
# os.system("ffmpeg -hwaccel_output_format cuda -y -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4")

# # Move file to path preset
# os.rename(download_Folder + "/output.mp4", path + f'/{videoTitle}')
# os.chdir(download_Folder)
# os.remove("audio.mp3")
# os.remove("audioFile.mp4")
# os.remove("video.mp4")

if __name__ == "__main__":
  app.run()