import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

n_sims = 15
data = np.random.randint(0, 37, n_sims)
df = pd.Series(data).value_counts().sort_index().div(n_sims)
df.plot(kind='bar', x=1, y=2)
plt.xlabel('Possible roulette numbers')
plt.ylabel('Relative frequency')
plt.title('Simulation of roulette throw')
plt.show()