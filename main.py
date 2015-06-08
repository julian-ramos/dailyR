import numpy as np

# filename='/Users/julian/Documents/data/data'
filename='/Users/julian/Downloads/casas_dataset/11/data_copy'

data=[]
label=[]
date=[]
sensor=[]
state=[]
participant=[]
tempday=[]
day=[]
hour=[]
label=[]
sensor_state=[]
label_state=[]
user=[]

file=open(filename)
for i in file.readlines():
    temp=i.strip('\t').split()
    if len(temp)>4:
        tempday=temp[0].split()[0]
        if tempday not in day:
            print(tempday)
            day.append(tempday)
#         day.append(temp[0])
        hour.append(temp[1])
        sensor.append(temp[2])
        sensor_state.append(temp[3])
        label.append(temp[4][3:])
        user.append(temp[4][1])
        label_state.append(temp[5])
#         participant.append(temp[3][1])
        
        
#Data extraction works nicely
#As a next step create a database on
#sqlite in which  Im going to start storing
#everysingle database I have, maybe I can host that database on the dropbox
#folder that way I will have access to all of the datasets from anywhere
#anytime
        
        
        
#Now I need to transform those dates
#into the circle representation
#I have a function for that on utilityFuncs

print('number of different days used')
print(len(day))



file.close()