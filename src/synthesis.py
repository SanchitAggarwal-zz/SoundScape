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
from numpy import linspace,sin,pi

__author__ = 'luminous'

#initial standard 13 tones from A-440 to A-880 increasing pitch
pitch=[440,466,494,523,554,587,622,659,698,740,784,831,880]

#class for generating a random point in real world  #call with initial values
#For only X Point(1,0,0)
#For only Y Point(0,1,0)
#For only Z Point(0,0,1)
class Point:
    def __init__(self,x=1,y=1,z=1,step=5):
        """
        :param x: X coordinate for channel and duration
        :param y: Y coordinate for pitch
        :param z: Z coordinate for amplitude
        :param step:scale size for each coordinate
        """
        low=-1*step
        high=step
        self.x=random.randint(low,high)*x
        self.y=random.randint(low,high)*y
        self.z=random.randint(low,high)*z

class SoundScape:
    def __init__(self,pitch,channel=2,rate=44100):

        """
        :param pitch: the standard pitch for sound
        :param channel: the channel either Left or Right
        :param rate: No of samples per seconds
        """
        self.pitch=pitch
        self.channel=channel
        self.rate=rate

    def generateSineWave(self, point,amp=1000,step=5):
        """
        :param amp: amplitude of the sound signal,initial vale 1000 which varies with depth
        :param step: scale size for each coordinate
        :param point: sine wave corresponding to the 3D point
        """
        self.length=math.fabs(point.x)
        self.duration=linspace(0,self.length,self.length*self.rate)
        self.frequency=self.pitch[point.y+step]
        self.amplitude=amp*math.pow(2,-1*point.z)
        sound=sin(2*pi*self.frequency*self.duration)*self.amplitude
        return sound