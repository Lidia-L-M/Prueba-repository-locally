# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:12:06 2025

@author: Lidia (from Marc's initial code')
This code creates single points in txt format to use in trigger form in the UV pulsed laser
The txt lines must be added to a dxf file that already makes single points
because the initialitation commands are missing (use prova.dxf)
lenght conversion: step of 50 equals to 25um in the dxf file for these step motors
"""


f = open('matrix_1mm_sep_10um.txt','w')
linies = []

x = 100000 #intial position
y = 100000

square_size=1000 #units in um (1mm)
separation_between_holes= 10 # 25um between holes
lenght_conversion= 50/25 # 50 steps are 25 um

holes_line= int(square_size/separation_between_holes) #number of holes per line
sep= separation_between_holes*lenght_conversion #separation between holes in step motors units

for i in range(holes_line):
    for j in range(holes_line):
        linies.append(str('JS #INPOS('+str(x+sep*i)+','+str(y+sep*j))+',0)')
        linies.append(str('JS #DRAW(0)'))
linies.append('EN')        

for l in linies:
    f.write(l)
    f.write('\n')
f.close()

#%%

f = open('square_1mm_sep3um.txt','w')
linies = []

x = 100000 #intial position
y = 100000

square_size=1000 #units in um (1mm)
separation_between_holes= 3 # 25um between holes
lenght_conversion= 50/25 # 50 steps are 25 um

holes_line= int(square_size/separation_between_holes) #number of holes per line
sep= separation_between_holes*lenght_conversion #separation between holes in step motors units



for j in range(holes_line):
    linies.append(str('JS #INPOS('+str(x)+','+str(y+sep*j))+',0)')
    linies.append(str('JS #DRAW(0)'))
for j in range(holes_line):
    linies.append(str('JS #INPOS('+str(x+sep*holes_line)+','+str(y+sep*j))+',0)')
    linies.append(str('JS #DRAW(0)'))
for j in range(holes_line):
    linies.append(str('JS #INPOS('+str(x+sep*j)+','+str(y))+',0)')
    linies.append(str('JS #DRAW(0)'))
for j in range(holes_line):
    linies.append(str('JS #INPOS('+str(x+sep*j)+','+str(y+sep*holes_line))+',0)')
    linies.append(str('JS #DRAW(0)'))
    
    
linies.append('EN')        

for l in linies:
    f.write(l)
    f.write('\n')
f.close()
