"""
This file contains the examples as presented in the Linear State Models
of Time Series on the Sargent-Starchurski website/materials

TODO: Write better intro later
"""
import numpy
import scipy.signal as sig


#----------------------------------------------------------------------#
#----------------------------------------------------------------------#
# Examples
#----------------------------------------------------------------------#
#----------------------------------------------------------------------#

# All examples will use these parameters
num_sims = 1
len_sims = 5000
time_unit = 1.0


#----------------------------------------------------------------------#
# Second-order difference equation
#----------------------------------------------------------------------#

# Take parameters as given
sode_alpha = 1.0
sode_rho1 = .9
sode_rho2 = .5

# Define the numerator and denominator
num = [sode_alpha]
den = [1., -sode_rho1, -sode_rho2]



#----------------------------------------------------------------------#
# Univariate Autoregressive Processes
# y_{t+1} = \alpha_1 y_t + \alpha_2 y_{t-1} + \alpha_3 y_{t-2}
#           + \alpha_4 y_{t-3}
#----------------------------------------------------------------------#

# Take parameters as given
uar_alpha1 = .5
uar_alpha2 = 0.3
uar_alpha3 = -0.5
uar_alpha4 = -0.3

# Define the initial condition, numerator and denominator
uar_x0 = 10.
uar_num = [1.]
uar_den = [1., -uar_alpha1, -uar_alpha2, -uar_alpha3, -uar_alpha4]

uar_simulations = np.zeros((num_sims, len_sims))
uar_sys = (uar_num, uar_den, time_unit)

# Use num and den to do simulation
for i in xrange(num_sims):
    # Draw the epsilon shocks
    uar_eps = np.random.randn(len_sims-1, 1)

    # this stores the discrete impluse response
    t_out, y = sig.dlsim(uar_sys, uar_eps, x0=uar_x0)

    # store x0 in the first position and from position 1:T-1 store the computed impulse repsonse
    uar_simulations[i,0],uar_simulations[i,1:]=uar_x0,y.T

plt.plot(y)
plt.plot(uar_eps)
plt.show()
