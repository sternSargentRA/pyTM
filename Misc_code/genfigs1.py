import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import scipy.optimize as opt

#-----------------------------------------------------------------------------#
#------------------------Perfect Foresight------------------------------------#
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#-------------------------Set the parameters----------------------------------#
#-----------------------------------------------------------------------------#

# Simulation parameters
periods = 100
tol = 1e-9
dist = 10
i = 0
maxiter = 1000
c_step = .001

# Constant parameters
bet = 0.95
gam = 2.0
delt = 0.2
alpha = 0.33
A = 1.0

# These are the exogenous parameters (Need to be vector bc they might differ)
# tauc = np.zeros(periods)
# taui = np.zeros(periods)
# tauk = np.zeros(periods)
tauc = 0.
taui = 0.
tauk = 0.
g = np.ones(periods)*0.4  # gov spends .4 in all but first 9 periods
g[:9] = np.ones(9)*.2

#-----------------------------------------------------------------------------#
#-------------------Define Certain Useful Functions---------------------------#
#-----------------------------------------------------------------------------#


def prodfunc(kval):
    '''
    This takes a value of k and gives the value of output
    '''
    A = 1.
    alpha = .33

    out = A * kval**(alpha)
    return out


def calcMU(cval):
    '''
    This take a value for consumption and returns MU of C
    '''
    gam = 2.0

    MU = cval**(-gam)

    return MU


def calccplus(choy, kman):
    '''
    takes vals and calculates tomorrow's c
    '''
    tauc = 0.
    tauk = 0.
    bet = .95
    alpha = .33
    delt = .2

    num = calcMU(choy)
    den = (bet * (1 + tauc)/(1 + tauc)) * \
          ((1 - tauk) * (alpha * A * kman**(alpha - 1) - delt) + 1)

    cman = (den/num) ** (1./gam)

    return cman


def calckplus(khoy, choy, ghoy):
    '''
    takes vals and calculates tomorrow's k
    '''
    delt = .2

    kman = prodfunc(khoy) + (1 - delt) * khoy - ghoy - choy

    return kman

#-----------------------------------------------------------------------------#
#--------------------Instantiate and run simulations--------------------------#
#-----------------------------------------------------------------------------#

# We can solve steady state by hand and get:
taukss = 0.
taucss = 0.
tauiss = 0.

kbar1 = ((1. / bet - 1 + delt - delt * taukss) / (alpha * A - alpha * A * taukss)) ** (1 / (alpha - 1))
gbar1 = .2
cbar1 = prodfunc(kbar1) + (1. - delt) * kbar1 - kbar1 - gbar1

kbar2 = kbar1
gbar2 = .4
cbar2 = prodfunc(kbar2) + (1. - delt) * kbar2 - kbar2 - gbar2

cguess = .6

while dist > tol and i < maxiter:
    i += 1

    Knewmat = np.zeros(periods)
    Cnewmat = np.zeros(periods)

    Knewmat[0] = kbar1
    Cnewmat[0] = cguess

    Knewmat[1] = calckplus(Knewmat[0], Cnewmat[0], g[0])

    for t in xrange(periods - 2):
        kt = Knewmat[t]
        ktp = Knewmat[t+1]
        ct = Cnewmat[t]

        ctp = calccplus(ct, ktp)
        Cnewmat[t+1] = ctp
        Knewmat[t+2] = calckplus(ktp, ctp, g[t+1])

        print('t', t)

    dist = Knewmat[-1] - kbar1

    if dist >= 0:
        cguess = cguess + c_step
    else:
        cguess = cguess - c_step

    print i

