import board
import server
import client
import riddles
import time
import random
from dist_funcs import get_hint
from enum import Enum
from PyQt5.QtCore import QObject, pyqtSignal

class Character(QObject):

    maxHP = 100
    changed_location = pyqtSignal(board.Location_types, name='changed_location')

    def __init__(self,ipAddr, portNum, my_board, controller, parent=None):
        QObject.__init__(self, parent)
        self.ipAddr = ipAddr
        self.portNum = portNum
        self.my_board = my_board
        self.position = self.my_board.get_starting_pos()
        print("Bot position: ",self.position)
        self.hp = self.maxHP
        self.direction = "east"
        self.controller = controller

    def _say_stuff(self, message):
        client.say_stuff(self.ipAddr, self.portNum, message)

    def get_direction_number(self, direction):
        if(direction == "north"):
            return 1
        elif(direction == "east"):
            return 2
        elif(direction == "south"):
            return 3
        elif(direction == "west"):
            return 4
        else:
            return "invalid direction, this should break"

    def turn(self, currDirection, newDirection):
        currDirection = self.get_direction_number(currDirection)
        newDirection = self.get_direction_number(newDirection)

        if(currDirection == newDirection):
            return 0
        else:
            return currDirection - newDirection

    def move(self, new_pos, direction):
        """Gets input from the user, then moves the robot"""

        # robot stuff!
        to_turn = self.turn(self.direction, direction)
        for i in range(abs(to_turn)):
            if(to_turn < 0):
                self.controller.turn_clockwise()
            elif(to_turn > 0):
                self.controller.turn_counterClockWise()
            time.sleep(.25)

        self.controller.move_forward(2) #2 is the speed
        time.sleep(1.5)
        self.controller.stop_moving()
        self.position = new_pos
        self.direction = direction
        print("We moved ", direction)

    def _move_where(self):
        foundDirection = False
        while not foundDirection:
            # returns the number of the new position
            prompt_string = "Where would you like to go? Options are: "
            for d in self.my_board.get_available_moves(self.position):
                prompt_string += " " + d + ",";

            self._say_stuff(prompt_string)
            direction = server.get_command(self.ipAddr, self.portNum).lower()
            print("Direction to go: ", direction)
            foundDirection = direction in self.my_board.get_available_moves(self.position)

        new_pos = self.my_board.get_new_pos(self.position, direction)
        print(new_pos, direction)
        return new_pos, direction

    def isAlive(self):
        return self.hp > 0

    def take_turn(self):
        # Ask for movement, make movement, do thing at node
        new_pos, direction = self._move_where()
        self.move(new_pos, direction)
        print("Now at position: ", new_pos)
        loc_type = self.my_board.get_loc_type(new_pos)
        self.changed_location.emit(loc_type)
        if loc_type == board.Location_types.START:
            self._say_stuff("You are at the starting position")
            return True
        elif loc_type == board.Location_types.END:
            print("At end")
            return True
        elif loc_type == board.Location_types.RECHARGE:
            self.hp = self.maxHP
            self._say_stuff("Beep boop beep. I'm feeling nice and Recharged")
            time.sleep(3)
            return True
        elif loc_type == board.Location_types.COFFEE:
            print("At coffee shop")
            msg_string = "The ending spot is on the " + self.my_board.get_end_side() + " side."
            msg_string += "You must go " + get_hint(self.my_board, self.position, self.my_board.get_end_pos()) + "from here!"
            print(msg_string)
            self._say_stuff(msg_string)
            time.sleep(3)
            return True
        elif loc_type == board.Location_types.FUN:
            riddle = self.my_board.get_riddle_at(self.position)
            if not riddle[1]:
                riddles.play_riddle(self.ipAddr, self.portNum, riddle[0])
            else:
                self._say_stuff("A riddle was solved here. It was: " + riddles.get_riddle_part(riddle[0]))
        else:
            monsters = self.my_board.get_monster_at(self.position)
            result = self._initial_fight(monsters)
            if result == True:
                pass
            elif result == False:
                return False
            else:
                return self._fight_loop(monsters)

    def _fight_loop(self, monsters):
        aliveFlag = 4
        while aliveFlag == 4:
            self._say_stuff("Would you like to run or fight?")
            command = server.get_command(self.ipAddr, self.portNum)
            if command == "fight":
                aliveFlag = self._initial_fight(monsters)
            else:
                roll = int(random.uniform(0, 4))
                if roll == 1:
                    self._say_stuff("Egad! I can't escape!")
                    for i in range(2):
                        self.controller.move_head_left()
                        time.sleep(.5)
                        self.controller.move_head_right()
                        self.controller.move_head_right()
                        time.sleep(.5)
                        self.controller.move_head_left()
                    self.controller.reset_pos()
                    aliveFlag = self._initial_fight(monsters)
                else:
                    self.goto_random_spot()
                    aliveFlag = True
        return aliveFlag

    def _initial_fight(self, monsters):
        if self._fight(monsters) and self.isAlive():
            self._say_stuff("We have vanquished our foe!")
            self.controller.move_shoulder_up()
            self.controller.move_shoulder_up()
            self.controller.move_shoulder_up2()
            self.controller.move_shoulder_up2()
            self.controller.twist_hand_left()
            self.controller.twist_hand_left()
            self.controller.twist_hand_left2()
            self.controller.twist_hand_left2()
            time.sleep(1)
            self.controller.reset_pos()
            return True
        elif not self.isAlive():
            self._say_stuff("Game over")
            self.controller.move_arms_down()
            self.controller.move_arms_down2()
            self.controller.move_head_down()
            return False;
        else:
            # return a truthy value that is not "True"
            return 4

    def goto_random_spot(self):
        choices = list(self.my_board.get_available_moves(self.position))
        to_go = random.choice(choices)
        new_pos = self.my_board.get_new_pos(self.position, to_go)
        self.move(new_pos, to_go)

    def _do_ninja(self):
        # look like a ninja:
        print("doing ninja things")
        self.controller.move_waist_left()
        self.karate_chop()
        self.controller.move_waist_right()
        self.controller.move_waist_right()
        self.karate_chop()
        self.controller.reset_pos()

    def karate_chop(self):
        for i in range(3):
            self.controller.move_shoulder_up()
            self.controller.move_arms_up()
            self.controller.move_shoulder_down2()
            self.controller.move_arms_down2()
            time.sleep(.5)
            self.controller.move_shoulder_up2()
            self.controller.move_arms_up2()
            self.controller.move_shoulder_down()
            self.controller.move_arms_down()
            time.sleep(.5)

    def _fight(self, monsters):
        alive = list(filter(lambda x: not x.isDead(), monsters))
        if alive:
            self._say_stuff(random.choice(self._fight.exclaimations))
            self._do_ninja()
            # died = set()
            deadCount = 0
            for mon in alive:
                take_out = int(random.uniform(25, 100))
                mon.take_punch(take_out)
                if mon.isDead():
                    deadCount += 1
                else:
                    ouch = mon.throw_punch()
                    self.hp -= ouch
            if self.hp > 0:
                left = (len(alive) - deadCount)
                if left == 1:
                    self._say_stuff("There is 1 monster remaining")
                else:
                    self._say_stuff("There are %d monsters left" % left)
                self._say_stuff("I have %d HP left" % self.hp)
            # did we kill them all?
            return len(alive) == deadCount
        return True

    _fight.exclaimations = ["Ack! Monsters!", "My Heavens! Its a troll!", "Oh Crap!", "Mon Dieu!"]
