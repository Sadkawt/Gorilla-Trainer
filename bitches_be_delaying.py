import math
import random

def bitches_be_custom(file, patternStr, multiplier):
    deltaTime = float(file.timingData[1])/(8*multiplier)
    totalNote = math.floor((file.timingEnd - file.timingStart)/(deltaTime*len(patternStr)))
    chord_list = []
    chord = random.sample(range(1,8), int(patternStr[-1]))
    base = [1,2,3,4,5,6,7]

    for itteration in range(totalNote):
        for chordSize in patternStr:
            if chordSize == "0":
                chord_list.append([0])
                chord = [0]
            else:
                chord = [x for x in base if x not in chord]
                if len(chord) == int(chordSize):
                    pass

                else:
                    for x in range(len(chord)-int(chordSize)):
                        chord.pop(random.randrange(len(chord)))
                chord_list.append(chord)

    index = 0
    for chord in chord_list:
        if chord == [0]:
            index += 1
        else:
            if random.choice([True, False]) == True:
                chord.reverse()
            for noteIndex in chord:
                xPos = 36 + 73*(noteIndex-1)
                time = file.timingStart + index*deltaTime
                file.lines.append("{},192,{},1,0,0:0:0:0:\n".format(xPos, time))
                index += 1
