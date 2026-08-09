import numpy as np


Fmax = 30 # Fmax - Maximal tetanic force, i.e. physiological cross-sectional area in N/cm^2
L = 10 # L - Current muscle length
L0 = 1 # L0 - Optimal muscle length
FQ = 1 # FQ -  An activation factor
Vmax = 10 # Maximum contraction velocity
V = 8 # Current velocity 
k = 0.25 #Constant

FA = -6.25*(L/L0)**2 + 12.5*(L/L0) - 5.25 # FA - A force/ length factor in percentage; 1 = 100%
FP = 0.0014*np.exp(6*(L-L0)/L0) #  A passive muscle element
if V >= 0:
    FV = (1 - V/Vmax)/(1 + V/(k*Vmax)) # FV - Force/velocity factor
else:
    FV = 1.8 - 0.8*((1 + V/Vmax)/(1 - 7.56*V/(k*Vmax)))

Fmuscle = Fmax*(FA*FV*FQ+FP) # Fmuscle - Total muscle force

print("FA: ", FA)
print("FV: " , FV)
print("FP: " , FP)
print("Fmuscle: " , Fmuscle)


