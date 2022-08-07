# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:09:47 2022

@author: TOT_User
"""
from FUNC import *
N = 6
def array0(N):
    return np.zeros((N+1,N+1))
    
if N== 1:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i][i:] = [r[0],r_d]
        if i==1:
            BDT_short_rate[i][i] = r_u
if N==2:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i] = [r[0],r_d,r_d2]
        if i==1:
            BDT_short_rate[i][1:] = [r_u,r_ud]
        if i==2:
            BDT_short_rate[i][2] = r_u2
if N==3:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i] = [r[0],r_d,r_d2,r_d3]
        if i==1:
            BDT_short_rate[i][i:] = [r_u,r_ud,r_ud2]
        if i==2:
            BDT_short_rate[i][i:] = [r_u2,r_u2d]
        if i==3:
            BDT_short_rate[i][i] = r_u3           
if N==4:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i] = [r[0],r_d,r_d2,r_d3,r_d4]
        if i==1:
            BDT_short_rate[i][i:] = [r_u,r_ud,r_ud2,r_ud3]
        if i==2:
            BDT_short_rate[i][i:] = [r_u2,r_u2d,r_u2d2]
        if i==3:
            BDT_short_rate[i][i:] = [r_u3,r_u3d]
        if i==4: 
            BDT_short_rate[i][i] = r_u4
if N==5:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i] = [r[0],r_d,r_d2,r_d3,r_d4,r_d5]
        if i==1:
            BDT_short_rate[i][i:] = [r_u,r_ud,r_ud2,r_ud3,r_ud4]
        if i==2:
            BDT_short_rate[i][i:] = [r_u2,r_u2d,r_u2d2,r_u2d3]
        if i==3:
            BDT_short_rate[i][i:] = [r_u3,r_u3d,r_u3d2]
        if i==4: 
            BDT_short_rate[i][i:] = [r_u4,r_u4d]
        if i==5: 
            BDT_short_rate[i][i] = r_u5    
if N==6:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i] = [r[0],r_d,r_d2,r_d3,r_d4,r_d5,r_d6]
        if i==1:
            BDT_short_rate[i][i:] = [r_u,r_ud,r_ud2,r_ud3,r_ud4,r_ud5]
        if i==2:
            BDT_short_rate[i][i:] = [r_u2,r_u2d,r_u2d2,r_u2d3,r_u2d4]
        if i==3:
            BDT_short_rate[i][i:] = [r_u3,r_u3d,r_u3d2,r_u3d3]
        if i==4: 
            BDT_short_rate[i][i:] = [r_u4,r_u4d,r_u4d2]
        if i==5: 
            BDT_short_rate[i][i:] = [r_u5,r_u5d]
        if i==6: 
            BDT_short_rate[i][i] = r_u6
if N==7:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i] = [r[0],r_d,r_d2,r_d3,r_d4,r_d5,r_d6,r_d7]
        if i==1:
            BDT_short_rate[i][i:] = [r_u,r_ud,r_ud2,r_ud3,r_ud4,r_ud5,r_ud6]
        if i==2:
            BDT_short_rate[i][i:] = [r_u2,r_u2d,r_u2d2,r_u2d3,r_u2d4,r_u2d5]
        if i==3:
            BDT_short_rate[i][i:] = [r_u3,r_u3d,r_u3d2,r_u3d3,r_u3d4]
        if i==4: 
            BDT_short_rate[i][i:] = [r_u4,r_u4d,r_u4d2,r_u4d3]
        if i==5: 
            BDT_short_rate[i][i:] = [r_u5,r_u5d,r_u5d2]
        if i==6: 
            BDT_short_rate[i][i:] = [r_u6,r_u6d]
        if i==7: 
            BDT_short_rate[i][i] = r_u7
if N==8:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i] = [r[0],r_d,r_d2,r_d3,r_d4,r_d5,r_d6,r_d7,r_d8]
        if i==1:
            BDT_short_rate[i][i:] = [r_u,r_ud,r_ud2,r_ud3,r_ud4,r_ud5,r_ud6,r_ud7]
        if i==2:
            BDT_short_rate[i][i:] = [r_u2,r_u2d,r_u2d2,r_u2d3,r_u2d4,r_u2d5,r_u2d6]
        if i==3:
            BDT_short_rate[i][i:] = [r_u3,r_u3d,r_u3d2,r_u3d3,r_u3d4,r_u3d5]
        if i==4: 
            BDT_short_rate[i][i:] = [r_u4,r_u4d,r_u4d2,r_u4d3,r_u4d4]
        if i==5: 
            BDT_short_rate[i][i:] = [r_u5,r_u5d,r_u5d2,r_u5d3]
        if i==6: 
            BDT_short_rate[i][i:] = [r_u6,r_u6d,r_u6d2]
        if i==7: 
            BDT_short_rate[i][i:] = [r_u7,r_u7d]
        if i==8: 
            BDT_short_rate[i][i] = r_u8
if N==9:
    BDT_short_rate = array0(N)
    for i in range(len(BDT_short_rate)):
        if i==0:
            BDT_short_rate[i] = [r[0],r_d,r_d2,r_d3,r_d4,r_d5,r_d6,r_d7,r_d8,r_d9]
        if i==1:
            BDT_short_rate[i][i:] = [r_u,r_ud,r_ud2,r_ud3,r_ud4,r_ud5,r_ud6,r_ud7,r_ud8]
        if i==2:
            BDT_short_rate[i][i:] = [r_u2,r_u2d,r_u2d2,r_u2d3,r_u2d4,r_u2d5,r_u2d6,r_u2d7]
        if i==3:
            BDT_short_rate[i][i:] = [r_u3,r_u3d,r_u3d2,r_u3d3,r_u3d4,r_u3d5,r_u3d6]
        if i==4: 
            BDT_short_rate[i][i:] = [r_u4,r_u4d,r_u4d2,r_u4d3,r_u4d4,r_u4d5]
        if i==5: 
            BDT_short_rate[i][i:] = [r_u5,r_u5d,r_u5d2,r_u5d3,r_u5d4]
        if i==6: 
            BDT_short_rate[i][i:] = [r_u6,r_u6d,r_u6d2,r_u6d3]
        if i==7: 
            BDT_short_rate[i][i:] = [r_u7,r_u7d,r_u7d2]
        if i==8: 
            BDT_short_rate[i][i:] = [r_u8,r_u8d]
        if i==9: 
            BDT_short_rate[i][i] = r_u9
if N == 10:
    BDT_short_rate = array0(N) 
    BDT_short_rate[0][:] = [0.1,r_d,r_d2,r_d3,r_d4,r_d5,r_d6,r_d7,r_d8,r_d9,r_d10] #t=0
    BDT_short_rate[1][1:] =[r_u,r_ud,r_ud2,r_ud3,r_ud4,r_ud5,r_ud6,r_ud7,r_ud8,r_ud9] #t=1
    BDT_short_rate[2][2:] = [r_u2,r_u2d,r_u2d2,r_u2d3,r_u2d4,r_u2d5,r_u2d6,r_u2d7,r_u2d8] #t=2
    BDT_short_rate[3][3:] = [r_u3,r_u3d,r_u3d2,r_u3d3,r_u3d4,r_u3d5,r_u3d6,r_u3d7] #t=3
    BDT_short_rate[4][4:] = [r_u4,r_u4d,r_u4d2,r_u4d3,r_u4d4,r_u4d5,r_u4d6] #t=4
    BDT_short_rate[5][5:] = [r_u5,r_u5d,r_u5d2,r_u5d3,r_u5d4,r_u5d5] 
    BDT_short_rate[6][6:] = [r_u6,r_u6d,r_u6d2,r_u6d3,r_u6d4] #t=6
    BDT_short_rate[7][7:] = [r_u7,r_u7d,r_u7d2,r_u7d3] #t=7
    BDT_short_rate[8][8:] = [r_u8,r_u8d,r_u8d2] #t=8
    BDT_short_rate[9][9:] = [r_u9,r_u9d] #t=9
    BDT_short_rate[10][10:] = [r_u10] #t=10   
    
Price = np.zeros((N+1,N+1))
for i in trange(len(Price)-1,-1,-1):
    for j in trange(len(Price)-1,-1,-1):
      if i > j :
          pass
      else:
          if j == N:
              Price[i][j] = round(price)
          else:
              Price[i][j] = round(100*c + (q*Price[i+1][j+1] + p*Price[i][j+1])/(1+BDT_short_rate[i][j]),2)
print(Price)
Bond_Price = Price[0][0]
Callable_Bond_Price = round((Bond_Price - Call_Price),2)
print('Callable Bond Price = {}'.format(Callable_Bond_Price))
