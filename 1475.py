#개행문자가 아니면 stdin.readline()

import sys
class frequency:
    def __init__(self, roomNumber):
        self.freqSet = set(roomNumber)
        self.freqDict = {}
        for i in self.freqSet:
            self.freqDict[i] = 0
        for i in roomNumber:
            self.freqDict[i] += 1
        if (('6' in self.freqDict.keys()) & ('9' in self.freqDict.keys())):
            self.freqDict['9'] += self.freqDict['6']
            del self.freqDict['6']

    def getSticker(self):
        counter = 0
        while(1):
            for i in self.freqDict.keys():
                self.freqDict[i] -= 1
                if i == '9':
                    self.freqDict[i] -= 1
            counter += 1
            
            if ( max(self.freqDict.values()) <=0 ):
                break
        return counter


if __name__ == "__main__":
    roomNumber = sys.stdin.readline()
    x = frequency(roomNumber).getSticker()
    print(x)
