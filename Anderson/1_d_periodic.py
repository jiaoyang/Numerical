__author__ = 'jiaoyang'


import numpy as np
import matplotlib.pyplot as plt

def sampleAD(N):
    A=np.zeros((N,N),np.float)
    for i in range(N):
        A[i,i]=np.random.uniform(-1,1)
        if (i==0):
            A[i,i+1]=1
            A[i,N-1]=1
        elif (i==N-1):
            A[i,0]=1
            A[i,i-1]=1
        else:
            A[i,i+1]=1
            A[i,i-1]=1

    return A



A=sampleAD(2000)
eig, ev=np.linalg.eigh(A)
print eig[1000]
print ev[:,1000]
plt.plot(ev[:,1000])
plt.show()

