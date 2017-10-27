import moviepy.editor as mp
import random 

video = mp.VideoFileClip("clips/vox1.mp4");

clips = []

start = 0
duration = 0.5
end = start + duration

#chopping the entire video in 0.5 sec clips
while end < video.duration:
	clip = video.subclip(start, end)
	clips.append(clip)
	start = start + duration
	end = end + duration

random.shuffle(clips) #shuffles the elements of an array randomly
clips = clips[0:10] #selecting the first 10 elements in the clips list

composition = mp.concatenate(clips)
composition.write_videofile("clips/random.mp4")