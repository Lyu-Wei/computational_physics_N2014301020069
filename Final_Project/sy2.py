# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def density(t1):
    
    x = np.linspace(-50,50,101)
    y = np.linspace(-50,50,101)
    x,y = np.meshgrid(x,y)
    d = np.zeros((101,101))
    d[50,50]=1
    d1 = deepcopy(d)

    for t in range(t1):
        for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])
        d1=deepcopy(d)

    for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    if d[i][j]==0:
                        d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])

    return x,y,d
t = 0
x,y,z = density(t)[0],density(t)[1],density(t)[2]

fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.coolwarm,linewidth=0.1, antialiased=False)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('density')
ax.set_title('Distribution in 2 dimension, t=0')
plt.xlim(-50,50)
plt.ylim(-50,50)

fig.colorbar(surf,shrink=0.5,aspect=5)

plt.show()