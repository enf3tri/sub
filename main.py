from lib.subpy_lib import add_text_to_video

if __name__ == '__main__':
  video_name = " "  # Link to the video for example: "example/Steve Jobs Secrets of Life.mp4"
  device_name = "cuda" #This will be define your computing device. If your GPU is not supports CUDA you can convert into "cpu" but it will be extremly slow.
  language_bool = False  #If set to True, it will add subtitles in the original language. Otherwise translated subtitles will be added
  translation_language = 'tr' #["bg", "cs", "da", "nl", "en", "et", "fi", "fr", "de", "el", "hu", "id", "it", "ja", "ko", "lv", "lt", "no", "pl", "pt", "ro", "ru", "sk", "sl", "es", "sv", "tr", "uk"]

  add_text_to_video(video_name, language_bool,translation_language,device_name)


