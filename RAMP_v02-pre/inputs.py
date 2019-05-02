# -*- coding: utf-8 -*-

#%% Definition of the inputs
'''
Input data definition (this is planned to be externalised in a yaml or similar file)
'''

import pandas as pd

from core import User, np
from initialise import User_list
from province_iter import p

#%% Inputs definition

T_in_DHW = pd.read_csv('Inlet Water Temperatures.csv', index_col=0, sep=';')
T_out_DHW = 48

#Yearly behaviour pattern
Year_behaviour = np.zeros(365)

for i in range (round(len(Year_behaviour)/7)):
    
    Year_behaviour[7*i+5:7*i+7] = 1

#User classes definition
MONOU3 = User("Single-family house, User 1",2)
User_list.append(MONOU3)

#Appliances definition

#Single Family House, User 1
MONOU3_shower_P = 4186*5.4/60*(np.ones((365,103))*T_out_DHW-T_in_DHW.values[:,:])
#MONOU3_shower_P[0:7] = [11300,10000,5000,2000,20000,11300,3000]

MONOU3_shower1 = MONOU3.Appliance(MONOU3,1,MONOU3_shower_P[:,p],2,10,0.5,2, wd_we_type = 0)
MONOU3_shower1.windows([6*60,9*60],[18*60,23*60],0.33)

MONOU3_shower2 = MONOU3.Appliance(MONOU3,1,MONOU3_shower_P[:,p],2,10,0.5,2, wd_we_type = 1)
MONOU3_shower2.windows([7*60,23*60],[0,0],0.33)

MONOU3_bathbasin_P = 4186*4.3/60*(np.ones((365,103))*T_out_DHW-T_in_DHW.values[:,:])

MONOU3_bathbasin1 = MONOU3.Appliance(MONOU3,1,MONOU3_bathbasin_P[:,p],1,6,0.5,1, wd_we_type = 0)
MONOU3_bathbasin1.windows([6*60,9*60],[18*60,23*60],0.05)

MONOU3_bathbasin2 = MONOU3.Appliance(MONOU3,1,MONOU3_bathbasin_P[:,p],1,6,0.5,1, wd_we_type = 1)
MONOU3_bathbasin2.windows([7*60,23*60],[0,0],0.05)

MONOU3_kitchenbasin_P = 4186*4.5/60*(np.ones((365,103))*T_out_DHW-T_in_DHW.values[:,:])

MONOU3_kitchenbasin1 = MONOU3.Appliance(MONOU3,1,MONOU3_kitchenbasin_P[:,p],1,6.5,0.5,1, wd_we_type = 0)
MONOU3_kitchenbasin1.windows([6*60,9*60],[18*60,23*60],0.05)

MONOU3_kitchenbasin2 = MONOU3.Appliance(MONOU3,1,MONOU3_kitchenbasin_P[:,p],1,6.5,0.5,1, wd_we_type = 1)
MONOU3_kitchenbasin2.windows([7*60,23*60],[0,0],0.05)