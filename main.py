
import matplotlib
import numpy as np
import dataOps as dO
import dataStats as dS
import matplotlib.pylab as plt
import math
import pydot as pd
import graph_tool.all as gt
from PIL import Image

import networkx as nx   

from warnings import catch_warnings
from PIL import Image
from graph_tool.draw.gtk_draw import interactive_window
# filename='/Users/julian/Documents/data/data'


#This data set times look normal but the format for the labels is like that for cairo
filename='/Users/julian/Documents/casas_dataset/aruba/data'


#This dataset timestamps look normal but the format is different for the user, labels etc
# filename='/Users/julian/Documents/casas_dataset/cairo/data'

#<<< THis data set timestamps look strange but that seems to be simply because
#the people this data was recorded from seems like they work every day
#This is why we do not seem the complete circle
# filename='/Users/julian/Documents/casas_dataset/twor.2010/data' 


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
#             print(tempday)
            day.append(tempday)
#         day.append(temp[0])
        hour.append(temp[1])
        sensor.append(temp[2])
        sensor_state.append(temp[3])
        label.append(temp[4]+" "+temp[5])
        
#         user.append(temp[4][1])
#         print(label[-1],user[-1])
#         label_state.append(temp[5])
#         participant.append(temp[3][1])

#     print('erase later the next like')
#     if len(label)>100:
#         break
        
        
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

hours=[]
minutes=[]
seconds=[]
for i in hour:
    temp=i.split(":")
    hours.append(int(temp[0]))
    minutes.append(int(temp[1]))
    seconds.append(float(temp[-1]))


timevecs=dO.time2vecHM(hours, minutes)

x=[i[0] for i in timevecs]
y=[i[1] for i in timevecs]

# plt.plot(x,y,'.',alpha=0.01)
# plt.show()

"""
To have in mind
Since the labels have start and end points we can actually have those as separate
states, either that or labeling all the data in between as the given activity. That 
however seems wasteful and maybe the results are the same????



Here is an idea on how to model this idea
A Big difficulty on modeling this data comes 
from the fact that we have both discrete and 
continuous data it does not seem to exist and 
HMM that can model both however. What about using 
the time and any other contextual information
as the observations, then learn an HMM on that and 
later identify what states are based on the labels 
for activities that we have. This ideally will find 
that some activities happen at different times of the day
but those that are not too far away from each other will be 
captured in the same state. Once we have states in this manner
we will have a PGM that we can observe for analysis

Another idea of course would be to create an HMM that can learn both

Another problem with HMMs comes of course from calculating the right number of states




"""

nodes=dS.unique(label)

#Constructing a graph out of the labels
#networkx code which does not produce very nice graphs

# 
# G=nx.MultiDiGraph()
# for i in nodes:
#     G.add_node(i)
# 
# 
# weights={}
# for i in range(len(label)-1):
#     if label[i]+label[i+1] not in weights.keys():
#         weights[label[i]+label[i+1]]=1
#     else:
#         weights[label[i]+label[i+1]]=weights[label[i]+label[i+1]]+1
#     G.add_weighted_edges_from([(label[i],label[i+1],weights[label[i]+label[i+1]])])
# #     G.edge(label[i],label[i+1])
#     
# for i in weights.keys():
#     print(i,weights[i]) 
# 
#   
# try:
#     pos=nx.graphviz_layout(G,prog='neato')
#     print("using graphviz")
# except:
#     print("using networkx")
#     pos=nx.spring_layout(G,k=1,iterations=300)
#    
#       
#         
# nx.draw(G,pos=pos,with_labels=True)
# # nx.draw_graphviz(G, prog='neato')
#  
# plt.show()
# 
# # G.render("graph.svg")
    
#Pydot code
g = pd.Dot(graph_type='digraph')
 
for i in nodes:
    tmpNode=pd.Node(i)
    g.add_node(tmpNode)
    
 
edges={'list':{},'weights':[],'edgeObj':{}}

for i in range(len(label)-1):
    if label[i]+label[i+1] not in edges['list'].keys():
        edges['list'][label[i]+label[i+1]]=1
        tmpEdge = pd.Edge(label[i],label[i+1])
#         tmpEdge.set_weight=
        g.add_edge(tmpEdge)
        
     
g.write_png('example1_graph.png')

#This one is actually pretty good but need to add some way to visualize the weights



# #Graph tool code
# g=gt.Graph(directed=True)
# nodeName=g.new_vertex_property("string")
# weights=g.new_edge_property("float")
# 
# nodesDict={}
# for i in nodes:
#     nodesDict[i]=g.add_vertex()
#     nodeName[nodesDict[i]]=i
#     
# edges={'list':{},'weights':[],'edgeObj':{}}
# for i in range(len(label)-1):
#     if label[i]+label[i+1] not in edges['list'].keys():
#         edges['list'][label[i]+label[i+1]]=1
#         tmpEdge=g.add_edge(nodesDict[label[i]],nodesDict[ label[i+1]])
#         weights[tmpEdge]=1
#         edges['edgeObj'][label[i]+label[i+1]]=tmpEdge
#         
#     else:
#         edges['list'][label[i]+label[i+1]]+=1
#         weights[edges['edgeObj'][label[i]+label[i+1]]]+=1
#         
# #Normalizing weights
# w=[]
# for i in edges['edgeObj']:
#     w.append(weights[edges['edgeObj'][i]])
#     
#     
# # plt.hist(w)
# # plt.show()
#     
# print(w)    
# maxWeight=max(w)
# for i in edges['edgeObj']:
#     weights[edges['edgeObj'][i]]=weights[edges['edgeObj'][i]]/maxWeight
# #     print(weights[edges['edgeObj'][i]]/maxWeight)
# 
#             
#     
# # pos=gt.sfdp_layout(g,eweight=weights)    
# # pos=gt.fruchterman_reingold_layout(g,weight=weights)
# pos=gt.arf_layout(g, weight=weights)
# 
# gt.graph_draw(g,
#               pos,
#               vcmap=matplotlib.cm.jet, 
#               vertex_text=nodeName,
#               vertex_size=1,
#               vertex_font_size=20,
#               vertex_color=[1,1,1,0],
#               edge_pen_width=1,
#               edge_marker_size=10,
#               output_size=(2000, 2000), 
#               output="arf-layout.pdf")
# 
# # gt.graphviz_draw(g,output="two-nodes.pdf")
# 
# 
# 
# 
# # a=Image.open("two-nodes.pdf")
# # a.show()



#Use MeanShift to cluster the labels and make them into a new
#label and then use those on the 

print("done")


