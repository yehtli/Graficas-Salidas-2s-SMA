import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Comparative graphs for models A and B

# Load CSV files to dataframes
A_MF = pd.read_csv('Exits_A_MF.csv', header=None)
A_Sim = pd.read_csv('Exits_A_Sim.csv', header=None)
B_MF = pd.read_csv('Exits_B_MF.csv', header=None)
B_Sim = pd.read_csv('Exits_B_Sim.csv', header=None)

#adjust figure size
plt.figure(figsize=(14,6))

#First panel (Healthy)
plt.subplot(1,3,1)

# Model A
plt.plot(A_MF[0],A_MF[1],color='green',label='Mean field model A')
plt.scatter(A_Sim[0],A_Sim[1],color='green',label='Numerical simulation model A')
# Model B
plt.plot(B_MF[0],B_MF[1],color='blue',label='Mean field model B')
plt.scatter(B_Sim[0],B_Sim[1],color='blue',label='Numerical simulation model B')
# Axis labels
plt.xlabel('Parameter λ for the carrier income protocol.')
plt.ylabel('Mean exit population of healthy individuals.')
plt.legend()
#plt.subplot(3,2,2)

#Second panel (Carrier)
plt.subplot(1,3,2)
plt.title('Comparative of mean exit populations for models A and B')
#Model A
plt.plot(A_MF[0],A_MF[2],color='red',label='Mean field model A')
plt.scatter(A_Sim[0],A_Sim[2],color='red',label='Numerical simulation model A')
#Model B
plt.plot(B_MF[0],B_MF[2],color='blue',label='Mean field model B')
plt.scatter(B_Sim[0],B_Sim[2],color='blue',label='Numerical simulation model B')

plt.xlabel('Parameter λ for the carrier income protocol.')
plt.ylabel('Mean exit population of carrier individuals.')
plt.legend()

# Third panel (Infected)

plt.subplot(1,3,3)
#Model A
plt.plot(A_MF[0],A_MF[3],color='orange',label='Mean field model A')
plt.scatter(A_Sim[0],A_Sim[3],color='orange',label='Numerical simulation model A')
#Model B
plt.plot(B_MF[0],B_MF[3],color='blue',label='Mean field model B')
plt.scatter(B_Sim[0],B_Sim[3],color='blue',label='Numerical simulation model B')

# Axis labels
plt.xlabel('Parameter λ for the carrier income protocol.')
plt.ylabel('Mean exit population of infected individuals.')

plt.tight_layout()
plt.show()
