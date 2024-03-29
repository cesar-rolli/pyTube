# pyTube
App to download YouTube videos in any resolution with GUI.


# To install in Linux
``` javascript
# Clone the repository
$ git clone https://github.com/SINCJunior/ArtemPro

# Install dependencies
$ apt-get install python3 python3-pip python3-tk
$ pip install moviepy
$ pip install pytube

# To use FFMPEG with NVidia GPU's
$ git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git
$ cd nv-codec-headers && sudo make install && cd -
$ git clone https://git.ffmpeg.org/ffmpeg.git
$ sudo apt-get install build-essential yasm cmake libtool libc6 libc6-dev unzip wget libnuma1 libnuma-dev libmp3lame-dev
$ cd ffmpeg/
$ ./configure --enable-nonfree --enable-cuda-sdk --enable-libnpp --enable-libmp3lame --extra-cflags=-I/usr/local/cuda/include --extra-ldflags=-L/usr/local/cuda/lib64
$ make -j 8
$ sudo make install
```

# Frameworks
This project use tkinter to make GUI,
pytube to make an API and
moviepy to edit downloaded videos.
Was built entirely in Python.

## Notes
I use Moviepy previously but its very slow, so I change to FFMPEG. 

Results to process the video (in 1080p and download time is not included) in:
- Moviepy: 385 sec (6 min 25 sec)
- FFMPEG: 16 sec

Its around 24 times faster!

My PC specs are:
- Intel i7 10700K
- 2x8GB
- NVidia RTX 3070


# How it works?
YouTube don't allow to download videos in high resolutions with audio, so, my idea was download the video in 360p and use it as audio. 
Then, the sript download the video at resolution you chose (1080p(HD), 1440p(HD), 2160p(4K) or 4320p(8K)) and combine the video and audio.
This process will be slow and use a lot of your computer. 


### Video that I used in tests: https://www.youtube.com/watch?v=vp2yiZnjK0w

# Next steps:
- Download another resolution if the selected one is not available,
- Download multiple videos (multiprocess, maybe?),
- Download playlist (could select this option at GUI),
- Use Makefile (https://youtu.be/Yt-UF7fNLJE),
- Make a web page to download in other device (use my PC as server),
- Make an API to send the final video.

![Captura de tela de 2021-12-17 17-37-51](https://user-images.githubusercontent.com/52143802/146606082-e348d38f-cf2b-4252-b670-fa9170d76e68.png)
