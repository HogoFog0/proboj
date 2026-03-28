from data import *
from collections import defaultdict
from heapq import *
import random

def GetMyShades(self,world:World):
    return [world.alive_shades[i] for i in world.alive_shades if world.alive_shades[i].id == world.my_id]

def eval(objective : Person | Tombstone, shade : Shade):
    return -objective.position.manhattan_dist(shade.position) + random.random()

def singleassign(self):
    world : World = self.world
    assigned = defaultdict(int)
    heaps = defaultdict(list)
    bigheap = []
    
    if(len(self.my_shades)):
        for i in world.alive_people:
            for j in self.my_shades:
                heappush(heaps[i],(-eval(j,i),j))
            heappush(bigheap,(heappop(heaps[i]),i))

        for i in world.alive_tombstones:
            if(i.owner == self.world.my_id): continue
            for j in self.my_shades:
                heappush(heaps[i],(-eval(j,i),j))
            heappush(bigheap,(heappop(heaps[i]),i))

        while(len(bigheap)):
            cur = heappop(bigheap)
            if(assigned[cur[0][1]]):
                if(len(heaps[cur[1]])):
                    heappush(bigheap,(heappop(heaps[cur[1]]),cur[1]))
            else:
                assigned[cur[0][1]] = cur[1]
    return assigned

































