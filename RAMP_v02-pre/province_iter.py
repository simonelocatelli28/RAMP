# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:54:10 2019

@author: Locatelli
"""

import numpy as np

profile = np.zeros((365*60*24,103))

for p in range(2):
    
    from RAMP_run import Profile_series
    profile[:len(Profile_series),p] = Profile_series