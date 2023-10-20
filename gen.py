# Importēt programmas, lai varētu ģenerēt tos skaitļus
import matplotlib.pyplot as plt
import numpy as np
# Pielikt mainīgos klāt
rng = np.random.randn(100)
plt.hist (rng, bins=5)
# Iegūsti skaitļus
print(rng)