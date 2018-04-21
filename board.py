import random
import riddles
import numpy as np
from enum import Enum

Location_types = Enum('Location_types', 'START END RECHARGE COFFEE EASY MED DIFFICULT FUN')

class Monster:

    def __init__(self, difficulty):
        self.hp = 100
        # self.difficulty = difficulty
        if difficulty == Location_types.EASY:
            self.difficulty = 10
        elif difficulty == Location_types.MED:
            self.difficulty = 25
        elif difficulty == Location_types.DIFFICULT:
            self.difficulty = 90

    def isDead(self):
        return self.hp <= 0

    def throw_punch(self):
        return int(random.uniform(0, self.difficulty))

    def take_punch(self, lost):
        self.hp -= lost
        return self.hp


class Board:

    layout = { 1 : {'east' : 2},
    2 : {'west' : 1, 'south' : 7, 'east' : 3},
    3 : {'west' : 2, 'south' : 8},
    4 : {'east' : 5},
    5 : {'west' : 4, 'south' : 10},
    6 : {'east' : 7, 'south' : 11},
    7 : {'north' : 2, 'south' : 12, 'west' : 6},
    8 : {'north' : 3},
    9 : {'east' : 10, 'south' : 14},
    10 : {'north' : 5, 'south' : 15, 'west' : 9},
    11 : {'north' : 6, 'south' : 16},
    12 : {'north' : 7, 'east' : 13},
    13 : {'west' : 12, 'east' : 14},
    14 : {'north' : 9, 'west' : 13, 'south' : 19},
    15 : {'north' : 10, 'south' : 20},
    16 : {'north' : 11, 'east' : 17},
    17 : {'south' : 22, 'west' : 16},
    18 : {'south' : 23},
    19 : {'north' : 14, 'east' : 20, 'south' : 24 },
    20 : {'north' : 15, 'west' : 19},
    21 : {'east' : 22},
    22 : {'north' : 17, 'east' : 23, 'west' : 21},
    23 : {'north' : 18, 'west' : 22},
    24 : {'north' : 19, 'east' : 25},
    25 : {'west' : 24} }

    def __init__(self):
        self._gen_locations()

    def _gen_start_end(self):
        sides = ["north", "south", "east", "west"]
        edges = [[1,2,3,4], [22,23,24,25],  [5,10,15,20], [6,11,16,21]]
        start_index = random.choice(range(len(edges)))
        if start_index % 2 == 0:
            # go back:
            end_index = start_index + 1
        else:
            # go forward
            end_index = start_index - 1
        # probably shouldn't go in this function. Oh well...
        self.end_side = sides[end_index]
        start_pos = random.choice(edges[start_index])
        end_pos = random.choice(edges[end_index])
        return start_pos, end_pos

    def member(self, lst, func):
        """ Returns the first item in the list where func returns true, else None"""
        for i in lst:
            if func(i):
                return i;
        return None;

    def find_values(self, number, positions):
        places = []
        for i in range(number):
            found = False
            while not found:
                choice = random.sample(positions, 1)[0]
                if not self.member(places, lambda x : self._next_to(x, choice)):
                    # not next to anything:
                    places.append(choice)
                    positions.remove(choice)
                    found = True;
        return places

    def _gen_locations(self):
        # pick the start and the end:
        self.start_pos, self.end_pos = self._gen_start_end()

        pos = set(range(1, 26))
        pos.remove(self.start_pos)
        pos.remove(self.end_pos)

        self.charging_stations = self.find_values(3, pos)
        pos = pos.difference(self.charging_stations)

        self.coffee_shops = self.find_values(2, pos)
        pos = pos.difference(self.coffee_shops)

        pos = list(pos)
        random.shuffle(pos)
        self.easy_monsters = []
        for i in pos[:7]:
            self.easy_monsters.append(i)
        self.med_monsters = []
        for i in pos[7:12]:
            self.med_monsters.append(i)
        self.difficult_monsters = []
        for i in pos[12:15]:
            self.difficult_monsters.append(i)
        self.fun_nodes = []
        for i in pos[15:]:
            self.fun_nodes.append(i)

        self.print_stats()

        self.monsters = {}
        self.riddles = {}
        places = {}
        places[self.end_pos] = Location_types.END
        places[self.start_pos] = Location_types.START
        # Location_types = Enum('Location_types', 'END RECHARGE COFFEE EASY MED DIFFICULT FUN')
        for n in self.easy_monsters:
            self.monsters[n] = [] # self.make_monsters(Location_types.EASY)
            places[n] = Location_types.EASY
        for n in self.med_monsters:
            self.monsters[n] = [] # self.make_monsters(Location_types.MED)
            places[n] = Location_types.MED
        for n in self.difficult_monsters:
            self.monsters[n] = [] # self.make_monsters(Location_types.DIFFICULT)
            places[n] = Location_types.DIFFICULT
        for index, n in enumerate(self.fun_nodes):
            # positions are always random, so this is okay:
            self.riddles[n] = (riddles.riddles[index], False)
            places[n] = Location_types.FUN
        for n in self.charging_stations:
            places[n] = Location_types.RECHARGE
        for n in self.coffee_shops:
            places[n] = Location_types.COFFEE

        self.places = places

    def print_stats(self):
        print("Board stats:")
        print("#############################################")
        print("Starting:\t", self.start_pos)
        print("Ending:\t", self.end_pos)
        print("Charging: ", self.charging_stations)
        print("Coffee:", self.coffee_shops)
        print("Easy:", self.easy_monsters)
        print("med:", self.med_monsters)
        print("difficult:", self.difficult_monsters)
        print("fun:", self.fun_nodes)
        print("#############################################")

    def get_new_pos(self, position, direction):
        return self.layout[position][direction]

    def make_monsters(self, difficult):
        if difficult ==  Location_types.DIFFICULT:
            num_monsters = 1
        else:
            num_monsters = int(random.uniform(2, 6))
        return [Monster(difficult) for i in range(num_monsters)]

    def _next_to(self, one, two):
        d = self.layout[one]
        return two in d.values()

    def get_available_moves(self, position):
        return self.layout[position].keys()

    def get_loc_type(self, position):
        return self.places[position]

    def get_monster_at(self, position):
        return self.monsters[position]

    def get_riddle_at(self, position):
        to_return = self.riddles[position]
        self.riddles[position] = (riddles.get_riddle_part(self.riddles[position]), True)
        return to_return

    def at_end(self, position):
        return self.end_pos == position

    def get_starting_pos(self):
        return self.start_pos;

    def get_end_side(self):
        return self.end_side

    def get_end_pos(self):
        return self.end_pos


if __name__ == "__main__":
    b = Board()
