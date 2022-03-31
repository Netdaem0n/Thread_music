from playsound import playsound
import os
import sys
from threading import Thread
a = ""

def play_sound():
    playsound(os.getcwd() + '\\music\\Halcyon.mp3')

def hi_men():
    while True:
        print("hello")
        a = input()
        if a == "exit":
            sys.exit()



t1 = Thread(target=play_sound, args=(), daemon=True)
t2 = Thread(target=hi_men, args=())


t1.start()
t2.start()
t1.join()
t2.join()