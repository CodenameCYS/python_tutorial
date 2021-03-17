import os
import argparse
from moviepy.editor import VideoFileClip

def get_video_audio(finpath, foutpath):
    video = VideoFileClip(finpath)
    audio = video.audio
    audio.write_audiofile(foutpath)
    return

def test():
    video_path = "E:\\movie\\IT狂人.The.IT.Crowd.S01E01.Chi_Eng.DVDRip.704X396-YYeTs人人影视.mkv"
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile('E:\\movie\\test.mp3')
    return

def main(finpath, foutpath):
    os.makedirs(foutpath, exist_ok=True)
    for filename in os.listdir(finpath):
        if os.path.isdir(os.path.join(finpath, filename)):
            continue
        videoname, suffix = os.path.splitext(filename)
        if not suffix in [".mp4", ".mkv"]:
            continue
        video_path = os.path.join(finpath, filename)
        audio_path = os.path.join(foutpath, f"{videoname}.mp3")
        get_video_audio(video_path, audio_path)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--finpath", type=str, required=True)
    parser.add_argument("--foutpath", type=str, required=True)
    args = parser.parse_args()

    main(args.finpath, args.foutpath)