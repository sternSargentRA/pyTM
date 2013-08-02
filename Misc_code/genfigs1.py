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
tol = 1e-6
dist = 10
i = 0
maxiter = 1e8
c_step = 1e-5

# Constant parameters
bet = 0.95
gam = 2.0
delt = 0.2
alpha = 0.33
A = 1.0

# These are the exogenous parameters (Need to be vector bc they might differ)
# Since they are all 0 we just left them as 0, but in more general cases they
# could be different

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
    Parameters:
    -----------
    kval: scalar - The value of k in a period

    Outputs:
    --------
    out: scalar - The value of output for a given level of capital

    This takes a value of k and gives the value of output
    '''
    A = 1.
    alpha = .33

    out = A * kval**(alpha)
    return out


def calcMU(cval):
    '''
    Parameters:
    -----------
    cval: scalar - The value of c in a period

    Outputs:
    --------
    mu: scalar - The marginal utility at a certain level of consumption

    This take a value for consumption and returns MU of C
    '''
    gam = 2.0

    mu = cval**(-gam)

    return mu


def calccplus(choy, kman):
    '''
    Parameters:
    -----------
    choy: scalar - The value of consumption in a period (today)
    kman: scalar - The value of capital tomorrow

    Outputs:
    --------
    cman: scalar - The value of consumption for tomorrow given c today and k
    k tomorrow

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
    Parameters:
    -----------
    khoy: scalar - The value of k in a given period
    choy: scalar - The value of c in a given period
    ghoy: scalar - The value of g in a given period

    Outputs:
    --------
    kman: scalar - The value of k tomorrow given the parameters above today

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

# This will be our guess at where the path for c should start given the
# first period level of capital is at 1.5
cguess = .604

# This loops performs the shooting algorithm: See RMT (Sargent and Ljungqvist)
while dist > tol and i < maxiter:
    i += 1

    # Get matrices to fill with values
    Knewmat = np.zeros(periods)
    Cnewmat = np.zeros(periods)

    # Give the first period levels of capital and consumption
    Knewmat[0] = 1.5
    Cnewmat[0] = cguess

    # Given the above we can calculate the level of k tomorrow
    Knewmat[1] = calckplus(Knewmat[0], Cnewmat[0], g[0])

    # We simulate out to 100 periods
    for t in xrange(periods - 2):
        kt = Knewmat[t]
        ktp = Knewmat[t+1]
        ct = Cnewmat[t]

        ctp = calccplus(ct, ktp)
        Cnewmat[t+1] = ctp
        Knewmat[t+2] = calckplus(ktp, ctp, g[t+1])

        # Since we are working on a finite grid, if we are within a certain
        # level of tolerance of the ss then just set the level of capital equal
        # to the ss
        if Knewmat[t+2] - kbar2 < tol:
            Knewmat[t+2] = kbar2

    # Calculate distance between solution and steady state
    dist = Knewmat[-1] - kbar1

    # If too big then make cguess bigger if too small then make it smaller
    if dist >= 0:
        cguess = cguess + c_step
    else:
        cguess = cguess - c_step

#-----------------------------------------------------------------------------#
#------------------Solve for necessary Variables------------------------------#
#-----------------------------------------------------------------------------#

# These are from formulas in RMT 4
bigR = (1. + taucss)/(1. + taucss) * \
       ((1. - taukss)*(alpha * A * Knewmat**(alpha - 1) - delt) + 1.)
bigRbar = (1. + taucss)/(1. + taucss) * \
          ((1. - taukss)*(alpha * A * kbar1**(alpha - 1) - delt) + 1.) \
    * np.ones(40)
eta = alpha * A * Knewmat**(alpha - 1.)
etabar = alpha * A * kbar1**(alpha-1.) * np.ones(40)

#-----------------------------------------------------------------------------#
#-----------------------------Make Plots--------------------------------------#
#-----------------------------------------------------------------------------#

fig = plt.figure()
# Make plot of capital
ax1 = fig.add_subplot(231)
ax1.plot(Knewmat[:40], 'k', label=r'$k_t$', linewidth=2.)
ax1.plot(range(40), np.ones(40) * kbar1, 'k--', label=r'$\bar{k}$')
ax1.set_xlabel('Time (t)')
ax1.set_xticks([0., 20., 40.])
ax1.set_ybound((1.4, 2.2))
ax1.legend(loc=0)
ax1.set_title(r'$k$')

# Make plot of consumption
ax2 = fig.add_subplot(232)
ax2.plot(Cnewmat[:40], 'k', label=r'$c_t$', linewidth=2.)
ax2.plot(range(40), np.ones(40) * cbar1, 'k--', label=r'$\bar{c}$')
ax2.set_xlabel('Time (t)')
ax2.set_xticks([0., 20., 40.])
ax2.set_ybound((.4, .66))
ax2.legend(loc=0)
ax2.set_title(r'$c$')

# Make plot of bigR
ax3 = fig.add_subplot(233)
ax3.plot(bigR[:40], 'k', label=r'$R_t$', linewidth = 2.)
ax3.plot(range(40), bigRbar, 'k--', label=r'$\bar{R}$', linewidth=2.)
ax3.set_xlabel('Time (t)')
ax3.set_xticks([0., 20., 40.])
ax3.set_ybound((1., 1.1))
ax3.legend(loc=0)
ax3.set_title(r'$R$')

# Make plot of eta
ax4 = fig.add_subplot(234)
ax4.plot(eta[:40], 'k', label=r'$\eta_t$', linewidth=2.)
ax4.plot(range(40), etabar, 'k--', label=r'$\bar{\eta}$', linewidth=2.)
ax4.set_xlabel('Time (t)')
ax4.set_xticks([0., 20., 40.])
ax4.set_ybound((.2, .27))
ax4.legend(loc=0)
ax4.set_title(r'$\eta$')

# Make plot of government spending
ax5 = fig.add_subplot(235)
ax5.plot(g[:40], 'k', label=r'$g_t$', linewidth=2.)
ax5.plot(range(40), np.ones(40)*.2, 'k--', label=r'$\bar{g}$', linewidth=2.)
ax5.set_xlabel('Time (t)')
ax5.set_xticks([0., 20., 40.])
ax5.set_ybound((0, .5))
ax5.legend(loc=0)
ax5.set_title(r'$g$')

fig.suptitle('Fig 11.9.1 RMT 4')
plt.show()

