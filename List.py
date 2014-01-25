import random
import collections

from File import *

def getDutyMap():
    duty = getFromFile(suckersFile)
    if duty == False:
        duty = generateDutyMap()
    duty = deserialize(duty)
    duty = collections.OrderedDict(sorted(duty.items()))
    return duty

def generateDutyMap():
    dutyMap = {'kitchen': createRandomList(),
            'bathroom': createRandomList(),
            'toilet': createRandomList() } 
    putInFile(serialize(dutyMap), suckersFile)
    return dutyMap
    
def createRandomList():
    list = ["Person 1", "Person 2", "Person 3", "Person 4"]
    random.shuffle(list)
    return list

def nextSucker(duty, dutyMap):
    if duty in dutyMap:
        list = dutyMap[duty]
        lastSucker = list.pop(0)
        list.append(lastSucker)
        result = putInFile(serialize(dutyMap), suckersFile)
        return result
    else:
        raise Error("Duty not found in dictionary")

def getSucker(duty, dutyMap):
    if duty in dutyMap:
        list = dutyMap[duty]
        return list[0]
    else:
        raise Error("Duty not found in dictionary")
