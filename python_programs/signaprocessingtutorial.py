# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:08:33 2013

@author: anmol
"""

# a small tip for matlab habits. 
# For python shapes are tuples. 
#So if you generated a matrix of ones

# in matlab : ones(r,c)
# in python : np.ones((r,c))




import scipy.signal as sig
import numpy as np
import pylab

NumSim=100           # Number of paths
T=50                 # Length of sample 

LagNum=[1.0 ,0.0]               #Lag polynomial numerator
LagDen=[1.0 ,-0.9]                  #Lag polynomial denominator
dt=1.0                # time interval
x0=100                # initial condition

# define a tuple sys to store the linear system
sys=(LagNum,LagDen,dt)


# Define an np array with zeros 
Simulations=np.zeros((NumSim,T))

for i in range(NumSim):
   
    # generate the impulse of length T-1 as we will store the first element as the intial condition   
    u=np.random.normal(0,1,(T-1,1))
    
    # this stores the discrete impluse response
    t_out,y=sig.dlsim(sys,u,x0=x0)
    # store x0 in the first position and from position 1:T-1 store the computed impulse repsonse
    Simulations[i,0],Simulations[i,1:]=x0,y.T
    # this is an prettier way of assigining multiple stuff  x=1,y=2 is equivalent to x,y=1,2

## ----------------------------------------------------------------------------------------------
#  Compute means and standard deviations
muhat=Simulations.mean(0) 
#pylab.plot.figure(1)
#pylab.plot(muhat.T)
#pylab.show() 
# unconditional means
sighat=Simulations.std(0) 
 # unconditional stds
# plots the simulations
pylab.plot(Simulations.T)
pylab.show()
