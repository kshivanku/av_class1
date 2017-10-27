import moviepy.editor as mp
import random

video = mp.VideoFileClip("clips/vox1.mp4");
video2 = mp.VideoFileClip("clips/ted1.mp4");

clips = []

clip1 = video.subclip(0,3)
clip2 = video2.subclip(0,3)

clip1 = clip1.set_pos((100, 100)).resize((400,400))  #you can dot connect functions
clip1 = clip1.set_start(1) #clip pops in at 1 sec after movie starts
clip1 = clip1.crossfadein(1)
clip1 = clip1.volumex(0)

clips.append(clip2)
clips.append(clip1)
#clips are layered according to their position in the list. 

composition = mp.CompositeVideoClip(clips)
composition.write_videofile('clips/overlay.mp4', fps=25)