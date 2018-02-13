import Maestro as ma
import serial
import time
targ = 1

#This will make it go
x = ma.Controller()

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

#for i in range(6000, 8000, 500):
for i in range(18000, 26000, 500):
    print(i)
    x.setTarget(targ,i)
#    time.sleep(.5)
    time.sleep(.5)
#############################################################

time.sleep(8)

time.sleep(3)

x.setTarget(1,0)
time.sleep(.5)
x.close()
