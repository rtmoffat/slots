import pygame as pg
import random

random.seed()
pg.sprite

#images=['cherry_img','bar_img','lemon_img','apple_img','orange_img']
#values=['cherry','bar','lemon','apple','orange']
images={'cherry_img':'cherry','bar_img':'bar','lemon_img':'lemon','apple_img':'apple','orange_img':'orange'}

class machine:
    reelset=None
    def __init__(self,reelset):
        self.reelset=reelset
    def pull(self):
        for reel in self.reelset.reels:
            print(reel.spin().image)
    
class reelset:
    reels=None
    def __init__(self):
        self.reels=[]
    def addReel(self,reel):
        self.reels.append(reel)

class reel:
    slots=None
    def __init__(self):
        self.slots=[]
    def addSlot(self,slot):
        self.slots.append(slot)
    def spin(self):
        return random.choice(self.slots)

class slot:
    image=None
    value=None
    def __init__(self,image,value):
        self.image=image
        self.value=value


def newReelSet(numReels,reelSize):
    """Returns a reelset with numreels and reelsize.
    
    Parameters:
    
    numReels=The number of reels to create for the reelset
    
    reelSize=The number of slots to create for each reel
    """
    #Create a new reelset and populate it
    rs=reelset()
    for x in range(1,(numReels+1)):
        myReel=reel()
        for y in range(1,reelSize+1):
            image=random.choice(list(images.keys()))
            mySlot=slot(image,images[image])
            myReel.addSlot(mySlot)
        print(x)
        rs.addReel(myReel)
    return rs

myRs=newReelSet(3,5)
myMachine=machine(myRs)
myMachine.pull()
print(len(myRs.reels))


