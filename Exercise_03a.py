# -*- coding: utf-8 -*-
import os
os.system('cls')

print u'请输入任意大写字母，然后按回车'

A=['  #  ',' # # ',' ### ','#   #','#   #']
B=['#### ','#   #','#### ','#   #','#### ']
C=['#####','#    ','#    ','#    ','#####']
D=['###  ','#  # ','#   #','#  # ','###  ']
E=['#####','#    ','#####','#    ','#####']
F=['#####','#    ','#####','#    ','#    ']
G=['#####','#    ','#  ##','#   #','#####']
H=['#   #','#   #','#####','#   #','#   #']
I=[' ### ','  #  ','  #  ','  #  ',' ### ']
J=[' ### ','  #  ','  #  ','  #  ',' ##  ']
K=['#  # ','# #  ','##   ','#  # ','#   #']
L=['#    ','#    ','#    ','#    ','#####']
M=['#   #','## ##','# # #','#   #','#   #']
N=['#   #','##  #','# # #','#  ##','#   #']
O=['#####','#   #','#   #','#   #','#####']
P=['#### ','#   #','#### ','#    ','#    ']
Q=['#####','#   #','# # #','#  ##','#####']
R=['#### ','#   #','#### ','# #  ','#  # ']
S=['#####','#    ','#####','    #','#####']
T=['#####','  #  ','  #  ','  #  ','  #  ']
U=['#   #','#   #','#   #','#   #','#####']
V=['#   #','#   #',' # # ',' # # ','  #  ']
W=['#   #','#   #','# # #','## ##','#   #']
X=['#   #',' # # ','  #  ',' # # ','#   #']
Y=['#   #',' # # ','  #  ','  #  ','  #  ']
Z=['#####','   # ','  #  ',' #   ','#####']

a = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
b = raw_input()
os.system('cls')
c = list(b)
d = '                                                  '

for i in range(len(c)):
    c[i] = ord(c[i])-65
for j in range(50):    
    for k in range(5):
        print d[:j],        
        for m in c:
            print a[m][k],' ',
        print ' '
    import time
    time.sleep(0.03)
    os.system('cls')