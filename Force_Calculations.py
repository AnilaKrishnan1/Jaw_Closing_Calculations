import numpy as np

Fmax = 20377.2293155461 # Fmax - Maximal tetanic force, i.e. physiological cross-sectional area in N/cm^2
L = 65 # L - Current muscle length in cm
L0 = 56.742237 # L0 - Optimal muscle length for M. adductor mandible externus superficialis muscle cm
Fiber_Length = 0.35*L0 # Converts muscle length to optimal fiber length
FQ = 1 # FQ -  An activation factor
Vmax = 14.6*10*Fiber_Length # Maximum contraction velocity; converts L0 into mm
V = 8 # Current velocity 
k = 0.25 #Constant

muscles = [0.5558085]
           #,0.651961,0.72138817,0.4527533333,0.657911,0.385,0.40362,0.307272]

for index, item in enumerate(muscles):
    L0 = muscles[index]*100
    FA = -6.25*(L/L0)**2 + 12.5*(L/L0) - 5.25 # FA - A force/ length factor in percentage; 1 = 100%
    FP = 0.0014*np.exp(6*(L-L0)/L0) #  A passive muscle element
    if V >= 0:
        FV = (1 - V/Vmax)/(1 + V/(k*Vmax)) # FV - Force/velocity factor
    else:
        FV = 1.8 - 0.8*((1 + V/Vmax)/(1 - 7.56*V/(k*Vmax)))

    Fmuscle = Fmax*(FA*FV*FQ+FP) # Fmuscle - Total muscle force
    print("L0: ", L0)
    print("FA: ", FA)
    print("FV: " , FV)
    print("FP: " , FP)
    print("Fmuscle: " , Fmuscle)


