import Maestro as ma
import time

x = ma.Controller()

x.setTarget(1,6000)
x.setSpeed(1,6000)


# THIS ACTUALLY GOES FORWARD

############################################################
############################################################
#x.setSpeed(1,1)
#for i in range(6000, 3500, -500):
#    x.setTarget(1,i)
#    print(i)
#    time.sleep(.5)

#time.sleep(5)
#########################################################################
#########################################################################


# THIS ACTUALLY GOES BACKWARDS

#-----------------------------------------------------------------------
#x.setSpeed(1,1)
#for i in range(6000, 8500, 500):
#    x.setTarget(1,i)
#    print(i)
#    time.sleep(.5)
#time.sleep(5)
#-----------------------------------------------------------------------

x.setSpeed(1,1)
for i in range (6000, 3500, -500):
    x.setTarget(1,i)
    print(i)
    time.sleep(.5)
time.sleep(5)
#print ("turning???")
#x.setTarget(2,6000)

#time.sleep(8)

print ("turning again!")
x.setTarget(2, 5500)
time.sleep(10)
print("turning once more!")
x.setTarget(2, 6500)
time.sleep(8)

x.setTarget(2,6000)

x.setTarget(1,6000)
x.close()
