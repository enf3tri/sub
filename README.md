# Subtitle Generation for Videos
This repository contains a Python code that automatically generates subtitles for videos. The code is designed to be run in Google Colaboratory or local.
![alt text](https://github.com/enf3tri/sub/blob/main/img/sub-screen-1.png)
![alt text](https://github.com/enf3tri/sub/blob/main/img/sub-screen-2.png)

# Prerequisites
> Before running the code, make sure to install the necessary packages by executing the following commands:

on GoogleColab (Jupyter Notebook)
``` .py
!pip install ffmpeg moviepy
!pip install faster-whisper
!apt install imagemagick
!cat /etc/ImageMagick-6/policy.xml | sed 's/none/read,write/g'> /etc/ImageMagick-6/policy.xml
!pip install --upgrade translators
!pip install -U kora
  ```
  
 on local
 ``` .py
 pip install -r requirements.txt
 ``` 
 


# Usage
To generate subtitles for a video, follow these steps:

Import the add_text_to_video function from the subpy_lib module:

``` .py
from lib.subpy_lib import add_text_to_video
```
### Define the following variables:

**video_name**: The link to the video. For example, "example/Steve Jobs Secrets of Life.mp4".

**device_name**: The computing device to be used. Set it to "cuda" if your GPU supports CUDA, otherwise set it to "cpu". Note that using CPU computation will be slower.

**language_bool**: Set it to False if you want to add subtitles in the original language. Set it to True if you want to translate the subtitles.

**translation_language**: The language to translate the subtitles to. Choose from the following options: ["bg", "cs", "da", "nl", "en", "et", "fi", "fr", "de", "el", "hu", "id", "it", "ja", "ko", "lv", "lt", "no", "pl", "pt", "ro", "ru", "sk", "sl", "es", "sv", "tr", "uk"].

Call the **add_text_to_video** function with the defined variables:
``` .py
add_text_to_video(video_name, language_bool,translation_language,device_name)
  
```


Once the process is complete, a video player will be displayed showing the output video with subtitles.

### Please note that the code uses the following steps to generate subtitles:

- [ ] Extract the audio from the uploaded video and save it as result.mp3.
- [ ] Perform speech recognition on the audio using the Faster Whisper model.
- [ ] Create text clips for each detected segment of speech, with the corresponding start time, end time, and transcribed text.
- [ ] If translation is enabled, translate the transcribed text to the specified language using the translators package.
- [ ] Overlay the text clips onto the original video to create a new video with subtitles.
- [ ] Save the output video as output.mp4 and display it using an HTML video player.

Feel free to modify the code and experiment with different parameters to customize the subtitle generation process.



# Acknowledgements

This code utilizes the following packages:

**ffmpeg** and **moviepy** for video and audio processing

**faster-whisper** for speech recognition

**translators** for text translation

**kora** for file uploads to Google Colab


# Demo
### Original Video
[![Watch the video](https://img.youtube.com/vi/kYfNvmF0Bqw/default.jpg)](https://www.youtube.com/watch?v=kYfNvmF0Bqw)
### Result
[![Watch the video](https://img.youtube.com/vi/5NGPkdrmzIo/default.jpg)](https://www.youtube.com/watch?v=5NGPkdrmzIo)


# License
This code is released under the MIT License.
