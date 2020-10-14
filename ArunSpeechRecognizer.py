import os
import speech_recognition as sr
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import threading
r = sr.Recognizer()
def ListenAndSet():
    r.pause_threshold = 1
    r.energy_threshold = 1500
    Speak['image'] = img2
    root.update()

    with sr.Microphone() as source:
        
        audio = r.listen(source)
        try:
            Speak['image'] = img3
            root.update()
            texts = r.recognize_google(audio,language="en")
            Box.insert(END,texts+" ")
            
            Speak['image'] = img
            root.update()

            
        except Exception as e:
            Speak['image'] = img
            root.update()
            Box.insert(END,str(e))
            pass

        


root = Tk()

root.geometry("800x500")
Label(root,text="welcome to Arun Speech Recognition Software",font=("consolas",20)).pack(pady=30)
# t = threading.Thread(target=ListenAndSet)
# t.setDaemon(True)
Speak = Button(root,text="Speak",font=("consolas",20),borderwidth=False,highlightthickness=0,command=ListenAndSet)

Speak.pack(pady=50)

Box = ScrolledText(root,font=("consolas",10))
Label(root,text="You Said: ",font=("consolas",15)).pack(pady=30)
Box.pack(fill=BOTH,expand=True)
img = PhotoImage(file="SpeakPython.png")
img2 = PhotoImage(file="MyMicListen.png")
img3 = PhotoImage(file="MyMicRecognise.png")
while True:
    Speak['image'] = img
    root.update()
    

    