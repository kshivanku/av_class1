import moviepy.editor as mp

# video = mp.VideoFileClip("vox1.mp4") #saves the video file in the variable video
video = mp.VideoFileClip("clips/vox1.mp4").subclip(0,1) #saves a subclip of the entire video
video2 = mp.VideoFileClip("clips/ted1.mp4").subclip(10, 12)

clips = [video, video2]

#Combining two clips together
composition = mp.concatenate(clips) #accepts as a parameter a list of video clips

#Saving the file to disk, write the name of the output file in (), any value for fps can be defined
composition.write_videofile("clips/composition.mp4", fps = 25) 

#Resizing your video
# video = video.resize((800,600)) #double paranthesis