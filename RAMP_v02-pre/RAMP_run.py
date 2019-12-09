# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:35:00 2019
This is the code for the open-source stochastic model for the generation of 
multi-energy load profiles in off-grid areas, called RAMP, v.0.2.1-pre.

@authors:
- Francesco Lombardi, Politecnico di Milano
- Sergio Balderrama, Université de Liège
- Sylvain Quoilin, KU Leuven
- Emanuela Colombo, Politecnico di Milano

Copyright 2019 RAMP, contributors listed above.
Licensed under the European Union Public Licence (EUPL), Version 1.1;
you may not use this file except in compliance with the License.

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations
under the License.
"""

#%% Import required modules

from stochastic_process import Stochastic_Process
from post_process import*

# Calls the stochastic process and saves the result in a list of stochastic profiles
# In this default example, the model runs for 2 input files ("input_file_1", "input_file_2"),
# but single or multiple files can be run restricting or enlarging the iteration range 
# and naming further input files with progressive numbering

tot_list = []
tot_list_us = []
avgs = []
lists = []
control = 'avg' #avg for average hourly load (optimistic), var for adding variance 
us_call = int(input("please indicate the number of indipendent days you wanna generate for each input profile. Thanks bro!\n"))
control1 = input("you wanna run all scenarios?(y/n)\n")

sc = 0
n_input = 4 #number of input files per scenario + 1 
start = 1

if control1 == 'y':    
    scenarios = ['baseline', 'income_growth', 'business_growth'] 
elif control1 == 'n':
    scenario = input("please indicate the scenario you wanna run: baseline, income_growth, business_growth:\n")
    scenarios = [scenario]
    control2 = input("you wanna run all inputs file? y for yes, number of the input (single) file you wanna run otherwise\n")
    if control2 != 'y':
        n_input = int(control2)
        start = n_input

print("please wait, my man... a lot.")
  

for scenario in scenarios:
    print("starting to process scenario %s" %(scenario))
    for j in range(start,n_input+1):
        print("starting to process profile %s" %(j))
        (Profiles_list,Profiles_list_us) = Stochastic_Process(j,us_call,scenario)  #PIETRO
        lists.append(Profiles_list)
        # Post-processes the results and generates plots
        Profiles_avg, Profiles_list_kW, Profiles_series = Profile_formatting(Profiles_list)
        avgs.append(Profiles_avg)
        Profiles_series_us = Profile_formatting_us(Profiles_list_us) # PIETRO
        (Profiles_series_hour_us,Profiles_series_hour) = Hourly_profile_us(Profiles_series_us,control) 
#        Profile_series_plot(Profiles_series) #by default, profiles are plotted as a series
        tot_list_us.append(Profiles_series_hour_us)
        tot_list.append(Profiles_series_hour)
        
#        export_series(Profiles_series,j)
#        export_series_us(Profiles_series_us,"minutes",j) #PIETRO
#        export_series_us(Profiles_series_hour_us,"hours",j)
        
#        if len(Profiles_list) > 1: #if more than one daily profile is generated, also cloud plots are shown
#            Profile_cloud_plot(Profiles_list, Profiles_avg)          
        print("profile %s is complete" %(j))
    print("scenario %s is complete" %(scenario))
    Profile_cloud_tot(lists[int(sc*(n_input)):int((n_input*(sc+1)))], avgs[int(sc*(n_input)):int(n_input*(sc+1))])
    sc += 1
    
#generating complete Demand file
C_dem = complete_demand(len(scenarios),20,[2,8,14],n_input,tot_list)