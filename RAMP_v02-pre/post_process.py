# -*- coding: utf-8 -*-

#%% Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math as mt

#%% Post-processing 

'''
Just some additional code lines to calculate useful indicators and generate plots
'''
def Profile_formatting(stoch_profiles):
    Profile_avg = np.zeros(1440)
    for pr in stoch_profiles:
        Profile_avg = Profile_avg + pr
    Profile_avg = Profile_avg/len(stoch_profiles)
    
    Profile_kW = []
    for kW in stoch_profiles:
        Profile_kW.append(kW/1000)
    
    Profile_series = np.array([])
    for iii in stoch_profiles:
        Profile_series = np.append(Profile_series,iii)
    
    return (Profile_avg, Profile_kW, Profile_series)

def Profile_formatting_us(stoch_profiles_us):
    
    row = len(stoch_profiles_us) #number of users
    col = len(stoch_profiles_us[0]) #numbers of profiles
    depth = len(stoch_profiles_us[0][0]) #number of periods
    Profile_series_us = np.empty([row,depth*col])
    for i in range(0,row):
        for iii in range(0,depth*col):
            ii = mt.floor(iii/depth)
            k = iii - ii*depth
            Profile_series_us[i][iii] = stoch_profiles_us[i][ii][k]
    
    return np.transpose(Profile_series_us)

def Hourly_profile_us(min_profile_us,control):
    users = len(min_profile_us[0])
    minutes = len(min_profile_us)
    hours = int(minutes/60)
    Hour_profile_us = np.zeros([hours,users])
    Hour_profile = np.zeros([hours])

    for us in range(0,users):
        for h in range(0,hours):
            temp = 0
            var = 0
            for m in range(0,60):
                mi = int(h*60 + m)
                temp += min_profile_us[mi,us]
            if control == 'avg':
                Hour_profile_us[h,us] = temp/60
            elif control == 'var':
                for m in range(0,60):
                    mi = int(h*60 + m)
                    var += (min_profile_us[mi,us] - temp/60)^2
                Hour_profile_us[h,us] = temp/60 + mt.sqrt(var/60)                       
            Hour_profile[h] += Hour_profile_us[h,us]

    return Hour_profile_us, Hour_profile


def Profile_cloud_plot(stoch_profiles,stoch_profiles_avg):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    for n in stoch_profiles:
        plt.plot(np.arange(1440),n,'#b0c4de')
        plt.xlabel('Time (hours)')
        plt.ylabel('Power (W)')
        plt.ylim(ymin=0)
        #plt.ylim(ymax=5000)
        plt.margins(x=0)
        plt.margins(y=0)
    plt.plot(np.arange(1440),stoch_profiles_avg,'#4169e1')
    plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
    #plt.savefig('profiles.eps', format='eps', dpi=1000)
    plt.show()


def Profile_cloud_tot(stoch_profiles,stoch_profiles_avg):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    colors= [['#C0C0C0','#696969'],['#b0c4de','#4169e1'],['#90EE90','#006400'],['#FFFFE0','#BDB76B'],['#FFD700','#FF8C00'],['#FF6347','#8B0000']]

#    color.cycle_map(len(stoch_profiles[0]))
    for i in range(0,len(stoch_profiles)):
        for n in stoch_profiles[i]:
            plt.plot(np.arange(1440),n,colors[i][0])
            plt.xlabel('Time (hours)')
            plt.ylabel('Power (W)')
            plt.ylim(ymin=0)
            plt.ylim(ymax=150000)
            plt.margins(x=0)
            plt.margins(y=0)
        plt.plot(np.arange(1440),stoch_profiles_avg[i],colors[i][1])
        plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
        plt.savefig('profiles.png', format='png', dpi=1000)
    plt.show()



def Profile_series_plot(stoch_profiles_series):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    plt.plot(np.arange(len(stoch_profiles_series)),stoch_profiles_series,'#4169e1')
    #plt.xlabel('Time (hours)')
    plt.ylabel('Power (W)')
    plt.ylim(ymin=0)
    #plt.ylim(ymax=5000)
    plt.margins(x=0)
    plt.margins(y=0)
    #plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
    #plt.savefig('profiles.eps', format='eps', dpi=1000)
    plt.show()
    


#%% Export individual profiles
'''
for i in range (len(Profile)):
    np.save('p0%d.npy' % (i), Profile[i])
'''

# Export Profiles

def export_series(stoch_profiles_series ,j):
    series_frame = pd.DataFrame(stoch_profiles_series)
    series_frame.to_csv('results/output_file_%d.csv' % (j))

def export_series_us(stoch_profiles_series, string, j): #PIETRO: parallel function for exporting in csv the differentiated demand
    series_frame = pd.DataFrame(stoch_profiles_series)
    series_frame.to_csv("results/%s_%d.csv" %(string,j))

def complete_demand(scen,years,steps,n_input,tot_list):
    Final_demand = np.zeros([8760,scen*years])
    ind_h = len(tot_list[0])
    if len(steps) != n_input-1:
        print("steps are uncorrect! they have to be of size n_input-1")
        return
    steps.insert(0,0)
    steps.append(years+1)
    st = len(steps)
    delta_t = int(np.floor(8760/ind_h))
     
    for sc in range(0,scen):
        for y in range(0,years):
            for j in range(0,st-1):
                
                if steps[j]<= y <steps[j+1]:
                    for i in range(0,delta_t):
                        Final_demand[i*ind_h:(i+1)*ind_h,sc*years+y] = tot_list[sc*n_input + j][:]
                    if (i+1)*ind_h < (8760-1):
                        Final_demand[(i+1)*ind_h:,sc*years+y] = tot_list[sc*n_input + j][:8760-(i+1)*ind_h ]

    series_frame = pd.DataFrame(Final_demand)
    series_frame.to_csv("Demand.csv")
           
    return Final_demand