import time
import Maestro as ma

x = ma.Controller()

x.setTarget(1,0)
x.setSpeed(1,0)

#x.setAccel(1,0)
# 6500 to 7300 is a good range for speed (going backwards)
# 17600 to <18000 is a good range for going forward
x.setSpeed(1,1)
for i in range(6400, 7500, 100):
    x.setTarget(1,i)
    print(i)
    time.sleep(1)

time.sleep(2)

#x.setTarget(1,0)
x.close()
