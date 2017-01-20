import numpy as np
a=np.loadtxt('output.txt',delimiter=',',skiprows=1)
print(1.0/(np.diff(a[:,0]).mean()))
print(1.0/(np.diff(a[:,0]).min()))
print(1.0/(np.diff(a[:,0]).max()))
