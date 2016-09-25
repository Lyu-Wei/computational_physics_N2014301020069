import os
import time
os.system('cls')

a = [[' ' for i in range(40)] for j in range(40)]

n = 1
while n < 40:
    a[21][5] = ' '
    a[18][5] = ' '   
    for j in range(4,35):   
        a[20][j] = ' '
        a[19][j] = ' '
    a[5][21] = '#'
    a[5][18] = '#'
    for i in range(4,35):
        a[i][20] = '*'
        a[i][19] = '*'
    for i in range(40):
        for j in range(40):
            print a[i][j],
        print ' '
    time.sleep(0.2)    
    os.system('cls') 
    a[5][21] = ' '
    a[5][18] = ' '
    for i in range(4,35):
        a[i][20] = ' '
        a[i][19] = ' '
    a[21][33] = '#'
    a[18][33] = '#'
    for j in range(4,35):   
        a[20][j] = '*'
        a[19][j] = '*'
    for i in range(40):
        for j in range(40):
            print a[i][j],
        print ' '
    time.sleep(0.2)    
    os.system('cls') 
    
    a[21][33] = ' '
    a[18][33] = ' '   
    for j in range(4,35):   
        a[20][j] = ' '
        a[19][j] = ' '
    a[33][21] = '#'
    a[33][18] = '#'
    for i in range(4,35):
        a[i][20] = '*'
        a[i][19] = '*'
    for i in range(40):
        for j in range(40):
            print a[i][j],
        print ' '
    time.sleep(0.2)    
    os.system('cls') 
    a[33][21] = ' '
    a[33][18] = ' '
    for i in range(4,35):
        a[i][20] = ' '
        a[i][19] = ' '
    a[21][5] = '#'
    a[18][5] = '#'
    for j in range(4,35):   
        a[20][j] = '*'
        a[19][j] = '*'
    for i in range(40):
        for j in range(40):
            print a[i][j],
        print ' '
    time.sleep(0.2)    
    os.system('cls') 
    n = n + 1
    