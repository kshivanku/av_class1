import moviepy.editor as mp
import random

video = mp.VideoFileClip("clips/vox1.mp4");
video2 = mp.VideoFileClip("clips/ted1.mp4");

clips = []

for i in range(0,10):
	start = random.uniform(0, video.duration - 1)  #uniform is just like randint but it accepts floats
	end = start + 1
	clip1 = video.subclip(start, end)

	start = random.uniform(0, video2.duration - 1)
	end = start + 1
	clip2 = video2.subclip(start, end)

	clips.append(clip1)
	clips.append(clip2)

composition = mp.concatenate(clips)
composition.write_videofile("clips/juxtapose.mp4", fps = 25)