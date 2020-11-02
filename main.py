from pytube import YouTube
from tqdm import tqdm
from time import sleep
link = input("Enter Youtube video link here: \n")
yout = YouTube(link)
print("Title: ",yout.title)
video = yout.streams.get_highest_resolution()
for i in tqdm(range(0, 100), desc ="Downloading"): 
    sleep(.1)
    i = video.download("C:/Users/user/Desktop")
print("Download completed!!")