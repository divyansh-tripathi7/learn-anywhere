import pytube

# Reading the YouTube link
video = "https://www.youtube.com/watch?v=x7X9w_GIm1s"
vid2 = "https://www.youtube.com/watch?v=wqRGa5sOUmc"
vid3 = 'https://www.youtube.com/watch?v=IJ3S44yJJU4'
# data = pytube.YouTube(video)
# data2= pytube.YouTube(vid2)
data3 = pytube.YouTube(vid3)

# Converting and downloading as 'MP4' file
audio = data3.streams.get_audio_only()
audio.download()


print("i am divi")

import whisper 


model = whisper.load_model("base")
# text = model.transcribe("Python in 100 Seconds.mp4")
# text2 = model.transcribe("STICK DIAGRAM - simplified (VLSI).mp4")

text3 = model.transcribe("Λεφτά υπάρχουν Βρέθηκαν στα γρήγορα για τις τράπεζες.mp4", task = 'translate')
#printing the transcribe
# print(text["text"])

print(text3['text'])


print("end")
# text3= model.transcribe("STICK DIAGRAM - simplified (VLSI).mp4", task = "translate")

# lang = model.detect_language()
# print(lang)