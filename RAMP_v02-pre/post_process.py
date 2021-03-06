# -*- coding: utf-8 -*-

#%% Import required libraries
import matplotlib.pyplot as plt
import numpy as np
from stochastic_process import Profile

#%% Post-processing
'''
Just some additional code lines to calculate useful indicators and generate plots
'''

Profile_avg = np.zeros(1440)
for pr in Profile:
    Profile_avg = Profile_avg + pr
Profile_avg = Profile_avg/len(Profile)
Profile_avg_kW = Profile_avg/1000

Profile_kW = []
for kW in Profile:
    Profile_kW.append(kW/1000)

Profile_series = np.array([])
for iii in Profile:
    Profile_series = np.append(Profile_series,iii)

x = np.arange(0,1440,5)
plt.figure(figsize=(10,5))
for n in Profile:
    plt.plot(np.arange(1440),n,'#b0c4de')
    plt.xlabel('Time (hours)')
    plt.ylabel('Power (W)')
    plt.ylim(ymin=0)
    #plt.ylim(ymax=5000)
    plt.margins(x=0)
    plt.margins(y=0)
plt.plot(np.arange(1440),Profile_avg,'#4169e1')
plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
#plt.savefig('profiles.eps', format='eps', dpi=1000)
plt.show()


#%% Export individual profiles
'''
for i in range (len(Profile)):
    np.save('p0%d.npy' % (i), Profile[i])
'''
