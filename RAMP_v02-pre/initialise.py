# -*- coding: utf-8 -*-

#%% Initialisation of a model instance

from core import np
import importlib


def yearly_pattern():
    '''
    Definition of a yearly pattern of weekends and weekdays, in case some appliances have specific wd/we behaviour
    '''
    #Yearly behaviour pattern
    Year_behaviour = np.zeros(365)
    Year_behaviour[5:365:7] = 1
    Year_behaviour[6:365:7] = 1
    
    return(Year_behaviour)

def Initialise_model(number_users):
    '''
    The model is ready to be initialised
    '''
    Profile = [] #creates an empty list to store the results of each code run, i.e. each stochastically generated profile
    Profile_users = [[] for i in range (number_users)]

    return (Profile, Profile_users)
    
def Initialise_inputs(j):
    Year_behaviour = yearly_pattern()
    user_list = getattr((importlib.import_module('input_file_%s_%d' %(scenario,j))), 'User_list')   
    
    # Calibration parameters
    '''
    Calibration parameters. These can be changed in case the user has some real data against which the model can be calibrated
    They regulate the probabilities defining the largeness of the peak window and the probability of coincident switch-on within the peak window
    '''
    peak_enlarg = 0 #percentage random enlargement or reduction of peak time range length
    mu_peak = 0.5 #median value of gaussian distribution [0,1] by which the number of coincident switch_ons is randomly selected
    s_peak = 1 #standard deviation (as percentage of the median value) of the gaussian distribution [0,1] above mentioned

    return (peak_enlarg, mu_peak, s_peak, Year_behaviour, user_list)

