# pyTube
App to download YouTube videos in any resolution with GUI.


# frameworks
This project use tkinter to make GUI,
pytube to make an API and
moviepy to edit downloaded videos.
Was built entirely in Python.

# how it works?
YouTube don't allow to download videos in high resolutions with audio, so, my idea was download the video in 360p and use it as audio. 
Then, the sript download the video at resolution you chose between 1080p(HD), 1440p(HD), 2160p(4K) or 4320p(8K) and combine the video and audio.
This process will be slow and will use a lot of your computer.

# next step
- Do a better GUI using Electron JS;
- Use a Raspberry Pi 4 (in my case) to run scripts and not consume my PC;
- Make an API to connect new GUI with RPI.
