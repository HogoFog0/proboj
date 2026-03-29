from data import *
from collections import defaultdict
from heapq import *
import random


def eval(objective : Person | Tombstone, shade : Shade): #
    return 100-objective.position.manhattan_dist(shade.position) + random.random()

def assignpeople(self):

    world : World = self.world
    heaps = defaultdict(list)
    bigheap = []
    
    if(len(self.my_shades)):
        for i in world.alive_people:
            for j in self.my_shades:
                if j in self.job: continue
                heappush(heaps[i],(-eval(i,j),j))
            heappush(bigheap,(heappop(heaps[i]),i))

        while(len(bigheap)):

            cur = heappop(bigheap)
            if -cur[0][0] < 0:
                break
            if(cur[0][1] in self.job):
                if(len(heaps[cur[1]])):
                    heappush(bigheap,(heappop(heaps[cur[1]]),cur[1]))
            else:
                self.job[cur[0][1]] = cur[1]


def assigntombs(self):
        world : World = self.world
        for i in self.my_shades:
            i : Shade
            if(i not in self.job):
                cur = [None,float('inf')]
                for j in world.alive_tombstones:
                    j : Tombstone
                    if(j.owner == self.world.my_id): continue
                    val = eval(j,i)
                    if(val < cur[1]):
                        cur[1] = val
                        cur[0] = j
                if(cur[0] is not None):
                    self.job[i] = cur[0]





























