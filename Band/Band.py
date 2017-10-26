__author__ = 'jiaoyang'

import numpy as np
import matplotlib.pyplot as plt



# Sample an $N*N$ band matrix, with band width $2W+1$.
def sampleB(W,N):
    A=np.zeros((N,N),np.float)

    for i in range(N):
        for j in range(W+1):
            a=np.random.normal(0,1)/np.sqrt(2*W+1)
            if j==0:
                A[i,i]=a
            else:
                if i+j<N:
                    A[i,i+j]=a
                    A[i+j,i]=a
                else:
                    A[i,i+j-N]=a
                    A[i+j-N,i]=a

    return A





def Green(A,N,z):
    G=np.linalg.inv(A-z*np.eye(N))
    return G


# Take out a submatrix of $G$ and check the imaginary part,
# However, it seems that the smallest eigenvalue of it can be as small as the trivial bound \eta
def subG(N,W,z):
    M=W/2
    A=sampleB(W,N)
    # eig=np.linalg.eigvalsh(A)
    # plt.hist(eig)
    # plt.show()


    G=Green(A,N,z)
    subG=G[0:M, 0:M]
    imsubG=np.imag(subG)

    eig=np.linalg.eigvalsh(imsubG)
    print(1.0/W, eig)
    # bin=np.arange(0,1, 1.0/W)
    # plt.hist(eig,bin)
    # plt.show()

    return eig


# Take out part of the eigenvectors, and check their length

def eignorm(N,W):
    M=W/2
    A=sampleB(W,N)
    eig,ev=np.linalg.eigh(A)

    #take out M eigenvectors
    subev=ev[:, N/2:N/2+M]
    norm=np.dot(subev, np.transpose(subev))
    print(np.float(M)/N)
    
    m=min(np.diag(norm))
    M=max(np.diag(norm))

    print(m,M)
    return norm




eignorm(2000,100)
