""" Python Code to Solve the Linear Advection Equation using CTST

Setting initial conditions as a bell curve

"""

import numpy as np # External library for numerical calculations
import matplotlib.pyplot as plt # Plotting library


# Function defining the initial and analytical solution (advection depends on the initital conditions, represented as a bell)
def initialBell(x):
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)


# Put everything inside a main function to avoid global variables 

def main ():
    # Setup space, initial phi (advection) profile and Courant number
    nx = 40        # Number of points in space
    c = 0.2        # The Courant number 
    # Spatial variable going from zero to one inclusive 
    x = np.linspace(0.0, 1.0, nx+1)
    # Three time levels of the dependent variable, phi
    phi = initialBell(x)
    phiNew = phi.copy()
    phiOld = phi.copy()


    #FTCS for the first time-step, looping over space
    for j in range (1, nx):
        phi[j] = phiOld[j] - 0.5*c*(phiOld[j+1] - phiOld[j-1])
    # apply periodic boundary conditions
    phi[0] = phiOld[0] - 0.5*c*(phiOld[1] - phiOld[nx-1])
    phi[nx] = phi[0]



    # Loop over remaining time-steps (nt) using CTCS
    
    
    nt = 40
    for n in range(1, nt):
        # loop over space
        for j in range(1, nx):
            phiNew[j] = phiOld[j] - c*(phi[j+1] - phi[j-1])
        # apply periodic boundary conditions 
        phiNew[0] = phiOld[0] - c*(phi[1] - phi[nx-1])
        phiNew[nx] = phiNew[0]
        #update phi for the next timestep
        phiOld= phi.copy()
        phi= phiNew.copy()
        
    # derived quantities 
    u = 1.
    dx = 1./nx
    dt = c*dx/u
    t = nt*dt
    
    
    # Plot the solution in comparison to the analytic solution 
    plt.plot(x, initialBell(x- u*t), 'k', label='analytic')
    plt.plot(x, phi, 'b', label='CTCS')
    plt.legend(loc ='best')
    plt.ylabel('$\phi$')
    plt.axhline(0, linestyle= ':', color='black')
    plt.show()
        
#Execute the code
main()           
