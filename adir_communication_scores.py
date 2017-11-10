import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Phenotypic_V1_0b_preprocessed1.csv')
control = df[df.DX_GROUP==2]
print len(control.index)
aut = df[df.DX_GROUP==1]
print len(aut.index)
comm_control = control[control.ADI_R_VERBAL_TOTAL_BV!=-9999]
comm_aut = aut[aut.ADI_R_VERBAL_TOTAL_BV!=-9999]
print len(comm_control)
print len(comm_aut)
comm_control = comm_control['ADI_R_VERBAL_TOTAL_BV']
comm_aut = comm_aut['ADI_R_VERBAL_TOTAL_BV']
#print(bmi_control)
#plt.plot(comm_control, 'b')
plt.plot(np.arange(506), comm_aut, 'ro')
plt.axis([-10,507,-1,30])
plt.ylabel('ADI_R_VERBAL_TOTAL_BV')
plt.show()
