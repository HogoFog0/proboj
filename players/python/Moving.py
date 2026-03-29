from data import *
from collections import deque
from collections import defaultdict
from heapq import *

def A_to_B(self, A, B):
    if(A==B): return None
    world : World = self.world
    q = deque()
    q.append(A)
    dist = defaultdict(int)
    parent = {}
    dist[A] = 0
    
    shade_positions = self.pointshades

    friends = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if(A+Point(dx,dy) in shade_positions and shade_positions[A+Point(dx,dy)].owner == self.world.my_id):
                friends+=1
    self.log(friends)
    while len(q):
        X = q.popleft()
        neighbours = X.get_neighbouring()

        for ngb in neighbours: 
            if ngb == B:
                parent[ngb] = X
                while parent[ngb] != A:
                    ngb = parent[ngb]
                return ngb
            
            # if(ngb.will_i_die_at(self.pointshades, world.my_id)): self.log(ngb)
            elif (world.map.can_move_to(self,ngb) 
                  and ngb not in dist 
                  and not (ngb in self.collisions and dist[X] == 0)
                  and not(ngb.will_i_die_at(self.pointshades, self,friends) and dist[X]<3)):
                dist[ngb] = dist[X]+1
                q.append(ngb)
                parent[ngb] = X

def Astar(self, A, B):
    if(A==B): return None
    world : World = self.world
    q = []
    heappush(q,(A.manhattan_dist(B),A))
    dist = defaultdict(lambda : float('inf'))
    parent = {}
    dist[A] = 0
    
    shade_positions = self.pointshades

    friends = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if(A+Point(dx,dy) in shade_positions and shade_positions[A+Point(dx,dy)].owner == self.world.my_id):
                friends+=1
    self.log(friends)
    while len(q):
        guess,X = heappop(q)
        neighbours = X.get_neighbouring()

        for ngb in neighbours: 
            if ngb == B:
                parent[ngb] = X
                while parent[ngb] != A:
                    ngb = parent[ngb]
                return ngb
            
            # if(ngb.will_i_die_at(self.pointshades, world.my_id)): self.log(ngb)
            elif (world.map.can_move_to(self,ngb) 
                  and dist[ngb] > dist[X]+1 
                  and not (ngb in self.collisions and dist[X] == 0)
                  and not(ngb.will_i_die_at(self.pointshades, self,friends) and dist[X]<3)):
                dist[ngb] = dist[X]+1
                heappush(q,(ngb.manhattan_dist(B),ngb))
                parent[ngb] = X
            


def BFS(self, A):
    world : World = self.world
    q = deque()
    q.append(A)
    dist = defaultdict(int)
    parent = {}
    dist[A] = 0
    
    while len(q):
        X = q.popleft()
        neighbours = X.get_neighbouring()

        for ngb in neighbours: 
            # if(ngb.will_i_die_at(self.pointshades, world.my_id)): self.log(ngb)
            if (world.map.can_move_to(self,ngb) 
                  and ngb not in dist 
                  and not (ngb in self.collisions and dist[X] == 0)):
                #   and not(ngb.will_i_die_at(self.pointshades, world.my_id) and dist[X]<3)):
                dist[ngb] = dist[X]+1
                q.append(ngb)
                parent[ngb] = X
    return dist

        