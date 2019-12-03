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
for j in range(1,2):
    (Profiles_list,Profiles_list_us) = Stochastic_Process(j)  #PIETRO
    
# Post-processes the results and generates plots
    Profiles_avg, Profiles_list_kW, Profiles_series = Profile_formatting(Profiles_list)
    Profiles_series_us = Profile_formatting_us(Profiles_list_us) # PIETRO
    Profiles_series_hour = Hourly_profile_us(Profiles_series_us)
    Profile_series_plot(Profiles_series) #by default, profiles are plotted as a series
    tot_list.append(Profiles_series_hour)
    
    export_series(Profiles_series,j)
    export_series_us(Profiles_series_us,"minutes",j) #PIETRO
    export_series_us(Profiles_series_hour,"hours",j)

    if len(Profiles_list) > 1: #if more than one daily profile is generated, also cloud plots are shown
        Profile_cloud_plot(Profiles_list, Profiles_avg)
'''
#WIP
Complete_hour = make_seasonal_dataframe(tot_list,[0,1],5,[])
export_series_us(Complete_hour,"complete")
'''