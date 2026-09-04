import numpy as np
from sklearn.preprocessing import StandardScaler

data = [
    [25,20000],
    [30,40000],
    [35,80000]
]

scalar = StandardScaler()
data_scaled = scalar.fit_transform(data)
print(data_scaled)