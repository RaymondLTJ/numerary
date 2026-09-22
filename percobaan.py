import numpy as np
from src.base import NumericalMethod

# dummy data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([8.25, 9.79, 13.47, 17.28, 17.15, 19.65, 24.87, 26.15, 26.80, 30.81])

a = NumericalMethod("hi")
b = NumericalMethod("Linear")

print(b.name())

b.name = "kol"

print(b.name())


