__author__ = 'jiaoyang'

import numpy as np
import matplotlib.pyplot as plt

def sampleER(p,N):
    A=np.zeros((N,N),np.float)

    for i in range(N):
        for j in range(i):
            a=np.random.binomial(1,p)
            A[i,j]=a
            A[j,i]=a

    A=A/(np.sqrt(N*p*(1-p)))
    return A




def density(x):
    if (x<=2) and (x>=-2):
        return np.sqrt(4-x**2)/(2*np.pi)
    else:
        return 0

N=2000;
p=0.01;


A=sampleER(p,N)


eig=np.linalg.eigvalsh(A);
bins=np.arange(-2.5,5,0.15)
plt.hist(eig,bins=bins,normed=True)
bins=np.arange(-2,2.01,0.01)
n=len(bins)
den=np.zeros(n)
for i in range(n):
    den[i]=density(bins[i])

plt.plot(bins,den,'r', linewidth=3.0)
plt.title('Empirical eigenvalue distribution of $G(0.01,2000)$')
plt.show()




