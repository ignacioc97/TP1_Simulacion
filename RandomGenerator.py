import pylab as plt
import numpy as np


# LCG Implementation

def lcg(a, c, m, initial_seed):
    seed = initial_seed
    while True:
        rand = (a * seed + c) % m
        seed = rand
        yield rand

def random_sample(n, interval, seed = 20200420162000):
    lower, upper = interval[0], (interval[1]+1)
    sample = []
    varAux = lcg(7**5, 5**7, 2**32, seed)
    for i in range(n):
        observation = (upper - lower) * (next(varAux) / ((2**32)-1)) + lower
        sample.append(int(observation))

    return sample


Z = []
for i in range(501):
    Z.append(random_sample(500, [0, 1]))


plt.imshow(Z, cmap='gray', interpolation='nearest')
plt.show()

U = np.random.random((500, 500))   # Test data
plt.imshow(U, cmap='gray', interpolation='nearest')
plt.show()
