from data import *

# def CalcFearMap(self):
#     world : World = self.world
#     self.fear_map = {}
#     for y in range(world.map.height):
#         for x in range(world.map.width):
#             self.fear_map[Point(x, y)] = Point(x, y).get_fear_at(world.alive_shades, PlayerID)
#    #self.log(self.fear_map)


# def CalcMaxEnemyFearMap(self):
#     world : World = self.world
#     self.max_enemy_fear_map = {}
#     for y in range(world.map.height):
#         for x in range(world.map.width):
#             self.max_enemy_fear_map[Point(x,y)] = min(Point(x, y).get_enemy_fears_at(world.alive_shades, PlayerID).values(), default=float("inf"))
#    #self.log(self.fear_map)

def ClearCaches(self):
    Point.get_fear_at.clear_cache()
    Point.get_fear_atplus.clear_cache()
    Point.get_enemy_fears_at.clear_cache()
    Shade.get_fear.clear_cache()
    Shade.get_enemy_fears.clear_cache()
    Shade.will_i_die.clear_cache()