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
    Hour_profile = np.zeros([hours,users])

    for us in range(0,users):
        for h in range(0,hours):
            temp = 0
            var = 0
            for m in range(0,60):
                mi = int(h*60 + m)
                temp += min_profile_us[mi][us]
            if control == 'avg':
                Hour_profile[h][us] = temp/60
            elif control == 'var':
                for m in range(0,60):
                    mi = int(h*60 + m)
                    var += (min_profile_us[mi][us] - temp/60)^2
                Hour_profile[h][us] = temp/60 + mt.sqrt(var/60)                       
    

    return Hour_profile


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
    series_frame.to_csv("results/%s%d.csv" %(string,j))


def make_seasonal_dataframe(dataframe_list,season_list,years,years_expansion):

    number_seasons = len(season_list)
    number_expansions = len(years_expansion)
    check1 = sum(season_list)
    check2 = number_seasons*number_expansions

    row = 8760
    col = years*(len(dataframe_list[0])+1)
    complete = np.empty([row, col]) 

    for i in range(0,row):
        for j in range(0,col):
            for k in range(1,number_seasons):
                if season_list[k-1] <= i < season_list[k]:
                    complete[i][j] = dataframe_list[k-1][i%24][j%years]

    return complete

#def create_excel()