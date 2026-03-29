#!/bin/env python
import sys
from typing import List
from data import World, Move, Person, World, Map, Shade, Tombstone, Point
from game import Game, PlayerInterface
from random import shuffle
from Moving import A_to_B
from farming import *

def GoTo(self, shade : Shade, end : Point):
    move = A_to_B(self,shade.position,end)
    if(move is not None):
        self.moves.append(Move(shade.id, move))
        self.collisions.add(move)

class Player(PlayerInterface):
    @staticmethod
    def log(*args):
        print(*args, file=sys.stderr)

    def init(self, world: World) -> None:
        Player.log("init")
        pass

    def get_turn(self, world: World) -> List[Move]:
        self.my_shades = [world.alive_shades[i] for i in world.alive_shades if world.alive_shades[i].owner == world.my_id]
        self.moves = []
        self.collisions = set()
        self.world = world
        # self.log(self.my_shades)
        assignment = singleassign(self)
        for i in assignment:
            GoTo(self, i,assignment[i].position)

        return self.moves

if __name__ == "__main__":
    game = Game(Player())
    game.run()
