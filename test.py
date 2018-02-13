import Maestro as ma
import serial
import time
targ = 1

#This will make it go
x = ma.Controller()
# x.setAccel(targ,0)
# x.setSpeed(targ, 1)
# x.setTarget(targ, 8000)
# x.setSpeed(targ, 2)
# x.setSpeed(targ, 3)
#x.setSpeed(targ, 4)
#x.setSpeed(targ, 5)

#time.sleep(10)
x.setTarget(targ,0)
x.setSpeed(targ, 0)

# time.sleep(10)

# reverse at 6500
# forward at 16000

############################################################33
# go in reverse:
x.setSpeed(targ,1)
x.setAccel(targ, 1)
# x.setTarget(targ, 8000)

for i in range(6000, 7000, 500):
    print(i)
    x.setTarget(targ,i)
    time.sleep(.5)
#############################################################
# x.setSpeed(targ, 1)
# x.setTarget(targ, 20000

#x.setTarget(targ, 0)

x.setSpeed(2,0)
x.setTarget(2,0)

x.setSpeed(2,1)
x.setAccel(2, 1)

x.setTarget(2,500)

#for i in range(0, 1000, 500):
#    print(i)
#    x.setTarget(2,i)
#    time.sleep(.5)
time.sleep(8)
#for i in range(18000, 50000, 500):
#    print(i)
#    x.setTarget(2,i)
#    time.sleep(.5)
time.sleep(3)
x.setSpeed(2,0)
x.setTarget(2,0)
x.setTarget(1,0)
time.sleep(.5)
x.close()
