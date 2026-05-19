#%%
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.abs(a)
c = np.abs(a)**2
d = np.sum(np.abs(a)**2, axis=-1)
e = np.sum(np.abs(a)**2, axis=-1)**(1./2)

print(f"{b}\n")
print(f"{c}\n")
print(f"{d}\n")
print(f"{e}\n")
#%%
