# -*- coding: utf-8 -*-

#%% Definition of the inputs
'''
Input data definition 
'''


from core import User, np
User_list = []

'''
This example input file represents an whole village-scale community,
adapted from the data used for the Journal publication. It should provide a 
complete guidance to most of the possibilities ensured by RAMP for inputs definition,
including specific modular duty cycles and cooking cycles. 
For examples related to "thermal loads", see the "input_file_2".
'''

#Create new user classes
HI = User("high income",100,3)
User_list.append(HI)

HMI = User("higher middle income",320,3)
User_list.append(HMI)

LI = User("low income",230,3)
User_list.append(LI)

Hospital = User("hospital",1)
User_list.append(Hospital)

School = User("school",2)
User_list.append(School)

Public_lighting = User("public lighting",1)
User_list.append(Public_lighting)

Bar = User("bar",1)
User_list.append(Bar)

Tailor = User("tailor",1)
User_list.append(Tailor)

Garage = User("garage",1)
User_list.append(Garage)

Pumps = User("pumps",2)
User_list.append(Pumps)

Carpenter = User("carpenter",2)
User_list.append(Carpenter)

#Create new appliances

#Public lighting
Pub_lights = Public_lighting.Appliance(Public_lighting,n=15,P=30,w=1,fixed='yes',flat='yes') ###????
Pub_lights.windows(w1=[1200,1440],w2=[0,360],r_w=0)

#High-Income
#Lights, security lights, phone charger, more than one TV, 
# fan, fridge, hi-fi stereos, blender Health 
HI_indoor_bulb = HI.Appliance(HI,n=6,P=5,w=2,t=180,r_t=0.3,c=15)
HI_indoor_bulb.windows([1080,1320],[330,390],0.35)

HI_outdoor_bulb = HI.Appliance(HI,n=2,P=10,w=2,flat='yes')
HI_outdoor_bulb.windows([1080,1440],[0,390],0.2)

HI_TV = HI.Appliance(HI,2,50,1,120,0.3,15)
HI_TV.windows([1080,1320],r_w=0.35)

HI_Phone_charger = HI.Appliance(HI,4,8,2,120,0.15,10)#? ch from 30 to 15
HI_Phone_charger.windows([1080,1440],[0,330],0.1) #?

HI_fan = HI.Appliance(HI,2,40,1,120,0.3,20,occasional_use=0.5) #ch from 30 to 20
HI_fan.windows([600,1080],r_w=0.3)

HI_hifi = HI.Appliance(HI,1,60,2,90,0.5,15)
HI_hifi.windows([660,780],[1080,1260],0.35)

HI_Blender = HI.Appliance(HI,1,50,2,20,0.3,3,occasional_use = 0.33) #ch from 5 to 3
HI_Blender.windows([660,780],[1020,1140],0.1)

HI_fridge = HI.Appliance(HI,1,140,1,flat='yes')
HI_fridge.windows([0,1440],r_w=0)

#Higher-Middle Income
HMI_indoor_bulb = HMI.Appliance(HMI,4,5,2,180,0.3,15)
HMI_indoor_bulb.windows([1080,1320],[330,390],0.35)

HMI_TV = HMI.Appliance(HMI,1,50,1,120,0.3,15)
HMI_TV.windows([1080,1320],r_w=0.35)

HMI_Phone_charger = HMI.Appliance(HMI,3,8,2,120,0.15,10)
HMI_Phone_charger.windows([1080,1440],[0,330],0.1) #?

HMI_fan = HMI.Appliance(HMI,1,40,1,120,0.3,20,occasional_use=0.5)
HMI_fan.windows([600,1080],r_w=0.3)

HMI_radio = HMI.Appliance(HMI,1,10,2,90,0.5,15)
HMI_radio.windows([660,960],[1080,1320],0.2)

#Low Income
LI_indoor_bulb = LI.Appliance(LI,3,5,2,180,0.3,15)
LI_indoor_bulb.windows([1080,1320],[330,390],0.35)

LI_Phone_charger = LI.Appliance(LI,2,8,2,120,0.15,10)
LI_Phone_charger.windows([1080,1440],[0,330],0.1) #?

#Hospital
Ho_indoor_bulb = Hospital.Appliance(Hospital,20,5,2,180,0.3,15)
Ho_indoor_bulb.windows([1080,1320],[330,390],0.35)

Ho_outdoor_bulb = Hospital.Appliance(Hospital,2,10,2,flat='yes')
Ho_outdoor_bulb.windows([1080,1440],[0,390],0.2)

Ho_water_heater = Hospital.Appliance(Hospital,1,800,2,60,0.5,20)
Ho_water_heater.windows([480,720],[870,1440],0)

Ho_Sterilizer = Hospital.Appliance(Hospital,n=1,P=1500,w=2,t=60,occasional_use=0.5)
Ho_Sterilizer.windows([480,720],[870,1440],0)

Ho_fridge = Hospital.Appliance(Hospital,1,200,1,flat='yes')
Ho_fridge.windows([0,1440],r_w=0)

Ho_PC = Hospital.Appliance(Hospital,2,200,2,120,0.3,10)
Ho_PC.windows([480,720],[870,1440],0)

Ho_washing_mac = Hospital.Appliance(Hospital,1,500,2,180,0.2,60,occasional_use = 0.5)
Ho_washing_mac.windows([480,720],[870,1440])

#Tailor
Ta_indoor_bulb = Tailor.Appliance(Tailor,2,5,2,240,0.3,60,wd_we_type = 0)
Ta_indoor_bulb.windows([600,720],[900,1080],0.1)

Ta_sewing_mac = Tailor.Appliance(Tailor,1,100,2,240,0.5,30,wd_we_type = 0)
Ta_sewing_mac.windows([600,720],[900,1080],0.1)

#Carpenter
Ca_jigsaw = Carpenter.Appliance(Carpenter,1,2000,2,120,0.3,5,wd_we_type = 0,occasional_use = 0.33) #??
Ca_jigsaw.windows([600,720],[900,1080],0.1)

Ca_driller = Carpenter.Appliance(Carpenter,1,500,2,60,0.5,1,wd_we_type = 0,occasional_use = 0.33)
Ca_driller.windows([600,720],[900,1080],0.1)

Ca_planer = Carpenter.Appliance(Carpenter,1,600,2,60,0.5,5,wd_we_type = 0,occasional_use = 0.33)
Ca_planer.windows([600,720],[900,1080],0.1)

Ca_indoor_bulb = Carpenter.Appliance(Carpenter,2,5,2,240,0.3,60,wd_we_type = 0)
Ca_indoor_bulb.windows([600,720],[900,1080],0.1)

#Garage
Ga_indoor_bulb = Garage.Appliance(Garage,4,5,2,240,0.3,60,wd_we_type = 0)
Ga_indoor_bulb.windows([600,720],[900,1080],0.1)

Ga_welding_mac = Garage.Appliance(Garage,1,1500,2,60,0.5,5,wd_we_type = 0,occasional_use = 0.3)
Ga_welding_mac.windows([600,720],[900,1080],0.1)

#Bar
Ba_indoor_bulb = Bar.Appliance(Bar,3,5,2,240,0.3,60)
Ba_indoor_bulb.windows([960,1260],r_w=0.35)

Ba_fridge = Bar.Appliance(Bar,1,140,1,flat='yes')
Ba_fridge.windows([0,1440],r_w=0)

Ba_hifi = Bar.Appliance(Bar,1,60,2,180,0.3,30)
Ba_hifi.windows([600,720],[900,1260],r_w=0.1)

#Pumps
Pu_pump = Pumps.Appliance(Pumps,2,1500,1,180,0.1,30)
Pu_pump.windows([240,1080],r_w=0.1)

#School
S_indoor_bulb = School.Appliance(School,15,10,1,240,0.3,60,wd_we_type = 0)
S_indoor_bulb.windows([960,1200],r_w=0.2)

S_outdoor_bulb = School.Appliance(School,5,1,10,2,flat='yes')
S_indoor_bulb.windows([1080,1440],r_w=0.1)

S_PC = School.Appliance(School,3,150,2,210,0.1,10)
S_PC.windows([510,750],[810,1080],r_w=0.35)



