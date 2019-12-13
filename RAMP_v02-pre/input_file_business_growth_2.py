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

Bar = User("bar",2)
User_list.append(Bar)

Tailor = User("tailor",1)
User_list.append(Tailor)

Garage = User("garage",1)
User_list.append(Garage)

Pumps = User("pumps",2)
User_list.append(Pumps)

Carpenter = User("carpenter",1)
User_list.append(Carpenter)

#Create new appliances
Internet_point = User("internet point",1)
User_list.append(Internet_point)

Grocery_store = User("grociery store",1)
User_list.append(Grocery_store)

Haircutter = User("haircutter",1)
User_list.append(Haircutter)

Generic_business = User("generic business",1)
User_list.append(Generic_business)

#Create new appliances

#Public lighting
Pub_lights = Public_lighting.Appliance(Public_lighting,n=130,P=60,w=1,fixed='yes',flat='yes') 

#High-Income
#Lights, security lights, phone charger, more than one TV, 
# fan, fridge, hi-fi stereos, blender Health 
HI_indoor_bulb = HI.Appliance(HI,n=8,P=7,w=1,t=180,r_t=0.3,c=15)
HI_indoor_bulb.windows([1080,1320],r_w=0.2)

HI_indoor_bulb2 = HI.Appliance(HI,6,7,1,20,0.2,5)
HI_indoor_bulb2.windows([330,390],r_w=0.1)

HI_outdoor_bulb = HI.Appliance(HI,n=2,P=10,w=2,fixed='yes',flat='yes')
HI_outdoor_bulb.windows([1080,1440],[0,390],0.1)

HI_TV = HI.Appliance(HI,2,80,1,120,0.3,15)
HI_TV.windows([1080,1320],r_w=0.1)

HI_TV2 = HI.Appliance(HI,2,80,1,60,0.2,5,occasional_use=0.5)
HI_TV2.windows([720,980],r_w=0.1)

HI_Phone_charger = HI.Appliance(HI,4,8,2,120,0.15,10)
HI_Phone_charger.windows([1080,1440],[0,330],0.1) 

HI_fan = HI.Appliance(HI,2,40,1,120,0.3,20,occasional_use=0.5) 
HI_fan.windows([600,1080],r_w=0.2)

HI_hifi = HI.Appliance(HI,1,40,2,90,0.5,15,thermal_P_var=0.3)
HI_hifi.windows([660,780],[1080,1260],0.3)

HI_Blender = HI.Appliance(HI,1,50,2,20,0.3,1,occasional_use = 0.5) 
HI_Blender.windows([600,720],[1020,1140],0.1)

HI_Freezer = HI.Appliance(HI,1,140,1,1440,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,20,5,10)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#Higher-Middle Income
HMI_indoor_bulb = HMI.Appliance(HMI,6,7,2,180,0.3,15)
HMI_indoor_bulb.windows([1080,1320],r_w=0.2)

HMI_indoor_bulb2 = HMI.Appliance(HMI,4,7,2,20,0.2,5)
HMI_indoor_bulb2.windows([330,390],r_w=0.1)

HMI_TV = HMI.Appliance(HMI,1,50,1,120,0.3,15)
HMI_TV.windows([1080,1320],r_w=0.1)

HMI_TV2 = HMI.Appliance(HMI,2,50,1,60,0.2,5,occasional_use=0.5)
HMI_TV2.windows([720,980],r_w=0.1)

HMI_Phone_charger = HMI.Appliance(HMI,3,8,2,120,0.15,10)
HMI_Phone_charger.windows([1080,1440],[0,330],0.1)

HMI_fan = HMI.Appliance(HMI,1,40,1,120,0.3,20,occasional_use=0.5)
HMI_fan.windows([600,1080],r_w=0.3)

HMI_radio = HMI.Appliance(HMI,1,20,2,90,0.5,15)
HMI_radio.windows([660,960],[1080,1320],0.3)

#Low Income
LI_indoor_bulb = LI.Appliance(LI,3,7,2,180,0.3,15)
LI_indoor_bulb.windows([1080,1320],[330,390],0.2)

LI_indoor_bulb2 = LI.Appliance(LI,2,7,2,20,0.2,5)
LI_indoor_bulb2.windows([330,390],r_w=0.1)

LI_Phone_charger = LI.Appliance(LI,2,8,2,120,0.15,10)
LI_Phone_charger.windows([1080,1440],[0,330],0.1) #?

#Hospital
Ho_indoor_bulb = Hospital.Appliance(Hospital,40,20,2,360,0.3,30)
Ho_indoor_bulb.windows([480,780],[870,1440],0.05)

Ho_outdoor_bulb = Hospital.Appliance(Hospital,4,10,2,fixed='yes',flat='yes')
Ho_outdoor_bulb.windows([1080,1440],[0,390],0.1)

Ho_water_heater = Hospital.Appliance(Hospital,1,600,2,180,0.3,30,thermal_P_var=0.3)
Ho_water_heater.windows([480,780],[870,1440],0.05)

Ho_Sterilizer = Hospital.Appliance(Hospital,n=1,P=1500,w=2,t=60,c=60,occasional_use=0.5)
Ho_Sterilizer.windows([480,780],[870,1440],0.05)

Ho_Freezer = Hospital.Appliance(Hospital,1,200,1,1440,0,30,'yes',3)
Ho_Freezer.windows([0,1440],[0,0])
Ho_Freezer.specific_cycle_1(200,20,5,10)
Ho_Freezer.specific_cycle_2(200,15,5,15)
Ho_Freezer.specific_cycle_3(200,10,5,20)
Ho_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

Ho_PC = Hospital.Appliance(Hospital,2,200,2,120,0.3,30)
Ho_PC.windows([480,780],[870,1440],0.05)

Ho_washing_mac = Hospital.Appliance(Hospital,1,500,2,180,0.2,60,fixed_cycle=1,occasional_use = 0.5)
Ho_washing_mac.windows([480,780],[870,1440],0)
Ho_washing_mac.specific_cycle_1(2000,10,10,50)
Ho_washing_mac.cycle_behaviour([600,780],[900,1080])

#Tailor
Ta_indoor_bulb = Tailor.Appliance(Tailor,6,10,2,300,0.3,30,wd_we_type = 0)
Ta_indoor_bulb.windows([600,780],[900,1080],0.05)

Ta_sewing_mac = Tailor.Appliance(Tailor,1,100,2,240,0.5,30,wd_we_type = 0)
Ta_sewing_mac.windows([600,780],[900,1080],0.05)

#Carpenter
Ca_jigsaw = Carpenter.Appliance(Carpenter,1,2000,2,120,0.5,5,wd_we_type = 0,occasional_use = 0.5) 
Ca_jigsaw.windows([600,780],[900,1080],0.05)

Ca_driller = Carpenter.Appliance(Carpenter,1,1500,2,90,0.5,1,wd_we_type = 0)
Ca_driller.windows([600,780],[900,1080],0.05)

Ca_planer = Carpenter.Appliance(Carpenter,1,600,2,60,0.5,5,wd_we_type = 0)
Ca_planer.windows([600,780],[900,1080],0.05)

Ca_indoor_bulb = Carpenter.Appliance(Carpenter,6,10,2,300,0.3,30,wd_we_type = 0)
Ca_indoor_bulb.windows([600,780],[900,1080],0.05)

#Garage
Ga_indoor_bulb = Garage.Appliance(Garage,10,10,2,300,0.3,30,wd_we_type = 0)
Ga_indoor_bulb.windows([600,780],[900,1080],0.05)

Ga_welding_mac = Garage.Appliance(Garage,1,1500,2,120,0.5,5,wd_we_type = 0,occasional_use = 0.5)
Ga_welding_mac.windows([600,780],[900,1080],0.05)

#Bar
Ba_indoor_bulb = Bar.Appliance(Bar,6,10,2,300,0.3,30)
Ba_indoor_bulb.windows([660,1440],r_w=0.05)

Ba_Freezer = Bar.Appliance(Bar,1,140,1,1440,0,30,'yes',3)
Ba_Freezer.windows([0,1440],[0,0])
Ba_Freezer.specific_cycle_1(200,20,5,10)
Ba_Freezer.specific_cycle_2(200,15,5,15)
Ba_Freezer.specific_cycle_3(200,10,5,20)
Ba_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

Ba_hifi = Bar.Appliance(Bar,1,60,1,300,0.3,30,thermal_P_var=0.3)
Ba_hifi.windows([660,1440],r_w=0.05)

#Pumps
Pu_pump = Pumps.Appliance(Pumps,2,1500,1,300,0.2,30)
Pu_pump.windows([240,1200],r_w=0.1)

#School
S_indoor_bulb = School.Appliance(School,30,20,2,360,0.3,30,wd_we_type = 0)
S_indoor_bulb.windows([540,720],[840,1200],r_w=0.05)

S_outdoor_bulb = School.Appliance(School,5,10,2,fixed='yes',flat='yes')
S_outdoor_bulb.windows([1080,1440],[0,390],r_w=0.1)

S_PC = School.Appliance(School,3,150,2,210,0.1,10)
S_PC.windows([540,720],[840,1200],r_w=0.05)

S_Pr = School.Appliance(School,1,150,2,20,0.5,2)
S_Pr.windows([540,720],[840,1200],r_w=0.05)



