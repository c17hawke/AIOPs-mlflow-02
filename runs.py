import os
import numpy as np

alpha_s = np.linspace(0.1, 1.0, 5)
l1_ratios = np.linspace(0.1, 1.0, 5)

for alpha in alpha_s:
    for l1 in l1_ratios:
        print(f"logging experiment for alpha:{alpha}, l1: {l1}")
        os.system(f"python demo.py -a {alpha} -l1 {l1}")