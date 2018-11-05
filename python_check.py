import string
import numpy
import time

prev_time = time.time()
print(prev_time)
while 1 :
    dt = time.time() - prev_time
    if dt >1 :
        print("a")
        prev_time = time.time()