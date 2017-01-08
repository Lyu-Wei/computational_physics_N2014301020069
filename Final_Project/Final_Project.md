## Final Project
### 姓名：吕蔚 
### 学号：2014301020069 
### 班级：14级彭桓武班
# 作业在这里
[作业部落](https://www.zybuluo.com/Lyu-Wei/note/503209)
```
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
y0 = np.zeros(101)
x1 = np.zeros(101)
x2 = np.zeros(101)

for i in range(1,101):
   r = np.random.rand()
   if r<0.5:
       x1[i] = x1[i-1] + 1
   else:
       x1[i] = x1[i-1] - 1
       
for i in range(1,101):
   r = np.random.rand()
   if r<0.5:
       x2[i] = x2[i-1] + 1
   else:
       x2[i] = x2[i-1] - 1

plt.scatter(steps, x1)
plt.scatter(steps, x2,c='r')
plt.plot(steps, y0)
plt.xlim(0,100)
plt.grid(True)
plt.xlabel('step number')
plt.ylabel('x')
plt.title('Random walk in one dimension')

plt.show()
```

```
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
xave = np.zeros(101)
y0 = np.zeros(101)
x = np.zeros(5000)

for j in range(101):
    for i in range(5000):
        r = np.random.rand()
        if r<0.5:
            x[i] = x[i] + 1
        else:
            x[i] = x[i] - 1
    xave[j] = sum(x)/5000
    
plt.plot(steps, xave, '.')
plt.plot(steps, y0)
plt.xlim(0,100)
plt.ylim(-1,1)
plt.grid(True)
plt.xlabel('step number (= time)')
plt.ylabel('<x>')
plt.title('Random walk in one dimension')
plt.annotate('<x> versus time', xy=(20, 0.5))

plt.show()
```
