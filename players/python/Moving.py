from data import *
from collections import deque
from collections import defaultdict

def A_to_B(self, world: World, A, B):
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
                parent[B] = X
                move = parent[B]
                while parent[move] != A:
                    move = parent[move]
                return move
            
            elif world.map.can_move_to(ngb) and ngb not in dist:
                dist[ngb] = dist[X]+1
                q.append(ngb)
                parent[ngb] = X
            
            
            

        