# -*- coding: utf-8 -*-

#%% Initialisation of a model instance
'''
The model is ready to be initialised
'''
User_list = [] #creates an empty list to store all the needed User classes
num_profiles = int(input("please indicate the number of profiles to be generated: ")) #asks the user how many profiles (i.e. code runs) he wants
print('Please wait...') 
Profile = [] #creates an empty list to store the results of each code run, i.e. each stochastically generated profile

from inputs import*

#%% Calibration parameters
'''
Calibration parameters. These can be changed in case the user has some real data against which the model can be calibrated
They regulate the probabilities defining the largeness of the peak window and the probability of coincident switch-on within the peak window
'''
peak_enlarg = 0 #percentage random enlargement or reduction of peak time range length
mu_peak = 0.5 #median value of gaussian distribution [0,1] by which the number of coincident switch_ons is randomly selected
s_peak = 1 #standard deviation (as percentage of the median value) of the gaussian distribution [0,1] above mentioned

