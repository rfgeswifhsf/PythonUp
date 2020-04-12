items=[1,2,3,4,5]
item=[2,3,4,5,6]
super=map(lambda x:x+2,items)
print(list(super))

super1=map(lambda x:[x+x,x*x],items)
print(tuple(super1))

less=filter(lambda x:x>3,items)
print(list(less))

from functools import reduce
re=reduce(lambda x,y:x+y,items)
print(re)

import numpy as np
print(np.add([1,2,3],[4,5,6]))

