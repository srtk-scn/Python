#memory usage between generator or List
import time
t1=time.time()
l=[i**8 for i in range(1000000)]
print(time.time()-t1)
t3=time.time()
g=(i**4 for i in range(1000000))
print(time.time()-t3)