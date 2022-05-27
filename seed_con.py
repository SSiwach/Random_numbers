import random
random.seed(42) # generate specific number which don't change with every compilation
N = 500 # no of samples
x = range(N)
y = [random.uniform(-1,1) for i in x]

import matplotlib.pyplot as plt
plt.scatter(x, y)
