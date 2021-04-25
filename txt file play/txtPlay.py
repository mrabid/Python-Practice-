from gtts import gTTS
import os

file = open("audio.txt", "r")
myText = file.read().replace("\n", " ")
language = 'en'
output = gTTS(text = myText, lang = language, slow = False)
output.save("output.mp3")
file.close()
os.system("start output.mp3")
print("Successful")

