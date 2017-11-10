import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Phenotypic_V1_0b_preprocessed1.csv')
control = df[df.DX_GROUP==2]
print len(control.index)
aut = df[df.DX_GROUP==1]
print len(aut.index)
age_anat_control = control[control.AGE_AT_MPRAGE!=-9999]
age_anat_aut = aut[aut.AGE_AT_MPRAGE!=-9999]
print len(age_anat_control)
print len(age_anat_aut)
age_anat_control = age_anat_control['AGE_AT_MPRAGE']
age_anat_aut = age_anat_aut['AGE_AT_MPRAGE']
#print(age_anat_control)
plt.plot(age_anat_control, 'b')
plt.plot(age_anat_aut, 'r')
plt.ylabel('AGE_AT_MPRAGE')
plt.show()

#plot for Age at anatomical scan (in years) for control and autistic people