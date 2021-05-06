import math
import random
from bitches_be_chordstreaming import bitches_be_chordstreaming
from bitches_be_delaying import bitches_be_custom
from bitches_be_chordjacking import bitches_be_chordjacking

class File(object):
    def __init__(self, path):
        f = open(path, "r", errors='ignore')
        self.lines = f.readlines()
        self.path = path
        self.timingData = None
        self.timingStart = 0
        self.timingEnd = 0
        self.diffIndex = 0
        self.artist = None
        self.title = None
        self.mapper = None


        for x in range(len(self.lines)):
            if self.lines[x] == "[General]\n":
                self.lines[x+7] = "Mode: 3\n"

            elif self.lines[x] == "[Metadata]\n":
                self.title = self.lines[x+1].split(":")[-1].strip("\n")
                self.artist = self.lines[x+3].split(":")[-1].strip("\n")
                self.mapper = self.lines[x+5].split(":")[-1].strip("\n")
                self.diffIndex = x+6
                #self.lines[x+6] = "Version:AutoMap type:{}\n".format(diffName)

            elif self.lines[x] == "[Difficulty]\n":
                self.lines[x+2] = "CircleSize:7\n"

            elif self.lines[x] == "[TimingPoints]\n":
                self.timingData = self.lines[x+1].split(",")


            elif self.lines[x] == "[HitObjects]\n":
                self.timingStart = float(self.lines[x+1].split(",")[2])
                self.timingEnd = float(self.lines[-1].split(",")[2])
                self.lines = self.lines[:x+1]
                break


    def save(self, path):
        f = open(path, "w")
        f.writelines(self.lines)
        f.close()
