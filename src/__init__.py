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

__author__ = 'luminous'

#class for generating a random point in real world
class Point:
    def __init__(self,step=10,seed=0):
        random.seed(seed)
        low=-1*step
        high=step
        self.x=random.randint(low,high)
        self.y=random.randint(low,high)
        self.z=random.randint(low,high)


class SoundScape:
    def __init__(self,seed



class DataItem:
    classlabel=None
    feature=[]
    def __init__(self, classlabel, feature):        # Container for data feature vectors, class labels for each
        try:
            self.classlabel = classlabel                # feature vector and functions to read and write data.
            self.feature = numpy.array(feature,dtype='f')         # Use constructor and destructor to initialize and clear data.
        except:
            print "exception in dataitem initialization",sys.exc_info()
class DataSet:
    Data=[]
    def __init__(self,data):                        #Assume that the data file is plain text with each row
        self.Data=data
    def readData(self, filename,classposition):     #containing the class label followed by the features,
        os.path.relpath(filename,os.curdir)         #separated by blank spaces.
        try:
            with open(filename, 'rb') as f:
                reader = csv.reader(f)
                for row in reader:
                    c_label=row.pop(classposition)
                    data_item=DataItem(c_label,row)
                    self.Data.append(data_item)
            return True
        except:
            print "exception in read data",sys.exc_info()
            return False

    def writeData(self, filename):
        try:
            os.path.relpath(filename,os.curdir)
            File_Write = open(filename, "w+")

            for d_item in self.Data:
                row=None
                row=str(d_item.classlabel)
                for pnt in d_item.feature:
                    row+=','+str(pnt)
                row+="\n"
                File_Write.write(row)
            File_Write.close()
            return True
        except:
            print "exception in write data"
            return False

def splitDataset(Dataset_Complete,folds=2,seed=0):          # Partition 'complete' dataset randomly into 'folds' parts and
    random.seed(seed)                                       # returns a pointer to an array of pointers to the partial datasets.
    random.shuffle(Dataset_Complete.Data)                   # seed is an argument to random number generator. The function can
    partial_sets=[]
    chunk_len=len(Dataset_Complete.Data) / folds
    for i in range(folds):                                  # be used to divide data for training, testing and cross validation.
		start = i * chunk_len                               # This need not replicate the data.
		end = (i + 1) * chunk_len
		split_dataset = DataSet(Dataset_Complete.Data[start:end])
		partial_sets.append(split_dataset)
    return partial_sets

def mergeDatasets(toMerge,numDatasets,indicesToMerge):      # Merge the datasets indexed by indicesToMerge in the toMerge list and return a
     merged_set=DataSet([])                                 # single dataset. This need not replicate the data.
     for i in range(numDatasets):
        merge_index=int(indicesToMerge[i])
        merged_set.Data+=toMerge[merge_index].Data
     return merged_set