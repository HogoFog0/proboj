#!/bin/env python
import sys
from typing import List
from data import World, Move, Person, World, Map, Shade, Tombstone, Point
from game import Game, PlayerInterface
from random import shuffle
from Moving import *
from assign import *
from utils import *

def GoTo(self, shade : Shade, end : Point):
    move = A_to_B(self,shade.position,end)
    if(move is not None):
        self.moves.append(Move(shade.id, move))
        self.collisions.add(move)
    else:
        self.collisions.add(shade.position)
        self.log("No path found")

class Player(PlayerInterface):
    @staticmethod
    def log(*args):
        print(*args, file=sys.stderr)

    def init(self, world: World) -> None:
        Player.log("init")
        pass

    def get_turn(self, world: World) -> List[Move]:
        self.world = world

        self.ememy_stones = [i for i in world.alive_tombstones if i.owner != self.world.my_id]
        self.my_stones = [i for i in world.alive_tombstones if i.owner == self.world.my_id]
        self.my_shades = [world.alive_shades[i] for i in world.alive_shades if world.alive_shades[i].id == world.my_id]

        self.moves = []
        self.collisions = set()
        self.blocked = set()
        self.blocked.add(i for i in self.my_stones)
        self.job = dict()

        for i in range(5000):
            for i in world.alive_shades:
                world.alive_shades[i].will_i_die(world.alive_shades)

        # self.log(self.my_shades)
        assignpeople(self)
        assigntombs(self)
        for i in self.my_shades:
            if(i not in self.job):
                self.collisions.add(i.position)
                self.log(i)

        for i in self.job:
            GoTo(self, i,self.job[i].position)

        #---Fear Counter---
        # CalcFearMap(self)
        # CalcMaxEnemyFearMap(self)

        return self.moves

if __name__ == "__main__":
    game = Game(Player())
    game.run()
