import Maestro as ma
import time

class RobotController:
    head_v_increment = 1
    head_h_increment = 1
    waist_increment = 1
    arm_increment = 1

    servo_left_bound = 4100
    servo_right_bound = 7900

    shoulder_left_bound = 6000
    shoulder_right_bound = 7900

    head_v_channel = 4
    head_h_channel = 3
    waist_channel = 0
    turn_channel = 2
    move_channel = 1
    arm_1_channel = 12
    arm_2_channel = 13
    arm_3_channel = 14
    arm_4_channel = 15
    arm_5_channel = 16
    arm_6_channel = 17
    arm_11_channel = 6
    arm_12_channel = 7
    arm_13_channel = 8
    arm_14_channel = 9
    arm_15_channel = 10
    arm_16_channel = 11

    waist_increment = int((servo_right_bound - servo_left_bound) / 3)
    head_v_increment = int((servo_right_bound - servo_left_bound) / 5)
    head_h_increment = int((servo_right_bound - servo_left_bound) / 5)
    arm_increment = int((servo_right_bound - servo_left_bound) / 5)

    max_backward_speed = 6700
    min_backward_speed = 7300

    min_forward_speed = 17600
    max_forward_speed = 18000

    head_v_pos = 6000
    head_h_pos = 6000
    waist_pos = 6000
    shoulder_pos = 6000
    arm_pos = 6000
    hand_twist_pos = 6000
    shoulder_pos2 = 6000
    arm_pos2 = 6000
    hand_twist_pos2 = 6000

    def __init__(self):
        self.controller = ma.Controller()
        self.controller.setAccel(self.head_v_channel, 8)
        self.controller.setAccel(self.head_h_channel, 8)
        self.controller.setAccel(self.arm_1_channel, 8)
        self.controller.setAccel(self.arm_2_channel, 8)
        self.controller.setAccel(self.arm_3_channel, 8)
        self.controller.setAccel(self.arm_4_channel, 8)
        self.controller.setAccel(self.arm_5_channel, 8)
        self.controller.setAccel(self.arm_11_channel, 8)
        self.controller.setAccel(self.arm_12_channel, 8)
        self.controller.setAccel(self.arm_13_channel, 8)
        self.controller.setAccel(self.arm_14_channel, 8)
        self.controller.setAccel(self.arm_15_channel, 8)
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

    def correct_servo_shoulder_bounds(self, number, right_bound, left_bound):
        if(number > right_bound):
            return right_bound
        elif(number < left_bound):
            return left_bound
        else:
            return number

    def reset_pos(self):
        self.head_v_pos = 6000
        self.head_h_pos = 6000
        self.waist_pos = 6000
        self.shoulder_pos = 6000
        self.arm_pos = 6000
        self.hand_twist_pos = 6000
        self.shoulder_pos2 = 6000
        self.arm_pos2 = 6000
        self.hand_twist_pos2 = 6000
        #set initial values
        self.controller.setTarget(self.head_v_channel, self.head_v_pos)
        self.controller.setTarget(self.head_h_channel, self.head_h_pos)
        self.controller.setTarget(self.waist_channel, self.waist_pos)
        self.controller.setTarget(self.arm_1_channel, self.shoulder_pos)
        self.controller.setTarget(self.arm_2_channel, 6500)
        self.controller.setTarget(self.arm_3_channel, self.arm_pos)
        self.controller.setTarget(self.arm_4_channel, self.arm_pos)
        self.controller.setTarget(self.arm_5_channel, self.hand_twist_pos)
        self.controller.setTarget(self.arm_11_channel, self.shoulder_pos2)
        self.controller.setTarget(self.arm_12_channel, 6500)
        self.controller.setTarget(self.arm_13_channel, self.arm_pos2)
        self.controller.setTarget(self.arm_14_channel, self.arm_pos2)
        self.controller.setTarget(self.arm_15_channel, self.hand_twist_pos2)
        
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

    def move_shoulder_down(self):
        self.shoulder_pos = self.move_servo_shoulder(self.shoulder_pos, self.arm_increment, self.arm_1_channel, self.shoulder_right_bound, self.shoulder_left_bound)
        #print("current position: ", self.shoulder_pos)

    def move_shoulder_up(self):
        self.shoulder_pos = self.move_servo_shoulder(self.shoulder_pos, -self.arm_increment, self.arm_1_channel, self.shoulder_right_bound, self.shoulder_left_bound)
        #print("current position: ", self.shoulder_pos)

    def move_arms_up(self):
        #self.arm_pos = self.move_servo(self.arm_pos, self.arm_increment, self.arm_2_channel)
        self.arm_pos = self.move_servo(self.arm_pos, self.arm_increment, self.arm_3_channel)
        self.arm_pos = self.move_servo(self.arm_pos, self.arm_increment, self.arm_4_channel)
        #self.arm_pos = self.move_servo(self.arm_pos, self.arm_increment, self.arm_5_channel)
        #print("current_pos", self.arm_pos)

    def move_arms_down(self):
        #self.arm_pos = self.move_servo(self.arm_pos, -self.arm_increment, self.arm_2_channel)
        self.arm_pos = self.move_servo(self.arm_pos, -self.arm_increment, self.arm_3_channel)
        self.arm_pos = self.move_servo(self.arm_pos, -self.arm_increment, self.arm_4_channel)
        #self.arm_pos = self.move_servo(self.arm_pos, -self.arm_increment, self.arm_5_channel)
        #print("current_pos", self.arm_pos)

    def twist_hand_left(self):
        self.hand_twist_pos = self.move_servo(self.hand_twist_pos, -self.arm_increment, self.arm_5_channel)

    def twist_hand_right(self):
        self.hand_twist_pos = self.move_servo(self.hand_twist_pos, self.arm_increment, self.arm_5_channel)

    def move_shoulder_down2(self):
        self.shoulder_pos2 = self.move_servo_shoulder(self.shoulder_pos, self.arm_increment, self.arm_1_channel, self.shoulder_right_bound, self.shoulder_left_bound)
        #print("current position: ", self.shoulder_pos)

    def move_shoulder_up2(self):
        self.shoulder_pos2 = self.move_servo_shoulder(self.shoulder_pos, -self.arm_increment, self.arm_1_channel, self.shoulder_right_bound, self.shoulder_left_bound)
        #print("current position: ", self.shoulder_pos)

    def move_arms_up2(self):
        #self.arm_pos = self.move_servo(self.arm_pos, self.arm_increment, self.arm_2_channel)
        self.arm_pos2 = self.move_servo(self.arm_pos, self.arm_increment, self.arm_3_channel)
        self.arm_pos2 = self.move_servo(self.arm_pos, self.arm_increment, self.arm_4_channel)
        #self.arm_pos = self.move_servo(self.arm_pos, self.arm_increment, self.arm_5_channel)
        #print("current_pos", self.arm_pos)

    def move_arms_down2(self):
        #self.arm_pos = self.move_servo(self.arm_pos, -self.arm_increment, self.arm_2_channel)
        self.arm_pos2 = self.move_servo(self.arm_pos, -self.arm_increment, self.arm_3_channel)
        self.arm_pos2 = self.move_servo(self.arm_pos, -self.arm_increment, self.arm_4_channel)
        #self.arm_pos = self.move_servo(self.arm_pos, -self.arm_increment, self.arm_5_channel)
        #print("current_pos", self.arm_pos)

    def twist_hand_left2(self):
        self.hand_twist_pos2 = self.move_servo(self.hand_twist_pos, -self.arm_increment, self.arm_5_channel)

    def twist_hand_right2(self):
        self.hand_twist_pos2 = self.move_servo(self.hand_twist_pos, self.arm_increment, self.arm_5_channel)


    def move_servo(self,oldPos, change, channel):
        newPos = oldPos + change
        newPos = self.correct_servo_bounds(newPos)
        self.controller.setTarget(channel, newPos)
        return newPos

    def move_servo_shoulder(self, oldPos, change, channel, right_bound, left_bound):
        newPos = oldPos + change
        newPos = self.correct_servo_shoulder_bounds(newPos, right_bound, left_bound)
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
            time.sleep(.01)
        # time.sleep(.5)
        self.moveScale = newSpeed
        print("moveScale is now: ", self.moveScale)

    def move_forward(self, speed):
        self.setSpeed(speed)

    # speed is absolute
    def move_backwards(self, speed):
        self.setSpeed(-speed)

    def ramp_forward(self):
        if not self.moveScale == 3:
            self.setSpeed(self.moveScale + 1)
        pass

    def ramp_backward(self):
        if not self.moveScale == -3:
            self.setSpeed(self.moveScale - 1)

    def stop_moving(self):
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
            # set turn "right" first:
            self.controller.setAccel(1,0)
            self.controller.setTarget(2,self.turn_clock)
            self.controller.setTarget(1, self.speedTable[2])
            time.sleep(.5)
            self.controller.setTarget(2,self.turn_neutral)
            self.controller.setTarget(1, self.speedTable[0])
            self.controller.setAccel(1,1)
            self.isTurning = False

    def turn_counterClockWise(self):    
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
            self.isTurning = False
