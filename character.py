import Board
import server
import client
import time
import random

class Character:

    maxHP = 100

    def __init__(self, ipAddr, portNum):
        self.ipAddr = ipAddr
        self.portNum = portNum
        self.board = Board()
        self.position = self.board.get_;
        self.hp = self.maxHP
        self.direction = "east"


    def _say_stuff(self, message):
        c = client.Client(self.ipAddr, self.portNum, "Recharged",
                          False)
        c.start()
        time.sleep(2)

    def move(self, direction):
        """Gets input from the user, then moves the robot"""
        pass

    def _move_where(self):
        # returns the number of the new position
        pass

    def isAlive():
        return self.hp > 0

    def take_turn(self):
        # Ask for movement, make movement, do thing at node
        new_pos, direction = self._move_where()
        self.move(direction)
        loc_type = self.board.get_loc_type(new_pos)
        if loc_type == Location_types.START:
            pass
        elif loc_type == Location_types.END:
            pass
        elif loc_type == Location_types.RECHARGE:
            self.hp = self.maxHP
            self._say_stuff("Recharged")
            time.sleep(1)
        elif loc_type == Location_types.COFFEE:
            pass
        else:
            monsters = self.board.get_monster_at(self.position)
            result = self._initial_fight(monsters)
            if result == True:
                pass
            elif result == False:
                return False
            else:
                self._fight_loop(monsters)

    def _fight_loop(self, monsters):
        while True:
            self._say_stuff("Would you like to run or fight?")
            command = sever.wait_for_command(

    def _initial_fight(self):
        if self._fight() and self.isAlive():
            self._say_stuff("We have vanquished our foe!")
            return True
        elif not self.isAlive():
            self._say_stuff("Game over")
            return False;
        else:
            # return a truthy value that is not "True"
            return 4

    def _do_ninja(self):
        # look like a ninja:
        pass

    def _fightLoop(self):

    def _fight(self, monsters):
        alive = filter(lambda x: !x.isDead(), monsters)
        if alive:
            self._say_stuff("Ack! A monster!")
            self._do_ninja()
            died = set()
            for mon in alive:
                take_out = random.uniform(5, 100)
                mon.take_punch(take_out)
                if mon.isDead():
                    died.append(mon)
                else:
                    ouch = mon.throw_punch()
                    self.hp -= ouch
            if self.hp > 0:
                self._say_stuff("There are %d monsters left" % (len(monsters) - len(died)))
                self._say_stuff("I have %d HP left" % self.hp)
            # did we kill them all?
            return len(monsters) == len(died):
        return True
