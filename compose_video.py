from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, vfx
from PIL import Image
import numpy as np
import os


def connect_everything(image_folder, durations, audio_file=None, zoom=0.08):
    """
    Builds a 1080×1920 slideshow where each still slowly zooms in.

    * image_folder – directory with .png/.jpg files (sorted by name)
    * durations    – list of seconds each image stays onscreen
    * audio_file   – optional soundtrack path
    * zoom         – extra scale reached at the end of each clip (0.08 → +8 %)
    """
    target_size = (1080, 1920)

    # collect images
    files = sorted(
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    )

    clips = []
    for path, d in zip(files, durations):
        frame = np.array(Image.open(path).resize(target_size, Image.Resampling.LANCZOS))

        clip = (
            ImageClip(frame)
            .with_duration(d)                     
            .with_position("center")
            .with_effects(                       
                [vfx.Resize(lambda t: 1 + zoom * (t / d))]
            )
        )
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    if audio_file:
        video = video.with_audio(AudioFileClip(audio_file))

    video.write_videofile("output_videos/output_video.mp4", fps=30)


if __name__ == "__main__":
    example_image_folder = "images/"
    example_durations = [2.5] * 10
    print(f"Example call: connect_everything('{example_image_folder}', {example_durations})")
    connect_everything(example_image_folder, example_durations, audio_file=None)
