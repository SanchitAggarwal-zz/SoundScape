#!/usr/bin/env python
''' Experiment to generate random location and sound corresponding to those location.
    The following attributes of sound are used to map the 3D location of the  real world:
        Y-Axis or Height (on the scale of -5 0 5 ) : with increasing Pitch of sound.
        X-Axis or Direction (Left or Right) : time duration of the signal within a channel.
        Z-Axis or Depth (on scale of -5 0 5 ) : with amplitude of sound for each channel.
    The produce soundScape for location is being used for training.
    A random test is conducted to check the accuracy of these mapping on Blindfolded people.
    Furthermore Color is also represented using different frequency for each sound.

'''
import sys
import wave
import random
import math
import struct
import argparse
from itertools import *
from numpy import linspace,sin,pi,int16
import pygame
import time
from scipy.io.wavfile import write
from pylab import plot,show,axis
from enum import Enum
import time

__author__ = 'luminous'

#initial standard 13 tones from A-440 to A-880 increasing pitch
pitch=[440,466,494,523,554,587,622,659,698,740,784,831,880]

#class for generating a random point in real world  #call with initial values
#For only X Point(1,0,0)
#For only Y Point(0,1,0)
#For only Z Point(0,0,1)
class Point:
    def __init__(self,x=1,y=1,z=1,step=5,mode=0):
        """
        :param mode: Training Mode = 0, Testing Mode = 1, for generating random numbers
        :param x: X coordinate for channel and duration
        :param y: Y coordinate for pitch
        :param z: Z coordinate for amplitude
        :param step:scale size for each coordinate
        """
        if mode == 0:
            self.x=x
            self.y=y
            self.z=z
        elif mode == 1:
            self.x=random.randint(-1*step,step)*x
            self.y=random.randint(0,2*step)*y
            self.z=random.randint(0,2*step)*z


class SoundScape:
    def __init__(self,pitch,rate=44100):

        """
        :param pitch: the standard pitch for sound
        :param rate: No of samples per seconds
        """
        self.pitch=pitch
        self.rate=rate
        self.Left=1
        self.Right=1

    def generateSineWave(self, point,amp=1000,step=5):
        """
        :rtype : sound, the resultant tone
        :param amp: amplitude of the sound signal,initial vale 1000 which increases with depth
        :param step: scale size for each coordinate
        :param point: sine wave corresponding to the 3D point
        :param channel: the channel either Left or Right
        """
        if point.x < 0 :
            self.Right=0   #set the right speaker volume to zero
        elif point.x > 0 :
            self.Left=0    #set the left speaker volume to zero

        self.length=1+math.fabs(point.x)
        self.duration=linspace(0,self.length,self.length*self.rate)
        self.frequency=self.pitch[point.y+step]
        self.amplitude=amp*math.pow(2,point.z+step)
        sound=sin(2*pi*self.frequency*self.duration)*self.amplitude
        return sound.astype(int16)

# A tone, 2 seconds, 44100 samples per second
X=Point(1,0,0)
SS=SoundScape(pitch)
sound = SS.generateSineWave(X)

write('440hzAtone.wav',44100,sound) # writing the sound to a file
pygame.init()
'''pygame.mixer.music.load("440hzAtone.wav")
pygame.mixer.music.play()
print pygame.mixer.get_num_channels()
'''
snd=pygame.mixer.Sound("440hzAtone.wav")
channel=snd.play()
s = int(snd.get_length())
print snd.get_num_channels()
print s
for i in range(0,s):
    if i < 2:
        channel.set_volume(0,0)
    else:
        channel.set_volume(0,0)
print snd.get_volume()

time.sleep(10)
plot(SS.duration,sound)
axis([0,0.4,15000,-15000])
show()



