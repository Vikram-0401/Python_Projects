import pyttsx3

engine = pyttsx3.init()
print("Welcome to Robo Speaker 1.1  Created by Vikram")

while True:
    x = input("Enter what you want to speak: ")
    if x.lower() == "exit":
        engine.say("Goodbye")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()
