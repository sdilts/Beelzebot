import random
import numpy as np

class Board:
    layout =   m = { 1 : {'east' : 2},
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
    12 : {'north' : 7},
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
        self.end_pos = 2

    def _gen_start_end(self):
        edges = [[1,2,3,4], [25,24,23,22],  [5,10,15,20], [21,16,11,6]]
        start_index = random.sample(range(len(edges)), 1)[0]
        if start_index % 2 == 0:
            # go back:
            end_index = start_index + 1
        else:
            # go forward
            end_index = start_index - 1
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

        charging_stations = self.find_values(3, pos)
        pos = pos.difference(charging_stations)

        coffee_shops = self.find_values(2, pos)
        pos = pos.difference(coffee_shops)

        pos = list(pos)
        random.shuffle(pos)
        easy_monsters = []
        for i in pos[:7]:
            easy_monsters.append(i)
        med_monsters = []
        for i in pos[7:12]:
            med_monsters.append(i)
        difficult_monsters = []
        for i in pos[12:15]:
            difficult_monsters.append(i)
        fun_nodes = []
        for i in pos[15:]:
            fun_nodes.append(i)

        print("Starting:\t", self.start_pos)
        print("Ending:\t", self.end_pos)
        print("Charging: ", charging_stations)
        print("Coffee:", coffee_shops)
        print("Easy:", easy_monsters)
        print("med:", med_monsters)
        print("difficult:", difficult_monsters)
        print("fun:", fun_nodes)


    def _next_to(self, one, two):
        d = self.layout[one]
        return two in d.values()

    def get_available(self, position):
        return self.layout[position].keys()

    def get_action(self, position):
        pass

    def get_starting_pos(self):
        return self.start_pos;

    def at_end_p(self, cur_pos):
        return cur_pos == self.end_pos;


b = Board()
