import moviepy.editor as mp
import translators as ts

from faster_whisper import WhisperModel
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_text_to_video(video_name, language_bool, translation_language, device_name):
    video_clip = VideoFileClip(video_name)
    vid_to_mp3(video_name)
    text_clips = []

    model = WhisperModel("large-v2", device=device_name, compute_type="float16")
    segments, info = model.transcribe("result.mp3", beam_size=1)
    
    for segment in segments:
        start_time = segment.start
        end_time = segment.end
        text = segment.text
        
        duration = end_time - start_time
        video_width, video_height = video_clip.size
        if language_bool:
          text_clip = TextClip(text, fontsize=24, font='Arial', color='yellow', bg_color = 'black',size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
        else:
          try:
            text_clip = TextClip(str(ts.translate_text(text,translator='deepl',to_language= translation_language)), fontsize=24, font='Arial', color='yellow', bg_color = 'black',size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
          except:
            text_clip = TextClip(str(ts.translate_text(text,to_language= translation_language)), fontsize=24, font='Arial', color='yellow', bg_color = 'black',size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)

        subtitle_x_position = 'center'
        subtitle_y_position = video_height* 4 / 5 

        text_position = (subtitle_x_position, subtitle_y_position)                    
        text_clips.append(text_clip.set_position(text_position))

    final_clip = CompositeVideoClip([video_clip] + text_clips)

    final_clip = final_clip.set_duration(video_clip.duration)
    final_clip = final_clip.set_audio(video_clip.audio)
    output_video = 'output.mp4'
    final_clip.write_videofile(output_video, codec='libx264', audio_codec='aac')
    
    return output_video


def vid_to_mp3(url):
  my_clip = mp.VideoFileClip(url)
  my_clip.audio.write_audiofile(r"result.mp3")
