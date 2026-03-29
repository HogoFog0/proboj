from data import *
from collections import defaultdict
from heapq import *
from Moving import *
import random


def eval(self,objective : Person | Tombstone, shade : Shade): #
    if(shade.position not in self.dists[objective]): self.dists[objective.position][shade.position] = objective.position.manhattan_dist(shade.position)
    if self.closestenemak[objective] < self.dists[objective.position][shade.position]:
        res = 0
    else:
        res = 100-self.dists[objective.position][shade.position]
    return res - random.random()

def eval2(self,objective : Point, shade : Shade): #
    if(shade.position not in self.dists[objective]): self.dists[objective][shade.position] = objective.manhattan_dist(shade.position)
    res = 100-self.dists[objective][shade.position]
    return res - random.random()

def calcclosestenemy(self,objective : Person | Tombstone):
    mn = float('inf')
    for o in self.enemy_shades:
        if(o.position not in self.dists[objective]): self.dists[objective.position][o.position] = objective.position.manhattan_dist(o.position)
        cur = self.dists[objective.position][o.position]
        if cur<mn:
                mn = cur
    self.closestenemak[objective] = mn


def assignpeople(self):

    world : World = self.world
    heaps = defaultdict(list)
    bigheap = []
    self.closestenemak = dict()
    
    if(len(self.my_shades)):
        for i in world.alive_people:
            calcclosestenemy(self,i)
            if i.position not in self.calceddict and self.calclimit:
                self.calceddict[i.position] = 1
                self.dists[i.position] = BFS(self,i.position)
                self.calclimit-=1
            for j in self.my_shades:
                if j in self.job: continue
                heappush(heaps[i],(-eval(self,i,j),j))
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
                    val = j.position.manhattan_dist(i.position)
                    if(val < cur[1]):
                        cur[1] = val
                        cur[0] = j
                if(cur[0] is not None):
                    self.job[i] = cur[0]

def assigndefence(self):
    world : World = self.world
    heaps = defaultdict(list)
    bigheap = []
    
    if(len(self.my_shades)):
        for x in self.my_stones:
            for i in [x.position+Point(1,0),x.position+Point(-1,0)]:
                if self.world.map.can_move_to(self,i):
                    for j in self.my_shades:
                        if j in self.job: continue
                        heappush(heaps[i],(-eval2(self,i,j),j))
                    if(len(heaps[i])) :heappush(bigheap,(heappop(heaps[i]),i))

                while(len(bigheap)):

                    cur = heappop(bigheap)
                    if -cur[0][0] < 0:
                        break
                    if(cur[0][1] in self.job):
                        if(len(heaps[cur[1]])):
                            heappush(bigheap,(heappop(heaps[cur[1]]),cur[1]))
                    else:
                        self.job[cur[0][1]] = cur[1]

def assignenemy(self):
    world : World = self.world
    for i in self.my_shades:
        i : Shade
        if(i not in self.job):
            cur = [None,float('inf')]
            for j in world.alive_shades:
                j : Shade
                if(j.owner == self.world.my_id): continue
                val = j.position.manhattan_dist(i.position)
                if(val < cur[1]):
                    cur[1] = val
                    cur[0] = j
            if(cur[0] is not None):
                self.job[i] = cur[0]