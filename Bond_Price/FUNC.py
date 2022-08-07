# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:52:51 2022

@author: TOT_User
"""
from __future__ import division
import sys
import math 
from scipy.optimize import fsolve
import pandas as pd
import numpy as np
from tqdm import trange
#given parameters
c = 0.055 #Coupon rate
T = 5  #Maturity
Call_Price = 103
stepsize = 0.5  #Semi-Annual
initial_rate = 0.06
u = 1.25
d = 1/u
q = 0.5
p = 1-q
N = int(T/stepsize)
price = 250*(1+c) #Price at maturity time'''
"""
Maturity            Yield(%)       Yield_Volatility
1                    10             20
2                    10.5           19
3                    11             18
4                    11.5           17
5                    12             16
6                    12.5           15
7                    13             14
8                    13.5           13
9                    14             12
10                   14.5           11
11                   15             10
"""
t = [1,2,3,4,5,6,7,8,9,10,11]        
r = [0.1,0.105,0.11,0.115,0.12,0.125,0.13,0.135,0.14,0.145,0.15]
vol = [0.20,0.19,0.18,0.17,0.16,0.15,0.14,0.13,0.12,0.11,0.1]
df  = pd.DataFrame(data={'t':t,'Yield':r,'Vol':vol})
m = 0.03  #guess
 
a1 = 100/(1+r[0])**1
a2 = 100/(1+r[1])**2
a3 = 100/(1+r[2])**3
a4 = 100/(1+r[3])**4
a5 = 100/(1+r[4])**5
a6 = 100/(1+r[5])**6
a7 = 100/(1+r[6])**7
a8 = 100/(1+r[7])**8
a9 = 100/(1+r[8])**9
a10 = 100/(1+r[9])**10
a11 = 100/(1+r[10])**11

def bdtOne(guess):
    r_u = guess * math.exp(2 * df.Vol.iloc[1]) #rate_dict['rate2'][1][1] = x[0]
    r_d = guess #rate_dict['rate2'][0][1] =x[0]
    N1 = (100)/(1+r_u) #stock_dict['stock2'][1][1]
    N2 = (100)/(1+r_d) #stock_dict['stock2'][0][1]
    return (0.5*((N1/(1+r[0])) + (N2/(1+r[0])))-a2)
g = fsolve(bdtOne,m)[0]
r_u = g * math.exp(2 * df.Vol.iloc[1])
r_d = g
def bdtTwo2(x):
    r_u2 = x[0] * math.exp(4 * x[1]) #rate_dict['rate3'][2][2]
    r_ud = x[0] * math.exp(2 * x[1]) #rate_dict['rate3'][1][2]
    r_d2 = x[0] #rate_dict['rate3'][0][2]
    N1 = (100)/(1+r_u2) #stock_dict['stock3'][2][2]
    N2 = (100)/(1+r_ud) #stock_dict['stock3'][1][2]
    N3 = (100)/(1+r_d2) #stock_dict['stock3'][0][2]
    ans1 = (0.5*(N1 + N2))/(1+r_u) #stock_dict['stock3'][1][1]
    ans2 = (0.5*(N2 + N3))/(1+r_d) #stock_dict['stock3'][0][1]
    y_u = math.sqrt(100/ans1) - 1
    y_d = math.sqrt(100/ans2) - 1
    out = [((0.5*(ans1 + ans2))/(1+r[0])-a3)] #stock_dict['stock3'][0][0]
    out.append((0.5 * math.log(y_u/y_d) - df.Vol.iloc[2]))
    return out

k = fsolve(bdtTwo2,[0.1,0.1])
r_u2 = k[0] * math.exp(4 * k[1])
r_ud = k[0] * math.exp(2 * k[1])
r_d2 = k[0]

def bdtThree3(x):
    r_u3 = x[0] * math.exp(6 * x[1]) #rate_dict['rate4'][3][3] = x[0]*math.exp(2*3 * x[1])
    r_u2d = x[0] * math.exp(4 * x[1]) #rate_dict['rate4'][2][3] = x[0]*math.exp(2*2 * x[1])
    r_ud3 = x[0] * math.exp(2 * x[1]) #rate_dict['rate4'][1][3] = x[0]*math.exp(2*1 * x[1])
    r_d4 = x[0] #rate_dict['rate4'][0][3] = x[0]
    N1 = 100/(1+r_u3) #stock_dict['stock3'][3][3]
    N2 = 100/(1+r_u2d) #stock_dict['stock3'][2][3]
    N3 = 100/(1+r_ud3) #stock_dict['stock3'][1][3]
    N4 = 100/(1+r_d4) #stock_dict['stock3'][0][3]
    ans1 = (0.5*(N1+N2))/(1+r_u2) #stock_dict['stock3'][2][2]
    ans2 = (0.5*(N2+N3))/(1+r_ud) #stock_dict['stock3'][1][2]
    ans3 = (0.5*(N3+N4))/(1+r_d2) #stock_dict['stock3'][0][2]
    fans1 = (0.5*(ans1+ans2))/(1+r_u) #stock_dict['stock3'][1][1]
    fans2 = (0.5*(ans2+ans3))/(1+r_d) #stock_dict['stock3'][1][0]
    y_u2 = math.sqrt(100/ans1) - 1 #yield_dict['yield3'][2][2] = math.sqrt(100/stock_dict['stock3'][2][2]) - 1
    y_ud = math.sqrt(100/ans2) - 1 #yield_dict['yield3'][1][2] = math.sqrt(100/stock_dict['stock3'][1][2]) - 1
    y_d2 = math.sqrt(100/ans3) - 1 #yield_dict['yield3'][0][2] = math.sqrt(100/stock_dict['stock3'][0][2]) - 1
    #y_u = (100/fans1)**(1/3) - 1
    #y_d = (100/fans2)**(1/3) - 1
    out = [((0.5*fans1 + 0.5*fans2)/(1+r[0]) - a4)]
    out.append((0.5 * math.log(y_u2/y_ud) - df.Vol.iloc[3] )) 
    return out

g = fsolve(bdtThree3,[0.1,0.1],xtol=1.49012e-20 )
#bdtThree3([ 0.08271889,  0.16859304])
r_u3 = g[0] * math.exp(6 * g[1])
r_u2d = g[0] * math.exp(4 * g[1])
r_ud2 = g[0] * math.exp(2 * g[1])
r_d3 = g[0]

def bdtFour(x):
    r_u4 = x[0]*math.exp(8 * x[1] )
    r_u3d = x[0]*math.exp(6 * x[1])
    r_u2d2 = x[0]*math.exp(4 * x[1])
    r_ud3 = x[0]*math.exp(2 * x[1])
    r_d4 = x[0]  
    N1 = 100/(1+r_u4) 
    N2 = 100/(1+r_u3d)
    N3 = 100/(1+r_u2d2)
    N4 = 100/(1+r_ud3)
    N5 = 100/(1+r_d4)
    ans1 = (0.5*(N1+N2))/(1+r_u3)
    ans2 = (0.5*(N2+N3))/(1+r_u2d)
    ans3 = (0.5*(N3+N4))/(1+r_ud2)
    ans4 = (0.5*(N4+N5))/(1+r_d3)
    fans1 = ((0.5*ans1 + 0.5*ans2))/(1 + r_u2)
    fans2 = ((0.5*ans2 + 0.5*ans3))/(1 + r_ud)
    fans3 = ((0.5*ans3 + 0.5*ans4))/(1 + r_d2)
    xans1 = ((0.5*fans1 + 0.5*fans2))/(1 + r_u)
    xans2 = ((0.5*fans2 + 0.5*fans3))/(1 + r_d)
    y_u3 = math.sqrt(100/ans1) - 1
    y_u2d = math.sqrt(100/ans2) - 1
    y_ud2 = math.sqrt(100/ans3) - 1
    y_d3 = math.sqrt(100/ans4) - 1
    out = [((0.5*xans1 + 0.5*xans2)/(1+r[0]) -a5 )]
    out.append(((0.5 * math.log(y_u3/y_u2d) - df.Vol.iloc[4])))    
    return out

g = fsolve(bdtFour,[0.1,0.1],xtol=1.49012e-20)
#bdtFour([ 0.08048839,  0.15227017])
r_u4 = g[0] * math.exp(8 * g[1])
r_u3d = g[0] * math.exp(6 * g[1])
r_u2d2 = g[0] * math.exp(4 * g[1])
r_ud3 = g[0] * math.exp(2 * g[1])
r_d4 = g[0] 

def bdtFive(x):
    r_u5 = x[0]*math.exp(10 * x[1] )
    r_u4d = x[0]*math.exp(8 * x[1] ) 
    r_u3d2 = x[0]*math.exp(6 * x[1]) 
    r_u2d3 = x[0]*math.exp(4 * x[1])
    r_ud4 = x[0]*math.exp(2 * x[1])    
    r_d5 = x[0]  
    N1 = 100/(1+r_u5) 
    N2 = 100/(1+r_u4d)
    N3 = 100/(1+r_u3d2)
    N4 = 100/(1+r_u2d3)
    N5 = 100/(1+r_ud4)
    N6 = 100/(1+r_d5)
    ans1 = (0.5*(N1+N2))/(1+r_u4)
    ans2 = (0.5*(N2+N3))/(1+r_u3d)
    ans3 = (0.5*(N3+N4))/(1+r_u2d2)
    ans4 = (0.5*(N4+N5))/(1+r_ud3)
    ans5 = (0.5*(N5+N6))/(1+r_d4)
    fans1 = (0.5*(ans1+ans2))/(1+r_u3)
    fans2 = (0.5*(ans2+ans3))/(1+r_u2d)
    fans3 = (0.5*(ans3+ans4))/(1+r_ud2)
    fans4 = (0.5*(ans4+ans5))/(1+r_d3)
    xans1 = (0.5*(fans1+fans2))/(1+r_u2)
    xans2 = (0.5*(fans2+fans3))/(1+r_ud)
    xans3 = (0.5*(fans3+fans4))/(1+r_d2)
    a4ans1 = (0.5*(xans1+xans2))/(1+r_u)
    a4ans2 = (0.5*(xans2+xans3))/(1+r_d)
    y_u4 = math.sqrt(100/ans1) - 1
    y_u3d = math.sqrt(100/ans2) - 1
    y_u2d2 = math.sqrt(100/ans3) - 1
    y_ud3 = math.sqrt(100/ans4) - 1
    y_d4 = math.sqrt(100/ans5) - 1
    out = [((0.5*a4ans1 + 0.5*a4ans2)/(1+r[0]) -a6 )]
    out.append(((0.5 * math.log(y_u4/y_u3d) - df.Vol.iloc[5])))    
    return out

g = fsolve(bdtFive,[0.1,0.1],xtol=1.49012e-20)
#bdtFour([ 0.08048839,  0.15227017])
r_u5 = g[0] * math.exp(10 * g[1])
r_u4d = g[0] * math.exp(8 * g[1])
r_u3d2 = g[0] * math.exp(6 * g[1])
r_u2d3 = g[0] * math.exp(4 * g[1])
r_ud4 = g[0] * math.exp(2 * g[1]) 
r_d5 = g[0]

def bdtSix(x):
    r_u6 = x[0]*math.exp(12 * x[1] )    
    r_u5d = x[0]*math.exp(10 * x[1] )
    r_u4d2 = x[0]*math.exp(8 * x[1] ) 
    r_u3d3 = x[0]*math.exp(6 * x[1]) 
    r_u2d4 = x[0]*math.exp(4 * x[1])
    r_ud5 = x[0]*math.exp(2 * x[1])    
    r_d6 = x[0]  
    N1 = 100/(1+r_u6) 
    N2 = 100/(1+r_u5d)
    N3 = 100/(1+r_u4d2)
    N4 = 100/(1+r_u3d3)
    N5 = 100/(1+r_u2d4)
    N6 = 100/(1+r_ud5)
    N7 = 100/(1+r_d6)
    ans1 = (0.5*(N1+N2))/(1+r_u5)
    ans2 = (0.5*(N2+N3))/(1+r_u4d)
    ans3 = (0.5*(N3+N4))/(1+r_u3d2)
    ans4 = (0.5*(N4+N5))/(1+r_u2d3)
    ans5 = (0.5*(N5+N6))/(1+r_ud4)
    ans6 = (0.5*(N6+N7))/(1+r_d5)
    fans1 = (0.5*(ans1+ans2))/(1+r_u4)
    fans2 = (0.5*(ans2+ans3))/(1+r_u3d)
    fans3 = (0.5*(ans3+ans4))/(1+r_u2d2)
    fans4 = (0.5*(ans4+ans5))/(1+r_ud3)
    fans5 = (0.5*(ans5+ans6))/(1+r_d4)
    xans1 = (0.5*(fans1+fans2))/(1+r_u3)
    xans2 = (0.5*(fans2+fans3))/(1+r_u2d)
    xans3 = (0.5*(fans3+fans4))/(1+r_ud2)
    xans4 = (0.5*(fans4+fans5))/(1+r_d3)
    a4ans1 = (0.5*(xans1+xans2))/(1+r_u2)
    a4ans2 = (0.5*(xans2+xans3))/(1+r_ud)
    a4ans3 = (0.5*(xans3+xans4))/(1+r_d2)
    a5ans1 = (0.5*(a4ans1+a4ans2))/(1+r_u)
    a5ans2 = (0.5*(a4ans2+a4ans3))/(1+r_d)
    y_u5 = math.sqrt(100/ans1) - 1
    y_u4d = math.sqrt(100/ans2) - 1
    y_u3d2 = math.sqrt(100/ans3) - 1
    y_u2d3 = math.sqrt(100/ans4) - 1
    y_ud4 = math.sqrt(100/ans5) - 1
    y_d5 = math.sqrt(100/ans6) - 1
    out = [((0.5*a5ans1 + 0.5*a5ans2)/(1+r[0]) -a7 )]
    out.append(((0.5 * math.log(y_u5/y_u4d) - df.Vol.iloc[6])))    
    return out

g = fsolve(bdtSix,[0.1,0.1],xtol=1.49012e-20)
#bdtFour([ 0.08048839,  0.15227017])
r_u6 = g[0] * math.exp(12 * g[1])
r_u5d = g[0] * math.exp(10 * g[1])
r_u4d2 = g[0] * math.exp(8 * g[1])
r_u3d3 = g[0] * math.exp(6 * g[1])
r_u2d4 = g[0] * math.exp(4 * g[1])
r_ud5 = g[0] * math.exp(2 * g[1]) 
r_d6 = g[0]

def bdtSeven(x):
    r_u7 = x[0]*math.exp(14 * x[1] )
    r_u6d = x[0]*math.exp(12 * x[1] )    
    r_u5d2 = x[0]*math.exp(10 * x[1] )
    r_u4d3 = x[0]*math.exp(8 * x[1] ) 
    r_u3d4 = x[0]*math.exp(6 * x[1]) 
    r_u2d5 = x[0]*math.exp(4 * x[1])
    r_ud6 = x[0]*math.exp(2 * x[1])    
    r_d7 = x[0]  
    N1 = 100/(1+r_u7) 
    N2 = 100/(1+r_u6d)
    N3 = 100/(1+r_u5d2)
    N4 = 100/(1+r_u4d3)
    N5 = 100/(1+r_u3d4)
    N6 = 100/(1+r_u2d5)
    N7 = 100/(1+r_ud6)
    N8 = 100/(1+r_d7)
    ans1 = (0.5*(N1+N2))/(1+r_u6)
    ans2 = (0.5*(N2+N3))/(1+r_u5d)
    ans3 = (0.5*(N3+N4))/(1+r_u4d2)
    ans4 = (0.5*(N4+N5))/(1+r_u3d3)
    ans5 = (0.5*(N5+N6))/(1+r_u2d4)
    ans6 = (0.5*(N6+N7))/(1+r_ud5)
    ans7 = (0.5*(N7+N8))/(1+r_d6)
    fans1 = (0.5*(ans1+ans2))/(1+r_u5)
    fans2 = (0.5*(ans2+ans3))/(1+r_u4d)
    fans3 = (0.5*(ans3+ans4))/(1+r_u3d2)
    fans4 = (0.5*(ans4+ans5))/(1+r_u2d3)
    fans5 = (0.5*(ans5+ans6))/(1+r_ud4)
    fans6 = (0.5*(ans6+ans7))/(1+r_d5)
    xans1 = (0.5*(fans1+fans2))/(1+r_u4)
    xans2 = (0.5*(fans2+fans3))/(1+r_u3d)
    xans3 = (0.5*(fans3+fans4))/(1+r_u2d2)
    xans4 = (0.5*(fans4+fans5))/(1+r_ud3)
    xans5 = (0.5*(fans5+fans6))/(1+r_d4)
    a4ans1 = (0.5*(xans1+xans2))/(1+r_u3)
    a4ans2 = (0.5*(xans2+xans3))/(1+r_u2d)
    a4ans3 = (0.5*(xans3+xans4))/(1+r_ud2)
    a4ans4 = (0.5*(xans4+xans5))/(1+r_d3)
    a5ans1 = (0.5*(a4ans1+a4ans2))/(1+r_u2)
    a5ans2 = (0.5*(a4ans2+a4ans3))/(1+r_ud)
    a5ans3 = (0.5*(a4ans3+a4ans4))/(1+r_d2)
    a6ans1 = (0.5*(a5ans1+a5ans2))/(1+r_u)
    a6ans2 = (0.5*(a5ans2+a5ans3))/(1+r_d)
    y_u6 = math.sqrt(100/ans1) - 1
    y_u5d = math.sqrt(100/ans2) - 1
    y_u4d2 = math.sqrt(100/ans3) - 1
    y_u3d3 = math.sqrt(100/ans4) - 1
    y_u2d4 = math.sqrt(100/ans5) - 1
    y_ud5 = math.sqrt(100/ans6) - 1
    y_d6 = math.sqrt(100/ans7) - 1
    out = [((0.5*a6ans1 + 0.5*a6ans2)/(1+r[0]) -a8 )]
    out.append(((0.5 * math.log(y_u6/y_u5d) - df.Vol.iloc[7])))    
    return out

g = fsolve(bdtSeven,[0.1,0.1],xtol=1.49012e-20)
r_u7 = g[0] * math.exp(14 * g[1])
r_u6d = g[0] * math.exp(12 * g[1])
r_u5d2 = g[0] * math.exp(10 * g[1])
r_u4d3 = g[0] * math.exp(8 * g[1])
r_u3d4 = g[0] * math.exp(6 * g[1])
r_u2d5 = g[0] * math.exp(4 * g[1])
r_ud6 = g[0] * math.exp(2 * g[1]) 
r_d7 = g[0]

def bdtEight(x):
    r_u8 = x[0]*math.exp(16 * x[1] )
    r_u7d = x[0]*math.exp(14 * x[1] )
    r_u6d2 = x[0]*math.exp(12 * x[1] )    
    r_u5d3 = x[0]*math.exp(10 * x[1] )
    r_u4d4 = x[0]*math.exp(8 * x[1] ) 
    r_u3d5 = x[0]*math.exp(6 * x[1]) 
    r_u2d6 = x[0]*math.exp(4 * x[1])
    r_ud7 = x[0]*math.exp(2 * x[1])    
    r_d8 = x[0]  
    N1 = 100/(1+r_u8) 
    N2 = 100/(1+r_u7d)
    N3 = 100/(1+r_u6d2)
    N4 = 100/(1+r_u5d3)
    N5 = 100/(1+r_u4d4)
    N6 = 100/(1+r_u3d5)
    N7 = 100/(1+r_u2d6)
    N8 = 100/(1+r_ud7)
    N9 = 100/(1+r_d8)
    ans1 = (0.5*(N1+N2))/(1+r_u7)
    ans2 = (0.5*(N2+N3))/(1+r_u6d)
    ans3 = (0.5*(N3+N4))/(1+r_u5d2)
    ans4 = (0.5*(N4+N5))/(1+r_u4d3)
    ans5 = (0.5*(N5+N6))/(1+r_u3d4)
    ans6 = (0.5*(N6+N7))/(1+r_u2d5)
    ans7 = (0.5*(N7+N8))/(1+r_ud6)
    ans8 = (0.5*(N8+N9))/(1+r_d7)
    fans1 = (0.5*(ans1+ans2))/(1+r_u6)
    fans2 = (0.5*(ans2+ans3))/(1+r_u5d)
    fans3 = (0.5*(ans3+ans4))/(1+r_u4d2)
    fans4 = (0.5*(ans4+ans5))/(1+r_u3d3)
    fans5 = (0.5*(ans5+ans6))/(1+r_u2d4)
    fans6 = (0.5*(ans6+ans7))/(1+r_ud5)
    fans7= (0.5*(ans7+ans8))/(1+r_d6)
    xans1 = (0.5*(fans1+fans2))/(1+r_u5)
    xans2 = (0.5*(fans2+fans3))/(1+r_u4d)
    xans3 = (0.5*(fans3+fans4))/(1+r_u3d2)
    xans4 = (0.5*(fans4+fans5))/(1+r_u2d3)
    xans5 = (0.5*(fans5+fans6))/(1+r_ud4)
    xans6 = (0.5*(fans6+fans7))/(1+r_d5)
    a4ans1 = (0.5*(xans1+xans2))/(1+r_u4)
    a4ans2 = (0.5*(xans2+xans3))/(1+r_u3d)
    a4ans3 = (0.5*(xans3+xans4))/(1+r_u2d2)
    a4ans4 = (0.5*(xans4+xans5))/(1+r_ud3)
    a4ans5 = (0.5*(xans5+xans6))/(1+r_d4)
    a5ans1 = (0.5*(a4ans1+a4ans2))/(1+r_u3)
    a5ans2 = (0.5*(a4ans2+a4ans3))/(1+r_u2d)
    a5ans3 = (0.5*(a4ans3+a4ans4))/(1+r_ud2)
    a5ans4 = (0.5*(a4ans4+a4ans5))/(1+r_d3)
    a6ans1 = (0.5*(a5ans1+a5ans2))/(1+r_u2)
    a6ans2 = (0.5*(a5ans2+a5ans3))/(1+r_ud)
    a6ans3 = (0.5*(a5ans3+a5ans4))/(1+r_d2)
    a7ans1 = (0.5*(a6ans1+a6ans2))/(1+r_u)
    a7ans2 = (0.5*(a6ans2+a6ans3))/(1+r_d)
    y_u7 = math.sqrt(100/ans1) - 1
    y_u6d = math.sqrt(100/ans2) - 1
    y_u5d2 = math.sqrt(100/ans3) - 1
    y_u4d3 = math.sqrt(100/ans4) - 1
    y_u3d4 = math.sqrt(100/ans5) - 1
    y_u2d5 = math.sqrt(100/ans6) - 1
    y_ud6 = math.sqrt(100/ans7) - 1
    y_d7 = math.sqrt(100/ans8) - 1
    out = [((0.5*a7ans1 + 0.5*a7ans2)/(1+r[0]) -a9 )]
    out.append(((0.5 * math.log(y_u7/y_u6d) - df.Vol.iloc[8])))    
    return out

g = fsolve(bdtEight,[0.1,0.1],xtol=1.49012e-20)
r_u8 = g[0] * math.exp(16 * g[1])
r_u7d = g[0] * math.exp(14 * g[1])
r_u6d2 = g[0] * math.exp(12 * g[1])
r_u5d3 = g[0] * math.exp(10 * g[1])
r_u4d4 = g[0] * math.exp(8 * g[1])
r_u3d5 = g[0] * math.exp(6 * g[1])
r_u2d6 = g[0] * math.exp(4 * g[1])
r_ud7 = g[0] * math.exp(2 * g[1]) 
r_d8 = g[0]

def bdtNine(x):
    r_u9 = x[0]*math.exp(18 * x[1] )
    r_u8d = x[0]*math.exp(16 * x[1] )
    r_u7d2 = x[0]*math.exp(14 * x[1] )
    r_u6d3 = x[0]*math.exp(12 * x[1] )    
    r_u5d4 = x[0]*math.exp(10 * x[1] )
    r_u4d5 = x[0]*math.exp(8 * x[1] ) 
    r_u3d6 = x[0]*math.exp(6 * x[1]) 
    r_u2d7 = x[0]*math.exp(4 * x[1])
    r_ud8 = x[0]*math.exp(2 * x[1])    
    r_d9 = x[0]  
    N1 = 100/(1+r_u9) 
    N2 = 100/(1+r_u8d)
    N3 = 100/(1+r_u7d2)
    N4 = 100/(1+r_u6d3)
    N5 = 100/(1+r_u5d4)
    N6 = 100/(1+r_u4d5)
    N7 = 100/(1+r_u3d6)
    N8 = 100/(1+r_u2d7)
    N9 = 100/(1+r_ud8)
    N10 = 100/(1+r_d9)
    ans1 = (0.5*(N1+N2))/(1+r_u8)
    ans2 = (0.5*(N2+N3))/(1+r_u7d)
    ans3 = (0.5*(N3+N4))/(1+r_u6d2)
    ans4 = (0.5*(N4+N5))/(1+r_u5d3)
    ans5 = (0.5*(N5+N6))/(1+r_u4d4)
    ans6 = (0.5*(N6+N7))/(1+r_u3d5)
    ans7 = (0.5*(N7+N8))/(1+r_u2d6)
    ans8 = (0.5*(N8+N9))/(1+r_ud7)
    ans9 = (0.5*(N9+N10))/(1+r_d8)
    fans1 = (0.5*(ans1+ans2))/(1+r_u7)
    fans2 = (0.5*(ans2+ans3))/(1+r_u6d)
    fans3 = (0.5*(ans3+ans4))/(1+r_u5d2)
    fans4 = (0.5*(ans4+ans5))/(1+r_u4d3)
    fans5 = (0.5*(ans5+ans6))/(1+r_u3d4)
    fans6 = (0.5*(ans6+ans7))/(1+r_u2d5)
    fans7= (0.5*(ans7+ans8))/(1+r_ud6)
    fans8= (0.5*(ans8+ans9))/(1+r_d7)
    xans1 = (0.5*(fans1+fans2))/(1+r_u6)
    xans2 = (0.5*(fans2+fans3))/(1+r_u5d)
    xans3 = (0.5*(fans3+fans4))/(1+r_u4d2)
    xans4 = (0.5*(fans4+fans5))/(1+r_u3d3)
    xans5 = (0.5*(fans5+fans6))/(1+r_u2d4)
    xans6 = (0.5*(fans6+fans7))/(1+r_ud5)
    xans7 = (0.5*(fans7+fans8))/(1+r_d6)
    a4ans1 = (0.5*(xans1+xans2))/(1+r_u5)
    a4ans2 = (0.5*(xans2+xans3))/(1+r_u4d)
    a4ans3 = (0.5*(xans3+xans4))/(1+r_u3d2)
    a4ans4 = (0.5*(xans4+xans5))/(1+r_u2d3)
    a4ans5 = (0.5*(xans5+xans6))/(1+r_ud4)
    a4ans6 = (0.5*(xans6+xans7))/(1+r_d5)
    a5ans1 = (0.5*(a4ans1+a4ans2))/(1+r_u4)
    a5ans2 = (0.5*(a4ans2+a4ans3))/(1+r_u3d)
    a5ans3 = (0.5*(a4ans3+a4ans4))/(1+r_u2d2)
    a5ans4 = (0.5*(a4ans4+a4ans5))/(1+r_ud3)
    a5ans5 = (0.5*(a4ans5+a4ans6))/(1+r_d4)
    a6ans1 = (0.5*(a5ans1+a5ans2))/(1+r_u3)
    a6ans2 = (0.5*(a5ans2+a5ans3))/(1+r_u2d)
    a6ans3 = (0.5*(a5ans3+a5ans4))/(1+r_ud2)
    a6ans4 = (0.5*(a5ans4+a5ans5))/(1+r_d3)
    a7ans1 = (0.5*(a6ans1+a6ans2))/(1+r_u2)
    a7ans2 = (0.5*(a6ans2+a6ans3))/(1+r_ud)
    a7ans3 = (0.5*(a6ans3+a6ans4))/(1+r_d2)
    a8ans1 = (0.5*(a7ans1+a7ans2))/(1+r_u)
    a8ans2 = (0.5*(a7ans2+a7ans3))/(1+r_d)
    y_u8 = math.sqrt(100/ans1) - 1
    y_u7d = math.sqrt(100/ans2) - 1
    y_u6d2 = math.sqrt(100/ans3) - 1
    y_u5d3 = math.sqrt(100/ans4) - 1
    y_u4d4 = math.sqrt(100/ans5) - 1
    y_u3d5 = math.sqrt(100/ans6) - 1
    y_u2d6 = math.sqrt(100/ans7) - 1
    y_ud7 = math.sqrt(100/ans8) - 1
    y_d7 = math.sqrt(100/ans9) - 1
    out = [((0.5*a8ans1 + 0.5*a8ans2)/(1+r[0]) -a10 )]
    out.append(((0.5 * math.log(y_u8/y_u7d) - df.Vol.iloc[9])))    
    return out

g = fsolve(bdtNine,[0.1,0.1],xtol=1.49012e-20)
r_u9 = g[0] * math.exp(18 * g[1]) 
r_u8d = g[0] * math.exp(16 * g[1])
r_u7d2 = g[0] * math.exp(14 * g[1])
r_u6d3 = g[0] * math.exp(12 * g[1])
r_u5d4 = g[0] * math.exp(10 * g[1])
r_u4d5 = g[0] * math.exp(8 * g[1])
r_u3d6 = g[0] * math.exp(6 * g[1])
r_u2d7 = g[0] * math.exp(4 * g[1])
r_ud8 = g[0] * math.exp(2 * g[1]) 
r_d9 = g[0]

def bdtTen(x):
    r_u10 = x[0]*math.exp(20 * x[1] )
    r_u9d = x[0]*math.exp(18 * x[1] )
    r_u8d2 = x[0]*math.exp(16 * x[1] )
    r_u7d3 = x[0]*math.exp(14 * x[1] )
    r_u6d4 = x[0]*math.exp(12 * x[1] )    
    r_u5d5 = x[0]*math.exp(10 * x[1] )
    r_u4d6 = x[0]*math.exp(8 * x[1] ) 
    r_u3d7 = x[0]*math.exp(6 * x[1]) 
    r_u2d8 = x[0]*math.exp(4 * x[1])
    r_ud9 = x[0]*math.exp(2 * x[1])    
    r_d10 = x[0]  
    N1 = 100/(1+r_u10) 
    N2 = 100/(1+r_u9d)
    N3 = 100/(1+r_u8d2)
    N4 = 100/(1+r_u7d3)
    N5 = 100/(1+r_u6d4)
    N6 = 100/(1+r_u5d5)
    N7 = 100/(1+r_u4d6)
    N8 = 100/(1+r_u3d7)
    N9 = 100/(1+r_u2d8)
    N10 = 100/(1+r_ud9)
    N11 = 100/(1+r_d10)
    ans1 = (0.5*(N1+N2))/(1+r_u9)
    ans2 = (0.5*(N2+N3))/(1+r_u8d)
    ans3 = (0.5*(N3+N4))/(1+r_u7d2)
    ans4 = (0.5*(N4+N5))/(1+r_u6d3)
    ans5 = (0.5*(N5+N6))/(1+r_u5d4)
    ans6 = (0.5*(N6+N7))/(1+r_u4d5)
    ans7 = (0.5*(N7+N8))/(1+r_u3d6)
    ans8 = (0.5*(N8+N9))/(1+r_u2d7)
    ans9 = (0.5*(N9+N10))/(1+r_ud8)
    ans10 = (0.5*(N10+N11))/(1+r_d9)
    fans1 = (0.5*(ans1+ans2))/(1+r_u8)
    fans2 = (0.5*(ans2+ans3))/(1+r_u7d)
    fans3 = (0.5*(ans3+ans4))/(1+r_u6d2)
    fans4 = (0.5*(ans4+ans5))/(1+r_u5d3)
    fans5 = (0.5*(ans5+ans6))/(1+r_u4d4)
    fans6 = (0.5*(ans6+ans7))/(1+r_u3d5)
    fans7= (0.5*(ans7+ans8))/(1+r_u2d6)
    fans8= (0.5*(ans8+ans9))/(1+r_ud7)
    fans9= (0.5*(ans9+ans10))/(1+r_d8)
    xans1 = (0.5*(fans1+fans2))/(1+r_u7)
    xans2 = (0.5*(fans2+fans3))/(1+r_u6d)
    xans3 = (0.5*(fans3+fans4))/(1+r_u5d2)
    xans4 = (0.5*(fans4+fans5))/(1+r_u4d3)
    xans5 = (0.5*(fans5+fans6))/(1+r_u3d4)
    xans6 = (0.5*(fans6+fans7))/(1+r_u2d5)
    xans7 = (0.5*(fans7+fans8))/(1+r_ud6)
    xans8 = (0.5*(fans8+fans9))/(1+r_d7)
    a4ans1 = (0.5*(xans1+xans2))/(1+r_u6)
    a4ans2 = (0.5*(xans2+xans3))/(1+r_u5d)
    a4ans3 = (0.5*(xans3+xans4))/(1+r_u4d2)
    a4ans4 = (0.5*(xans4+xans5))/(1+r_u3d3)
    a4ans5 = (0.5*(xans5+xans6))/(1+r_u2d4)
    a4ans6 = (0.5*(xans6+xans7))/(1+r_ud5)
    a4ans7 = (0.5*(xans7+xans8))/(1+r_d6)
    a5ans1 = (0.5*(a4ans1+a4ans2))/(1+r_u5)
    a5ans2 = (0.5*(a4ans2+a4ans3))/(1+r_u4d)
    a5ans3 = (0.5*(a4ans3+a4ans4))/(1+r_u3d2)
    a5ans4 = (0.5*(a4ans4+a4ans5))/(1+r_u2d3)
    a5ans5 = (0.5*(a4ans5+a4ans6))/(1+r_ud4)
    a5ans6 = (0.5*(a4ans6+a4ans7))/(1+r_d5)
    a6ans1 = (0.5*(a5ans1+a5ans2))/(1+r_u4)
    a6ans2 = (0.5*(a5ans2+a5ans3))/(1+r_u3d)
    a6ans3 = (0.5*(a5ans3+a5ans4))/(1+r_u2d2)
    a6ans4 = (0.5*(a5ans4+a5ans5))/(1+r_ud3)
    a6ans5 = (0.5*(a5ans5+a5ans6))/(1+r_d4)
    a7ans1 = (0.5*(a6ans1+a6ans2))/(1+r_u3)
    a7ans2 = (0.5*(a6ans2+a6ans3))/(1+r_u2d)
    a7ans3 = (0.5*(a6ans3+a6ans4))/(1+r_ud2)
    a7ans4 = (0.5*(a6ans4+a6ans5))/(1+r_d3)
    a8ans1 = (0.5*(a7ans1+a7ans2))/(1+r_u2)
    a8ans2 = (0.5*(a7ans2+a7ans3))/(1+r_ud)
    a8ans3 = (0.5*(a7ans3+a7ans4))/(1+r_d2)
    a9ans1 = (0.5*(a8ans1+a8ans2))/(1+r_u)
    a9ans2 = (0.5*(a8ans2+a8ans3))/(1+r_d)
    y_u9 = math.sqrt(100/ans1) - 1
    y_u8d = math.sqrt(100/ans2) - 1
    y_u7d2 = math.sqrt(100/ans3) - 1
    y_u6d3 = math.sqrt(100/ans4) - 1
    y_u5d4 = math.sqrt(100/ans5) - 1
    y_u4d5 = math.sqrt(100/ans6) - 1
    y_u3d6 = math.sqrt(100/ans7) - 1
    y_u2d7 = math.sqrt(100/ans8) - 1
    y_ud8 = math.sqrt(100/ans9) - 1
    y_d9 = math.sqrt(100/ans10) - 1
    out = [((0.5*a9ans1 + 0.5*a9ans2)/(1+r[0]) -a11 )]
    out.append(((0.5 * math.log(y_u9/y_u8d) - df.Vol.iloc[10])))    
    return out

g = fsolve(bdtTen,[0.1,0.1],xtol=1.49012e-20)
r_u10 = g[0] * math.exp(20 * g[1]) 
r_u9d = g[0] * math.exp(18 * g[1]) 
r_u8d2 = g[0] * math.exp(16 * g[1])
r_u7d3 = g[0] * math.exp(14 * g[1])
r_u6d4 = g[0] * math.exp(12 * g[1])
r_u5d5 = g[0] * math.exp(10 * g[1])
r_u4d6 = g[0] * math.exp(8 * g[1])
r_u3d7 = g[0] * math.exp(6 * g[1])
r_u2d8 = g[0] * math.exp(4 * g[1])
r_ud9 = g[0] * math.exp(2 * g[1]) 
r_d10 = g[0]
#Lattice printer not included

