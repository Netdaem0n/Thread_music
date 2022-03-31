from playsound import playsound
import os
import sys
from threading import Thread

commanda = ""


def play_sound():
    playsound(os.getcwd() + '\\music\\Halcyon.mp3')


def hi_men():
    while True:
        print("hello")
        global commanda
        commanda = input()
        if commanda == "exit":
            sys.exit()
        variant2 = lambda x: sys.exit() if x.lower() == "bye" else print("Not this time!\n")
        variant2(commanda)


t1 = Thread(target=play_sound, args=(), daemon=True)
t2 = Thread(target=hi_men, args=())

t1.start()
t2.start()
