import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
today = date.today()

with speech_recognition.Microphone() as mic:

    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)
print("Robot: ...")
try:
  you = robot_ear.recognize_google(audio)
except:
  you == " "
print("You: " + you)

if you == "":
  robot_brain = "I can't hear you, try again"
elif you == "Hello":
  robot_brain = "Hello peter"
elif you == "today":
  today = date.today()
  robot_brain = today.strftime("%B %d, %Y")
elif you == "time":
  now = datetime.now()
  robot_brain = now.strftime("%H hours %M minutes %S seconds")
else:
  robot_brain = "I'm fine, thanks"

print("Robot: " + robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
