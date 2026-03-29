from data import *

def CalcMyShades(self):
    world : World = self.world
    self.my_shades = [world.alive_shades[i] for i in world.alive_shades if world.alive_shades[i].id == world.my_id]
