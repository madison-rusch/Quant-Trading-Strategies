import numpy as np

B1 = []
B2 = []
for i in range(10000):
    b1 = np.random.normal()
    b2 = b1 + np.random.normal()
    B1.append(b1)
    B2.append(b2)
    
count_positive = 0
for i in range(len(B1)):
    val = B2[i] - 2*B1[i]
    if val < 0:
        count_positive += 1
        
print(count_positive/10000)
