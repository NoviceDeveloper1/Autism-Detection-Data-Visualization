import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Phenotypic_V1_0b_preprocessed1.csv')
control = df[df.DX_GROUP==2]
print len(control.index)
aut = df[df.DX_GROUP==1]
print len(aut.index)
comm_control = control[control.ADI_R_SOCIAL_TOTAL_A!=-9999]
comm_aut = aut[aut.ADI_R_SOCIAL_TOTAL_A!=-9999]
comm_aut1 = aut[aut.ADOS_SOCIAL!=-9999]
comm_aut2 = aut[aut.ADOS_GOTHAM_SOCAFFECT!=-9999]
comm_aut3 = aut[aut.VINELAND_SOCIAL_STANDARD!=-9999]
print len(comm_control)
print len(comm_aut)
print len(comm_aut1)
print len(comm_aut2)
print len(comm_aut3)
comm_control = comm_control['ADI_R_SOCIAL_TOTAL_A']
comm_aut = comm_aut['ADI_R_SOCIAL_TOTAL_A']
comm_aut1 = comm_aut1['ADOS_SOCIAL']
comm_aut2 = comm_aut2['ADOS_GOTHAM_SOCAFFECT']
comm_aut3 = comm_aut3['VINELAND_SOCIAL_STANDARD']

#print(bmi_control)
#plt.plot(comm_control, 'b')
plt.plot(np.arange(505), comm_aut, 'ro')

plt.plot(np.arange(524), comm_aut1, 'g^')

plt.plot(np.arange(487), comm_aut2, 'bs')

plt.plot(np.arange(529), comm_aut3, 'c*')

plt.axis([-10,530,-1,120])
#plt.axis([-10,524,-1,10])
plt.ylabel('SOCIAL INTERACTION')
plt.show()


#plot between all the social interaction scores available in the attributes