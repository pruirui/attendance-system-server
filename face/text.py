#coding=utf-8
import numpy as np
 
a=np.arange(15).reshape(3,5)
print (a)
b=a.tobytes()
print ((b))
c=np.frombuffer(b,np.int32).reshape(3,5)
print (c)