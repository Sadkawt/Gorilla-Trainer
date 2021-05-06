import math
import random

def bitches_be_chordjacking(file, patternStr, multiplier):
    deltaTime = float(file.timingData[1])/(2*multiplier)
    totalNote = math.floor((file.timingEnd - file.timingStart)/(deltaTime*len(patternStr)))
    chord_list = []

    for itteration in range(totalNote):
        for chordSize in patternStr:
            if chordSize == "0":
                chord_list.append([0])
                chord = [0]
            else:
                chord = random.sample(range(1,8), int(chordSize))
                chord_list.append(chord)


    index = 0
    for chord in chord_list:
        if chord == [0]:
            index += 1
        else:
            for noteIndex in chord:
                xPos = 36 + 73*(noteIndex-1)
                time = file.timingStart + index*deltaTime
                file.lines.append("{},192,{},1,0,0:0:0:0:\n".format(xPos, time))
            index += 1
