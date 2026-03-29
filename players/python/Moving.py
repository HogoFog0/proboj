from data import *
from collections import deque
from collections import defaultdict

def A_to_B(self, A, B):
    if(A==B): return None
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
            if ngb == B:
                parent[ngb] = X
                while parent[ngb] != A:
                    ngb = parent[ngb]
                return ngb
            
            # if(ngb.will_i_die_at(self.pointshades, world.my_id)): self.log(ngb)
            elif (world.map.can_move_to(self,ngb) 
                  and ngb not in dist 
                  and not (ngb in self.collisions and dist[X] == 0)):
                #   and not(ngb.will_i_die_at(self.pointshades, world.my_id) and dist[X]<3)):
                dist[ngb] = dist[X]+1
                q.append(ngb)
                parent[ngb] = X
            
            
            

        