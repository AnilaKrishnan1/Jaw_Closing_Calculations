import numpy as np

Fmax = 20377.2293155461 # Fmax - Maximal tetanic force, i.e. physiological cross-sectional area in N/cm^2 
L = 65 # L - Current muscle length in cm
L0 = 56.742237 # L0 - Optimal muscle length for M. adductor mandible externus superficialis muscle cm
FQ = 1 # FQ -  An activation factor
V = 8 # Current velocity 
k = 0.25 #Constant
Muscle_names = ["mames", "mamem", "mamep", "mamp", "mps", "mptd palatine", "mptd ascending", "mptv"]

Moment_arms = [0.36, 0.36, 0.62, 0.36, 0.62, 0.28, 0.28, 0.26]
Muscle_lengths = {
    0: [0.5558085, 0.651961, 0.72138817, 0.4527533333, 0.657911, 0.385, 0.40362, 0.307272],
    13: [0.6839465, 0.7428735, 0.802157, 0.579067,0.754217, 0.4506805, 0.4635885, 0.39409438],
    28: [0.780683,0.8410825,0.888784945,0.510463,0.8010595,0.5226395,0.5787535,0.426121],
    43: [0.814241,0.8800235,0.9761285,0.586734,0.841646,0.584328,0.6253765,0.4968485]
}       
Optimal_length = Muscle_lengths[13] # L0 is based on the optimal length, which is 13 degrees

for angle, lengths in Muscle_lengths.items():
    print("_____________________________________________")
    print("\nJaw angle:", angle, "degrees")
        
    for index, item in enumerate(lengths):
        L0 = Optimal_length[index]*100 # Converts to cm
        Fiber_Length = 0.35*L0 # Converts muscle length to optimal fiber length
        Vmax = 14.6*10*Fiber_Length # Maximum contraction velocity; converts L0 into mm
        L = item*100 # Converts to cm
        FA = -6.25*(L/L0)**2 + 12.5*(L/L0) - 5.25 # FA - A force/ length factor in percentage; 1 = 100%
        FP = 0.0014*np.exp(6*(L-L0)/L0) #  A passive muscle element
        
        if V >= 0:
            FV = (1 - V/Vmax)/(1 + V/(k*Vmax)) # FV - Force/velocity factor
        else:
            FV = 1.8 - 0.8*((1 + V/Vmax)/(1 - 7.56*V/(k*Vmax)))

        Fmuscle = Fmax*(FA*FV*FQ+FP)# Fmuscle - Total muscle force N/mm
        Torque = Fmuscle*Moment_arms[index] 
        
        print(Muscle_names[index])
        print("Fmuscle: " , Fmuscle) 
        print("Torque: ", Torque)
        


