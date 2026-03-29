#!/bin/env python
import sys
from typing import List
from data import World, Move, Person, World, Map, Shade, Tombstone, Point
from game import Game, PlayerInterface
from random import shuffle
from Moving import *
from assign import *
from utils import *
from collections import defaultdict

import time

def GoTo(self, shade : Shade, end : Point):
    move = Astar(self,shade.position,end)
    # self.log(move,shade.position,end)
    if(move is not None):
        self.moves.append(Move(shade.id, move))
        # self.log(move,move.will_i_die_at(self.pointshades,self))
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
        self.turn = 0
        self.calced = 0
        self.dists = defaultdict(dict)
        self.calceddict = dict()
        pass

    def get_turn(self, world: World) -> List[Move]:
        self.world = world
        self.turn += 1



        self.log(self.world.my_id)

        start = time.time()
        self.ememy_stones = [i for i in world.alive_tombstones if i.owner != self.world.my_id]
        self.my_stones = [i for i in world.alive_tombstones if i.owner == self.world.my_id]
        self.my_shades = [world.alive_shades[i] for i in world.alive_shades if world.alive_shades[i].owner == world.my_id]
        self.enemy_shades = [world.alive_shades[i] for i in world.alive_shades if world.alive_shades[i].owner != world.my_id]
        # self.log(world.alive_shades)
        self.pointshades = dict()
        for i in world.alive_shades:
            this = world.alive_shades[i]
            self.pointshades[this.position] = this

        self.moves = []
        self.collisions = set()
        self.blocked = set()
        self.blocked.add(i for i in self.my_stones)
        self.job = dict()
        self.closestenemy = dict()

        ClearCaches(self)
        self.calclimit = 10

        # self.log(self.my_shades)
        assignpeople(self)
        assigndefence(self)
        assigntombs(self)
        if(not len(self.enemy_stones)):
            try:
                assignenemy(self)
            except:
                self.log("lolol")
                pass
        # self.log(self.job)
        for i in self.my_shades:
            if(i not in self.job):
                self.collisions.add(i.position)
                self.log(i)
            else:
                try:
                    if(i.position == self.job[i].position):
                        self.collisions.add(i.position)
                        self.log(i)
                except:
                    pass

        for i in self.job:
            try:
                GoTo(self, i,self.job[i].position)
            except:
                GoTo(self, i,self.job[i])

        #---Fear Counter---
        # CalcFearMap(self)
        # CalcMaxEnemyFearMap(self)
        # self.log(self.moves)

        end = time.time()

        elapsed = end-start

        self.log("TIME")
        self.log(f"Elapsed time: {elapsed:.3f} seconds")

        return self.moves

if __name__ == "__main__":
    game = Game(Player())
    game.run()
