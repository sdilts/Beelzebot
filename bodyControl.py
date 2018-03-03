import Maestro as ma
import time

class RobotController:
    head_v_increment = 1
    head_h_increment = 1
    waist_increment = 1

    servo_left_bound = 4100
    servo_right_bound = 7900

    head_v_channel = 4
    head_h_channel = 3
    waist_channel = 0
    turn_channel = 2
    move_channel = 1

    waist_increment = int((servo_right_bound - servo_left_bound) / 3)
    head_v_increment = int((servo_right_bound - servo_left_bound) / 5)
    head_h_increment = int((servo_right_bound - servo_left_bound) / 5)

    max_backward_speed = 6700
    min_backward_speed = 7300

    min_forward_speed = 17600
    max_forward_speed = 18000

    head_v_pos = 6000
    head_h_pos = 6000
    waist_pos = 6000

    def __init__(self):
        self.controller = ma.Controller()
        self.controller.setAccel(self.head_v_channel, 8)
        self.controller.setAccel(self.head_h_channel, 8)
        self.controller.setAccel(self.waist_channel, 8)
        self.controller.setAccel(self.move_channel, 1)
        self.controller.setSpeed(self.turn_channel, 0)

    def clean_up():
        pass

    def stop(self):
        self.controller.setTarget(self.move_channel, 0)

    def forward(self):
        self.controller.setSpeed(self.move_channel, 1)
        self.controller.setTarget(self.move_channel, 7000)
        for i in range(10):
            self.controller.setSpeed(self.move_channel, 2)
            self.controller.setTarget(self.move_channel, 8000)

    def correct_servo_bounds(self, number):
        if(number > self.servo_right_bound):
            return self.servo_right_bound
        elif(number < self.servo_left_bound):
            return self.servo_left_bound
        else:
            return number

    def reset_pos(self):
        self.head_v_pos = 6000
        self.head_h_pos = 6000
        self.waist_pos = 6000
        #set initial values
        self.controller.setTarget(self.head_v_channel, self.head_v_pos)
        self.controller.setTarget(self.head_h_channel, self.head_h_pos)
        self.controller.setTarget(self.waist_channel, self.waist_pos)
        pass

    def move_head_up(self):
        self.head_v_pos = self.move_servo(self.head_v_pos, self.head_v_increment, self.head_v_channel)
        pass

    def move_head_down(self):
        self.head_v_pos = self.move_servo(self.head_v_pos, -self.head_v_increment, self.head_v_channel)
        pass

    def move_head_left(self):
        self.head_h_pos = self.move_servo(self.head_h_pos, self.head_h_increment, self.head_h_channel)
        pass

    def move_head_right(self):
        self.head_h_pos = self.move_servo(self.head_h_pos, -self.head_h_increment, self.head_h_channel)
        pass

    def move_waist_left(self):
        self.waist_pos = self.move_servo(self.waist_pos, self.waist_increment, self.waist_channel)

    def move_waist_right(self):
        self.waist_pos = self.move_servo(self.waist_pos, -self.waist_increment, self.waist_channel)


    def move_servo(self,oldPos, change, channel):
        newPos = oldPos + change
        newPos = self.correct_servo_bounds(newPos)
        self.controller.setTarget(channel, newPos)
        return newPos


    # scale from -3 to positive 3, 0 = not moving
    moveScale = 0
    # index, actual speed
    speedTable = {3 : 5000, 2 : 5300, 1 : 5500, 0 : 6000, -1 : 6500, -2 : 6700, -3 : 7000 }
    speed_inc = 100

    def setSpeed(self,newSpeed):
        step = self.speed_inc
        if self.moveScale < newSpeed:
            step = step*(-1)

        for val in range(self.speedTable[self.moveScale], self.speedTable[newSpeed], step):
            self.controller.setTarget(1,val)
            # print("Setting target to: ", val)
            time.sleep(.01)
        # time.sleep(.5)
        self.moveScale = newSpeed
        print("moveScale is now: ", self.moveScale)

    def move_forward(speed):
        self.setSpeed(speed)

    # speed is absolute
    def move_backwards(speed):
        self.setSpeed(-speed)

    def ramp_forward(self):
        if not self.moveScale == 3:
            self.setSpeed(self.moveScale + 1)
        pass

    def ramp_backward(self):
        if not self.moveScale == -3:
            self.setSpeed(self.moveScale - 1)

    def stop_moving(self):
        #print("I'm a gunna stop moving")
        #print("moveScale is: ", self.moveScale)
        newSpeed = self.moveScale
        while(self.moveScale != 0):
            if self.moveScale > 0:
                newSpeed -= 1
            elif self.moveScale < 0:
                newSpeed += 1
            self.setSpeed(newSpeed)

    # might need mutex for this?
    isTurning = False
    turn_neutral = 6000
    turn_clock = 7500
    turn_counter_clock = 4500


    def turn_clockwise(self):
        # make sure that we are not moving:
        self.stop_moving()
        if self.moveScale == 0 and not self.isTurning:
            self.isTurning = True
            #TODO A THING
            # set turn "right" first:
            self.controller.setAccel(1,0)
            self.controller.setTarget(2,self.turn_clock)
            self.controller.setTarget(1, self.speedTable[2])
            time.sleep(.5)
            self.controller.setTarget(2,self.turn_neutral)
            self.controller.setTarget(1, self.speedTable[0])
            self.controller.setAccel(1,1)
         #   print("Turning Clockwise")
            self.isTurning = False

    def turn_coutnerClockWise(self):    
        self.stop_moving()
        if self.moveScale == 0 and not self.isTurning:
            self.isTurning = True
            self.controller.setAccel(1,0)
            self.controller.setTarget(2,self.turn_counter_clock)
            self.controller.setTarget(1, self.speedTable[1])
            time.sleep(.5)
            
            self.controller.setTarget(2,self.turn_neutral)
            self.controller.setTarget(1, self.speedTable[0])
            self.controller.setAccel(1,1)
         #   print("Turning Counter Clockwise")
            self.isTurning = False
