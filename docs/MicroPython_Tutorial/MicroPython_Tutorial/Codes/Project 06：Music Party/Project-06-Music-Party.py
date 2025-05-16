'''
Function: Clap your hands, the microbit microphone receives the sound signal, the music sounds, and the RGB emits a dazzling light to simulate a musical party
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
import music

display.clear() # clear LED matrix

while True:
    if microphone.current_event() == SoundEvent.LOUD:  # If the microphone picks up a loud signal
       music.play(["G3:4", "G3", "A4"]) # the speaker plays some tones
       pin1.write_analog(1023)      # P1 analog value is 1023,RGB is red
       pin2.write_analog(0)
       # pin3.write_analog(0)
       sleep(100)
       music.play(["G4:4", "C5", "B4"])
       pin1.write_analog(0)         # P1 analog value is 0,RGB is not red
       pin2.write_analog(1023)      # P2 analog value is 1023,RGB is green
       # pin3.write_analog(0)
       sleep(100)
       pin1.write_analog(10)
       pin2.write_analog(10)
       # pin3.write_analog(1023)      # P3 analog value is 1023,RGB is blue
       sleep(100)
       music.play(["G4:4", "D5", "C5"])
       pin1.write_analog(123)
       pin2.write_analog(123)
       # pin3.write_analog(0)
       sleep(100)
       music.play(["G4:4", "D5", "C5"])
       pin1.write_analog(1023)
       pin2.write_analog(400)
       # pin3.write_analog(1023)
       sleep(100)
       music.play(["G3:4", "G3", "G4"])
       pin1.write_analog(10)
       pin2.write_analog(1023)
       # pin3.write_analog(1023)
       sleep(100)
       pin1.write_analog(1023)
       pin2.write_analog(1023)
       # pin3.write_analog(1023)
       sleep(100)
       music.play(["E5:4", "C5", "B4", "A4"])
       pin1.write_analog(32)
       pin2.write_analog(184)
       # pin3.write_analog(336)
       sleep(100)
       pin1.write_analog(640)
       pin2.write_analog(328)
       # pin3.write_analog(180)
       sleep(100)
       music.play(["F5:4", "F5", "E5"])
       pin1.write_analog(552)
       pin2.write_analog(172)
       # pin3.write_analog(904)
       sleep(100)
       pin1.write_analog(1020)
       pin2.write_analog(796)
       # pin3.write_analog(560)
       sleep(100)
       music.play(["C5:4", "D5", "C5"])
       pin1.write_analog(136)
       pin2.write_analog(560)
       # pin3.write_analog(140)
       sleep(100)
       pin1.write_analog(0)
       pin2.write_analog(0)
       # pin3.write_analog(0)
       sleep(100)
if microphone.current_event() == SoundEvent.QUIET:  # If the microphone picks up a quie signal
       pin1.write_analog(0)
       pin2.write_analog(0)
