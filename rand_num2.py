import numpy as np
r = np.random.random()
print(r)
# one number between 0 and 1
r = np.random.random(size=10000)
print(r) # array with 10000 numbers
r = np.random.uniform(-1, 10)
print(r)
# one number between -1 and 10
r = np.random.uniform(-1, 10, size=10000)
print(r)
