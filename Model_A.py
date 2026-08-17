import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Model A: Code for graphing exits 

# Load CSV files to dataframes
A_MF = pd.read_csv('Exits_A_MF.csv', header=None)
A_Sim = pd.read_csv('Exits_A_Sim.csv', header=None)

#Adjust figure size
plt.figure(figsize=(12,5))

# First panel (Healthy)
plt.subplot(1,3,1)

# Column 0 values are the values of lambda for the carrier income protocol
# Column 1 values are mean exit populations of healthy individuals
plt.plot(A_MF[0],A_MF[1],color='green',label='Mean field')
plt.scatter(A_Sim[0],A_Sim[1],color='green',label='Numerical simulation')
plt.xlabel('Parameter λ for the carrier income protocol.')
plt.ylabel('Mean exit population of healthy individuals.')
plt.legend()

# Second panel (Carrier)
plt.subplot(1,3,2)
plt.title('Open two-state semi-Markov model with two entry points and two exit points.')

# Column 0 values are the values of lambda for the carrier income protocol
# Column 2 values are mean exit populations of carrier individuals
plt.plot(A_MF[0],A_MF[2],color='red',label='Mean field')
plt.scatter(A_Sim[0],A_Sim[2],color='red',label='Numerical simulation')
plt.xlabel('Parameter λ for the carrier income protocol.')
plt.ylabel('Mean exit population of carrier individuals.')
plt.legend()

# Third panel (Infected)
plt.subplot(1,3,3)

# Column 0 values are the values of lambda for the carrier income protocol
# Column 3 values are mean exit populations of infected individuals
plt.plot(A_MF[0],A_MF[3],color='orange',label='Mean field')
plt.scatter(A_Sim[0],A_Sim[3],color='orange',label='Numerical simulation')
plt.xlabel('Parameter λ for the carrier income protocol.')
plt.ylabel('Mean exit population of infected individuals.')
plt.legend()
#plt.subplot(3,2,6)


plt.tight_layout()
plt.show()
