# pyTube
App to download YouTube videos in any resolution with GUI.


# Frameworks
This project use tkinter to make GUI,
pytube to make an API and
moviepy to edit downloaded videos.
Was built entirely in Python.

# How it works?
YouTube don't allow to download videos in high resolutions with audio, so, my idea was download the video in 360p and use it as audio. 
Then, the sript download the video at resolution you chose (1080p(HD), 1440p(HD), 2160p(4K) or 4320p(8K)) and combine the video and audio.
This process will be slow and use a lot of your computer. (https://www.youtube.com/watch?v=vp2yiZnjK0w)

# Next steps:
- Do a better GUI using Electron JS;
- Use a Raspberry Pi 4 (in my case) to run scripts and not consume my PC;
- Make an API to connect new GUI with RPI.

![Captura de tela de 2021-12-17 17-37-51](https://user-images.githubusercontent.com/52143802/146606082-e348d38f-cf2b-4252-b670-fa9170d76e68.png)
