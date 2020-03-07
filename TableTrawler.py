#Planet Data:
#Inclination- 21
#Eccentricity- 16
#SMA- 6
#LAN- None
#AOP- None
#ReferenceBody- 0
#Name- 2
#Mass- 26
#Radius- 32

#Star Data:
#Name- 0
#Distance- 52
#Temperature- 64
#Mass- 73
#Radius- 74
from random import randint
from random import random
from random import seed
import urllib.request

seed(239723535)
def random_float(min, max):
    return random() * (min - max) + max

#Download the data first
response = urllib.request.urlopen('https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=csv')
data = response.read()
f = open("Exoplanets.csv", "wb")
f.write(data);
f.close()

astronomical_unit = 1.496e+10 #AU, adjusted for KSP scale
jupiter_mass = 1.89813e25     #Mj, adjusted for KSP scale
jupiter_radius = 7.1492e6     #Rj, adjusted for KSP scale
parsec = 3.0857e14            #PC, adjusted for KSP scale
solar_mass = 1.98847e28       #Ms, adjusted for KSP scale
solar_radius = 6.957e7        #Rs, adjusted for KSP scale
f = open("Exoplanets.csv", "r")
output = "Reference Body,Name,LAN,AOP,SMA,Inclination,Eccentricity,Mass,Radius"
output_a = "Reference Body,Name,LAN,AOP,SMA,Inclination,Eccentricity,Mass,Radius";
output_s = "Name,Distance,Temperature,Mass,Radius"
star_names = []
for line in f.readlines():
    if line.startswith("#"):
        continue
    if line.startswith("pl_hostname"):
        continue
    is_complete = True
    values = line.split(",")
    name = ""
    lan = round(random_float(0, 360), 1)
    aop = round(random_float(0, 15), 1)
    sma = ""
    rb = ""
    inc = ""
    ecc = ""
    mass = ""
    rad = ""
    if values[21] == "":
        is_complete = False
    else:
        inc = float(values[21]) - 90
    if values[16] == "":
        is_complete = False
    else:
        ecc = values[16]
    if values[6] == "":
        is_complete = False
    else:
        sma = float(values[6]) * astronomical_unit
    if values[26] == "":
        is_complete = False
    else:
        mass = float(values[26]) * jupiter_mass
    if values[32] == "":
        is_complete = False
    else:
        rad = float(values[32]) * jupiter_radius
    name = values[2]
    rb = values[0]
    s = ""
    if inc != "":
        s = "%.2f" % inc
    output_a += f"\n{rb},{name},{lan},{aop},{sma},{s},{ecc},{mass},{rad}"
    if is_complete:
        output += f"\n{rb},{name},{lan},{aop},{sma},{s},{ecc},{mass},{rad}"
    
    name = values[0]
    if name not in star_names:
        star_names.append(name)
        if values[52] == "":
            continue
        else:
            lan = float(values[52]) * parsec
        if values[64] == "":
            continue
        else:
            rb = float(values[64])
        if values[73] == "":
            continue
        else:
            mass = float(values[73]) * solar_mass
        if values[74] == "":
            continue
        else:
            radius = float(values[74]) * solar_radius
        output_s += f"\n{name},{lan},{rb},{mass},{radius}"
outputf = open("Planets.csv", "w")
outputf.write(output)
f.close()
outputf.close()

outputf = open("Planets_All.csv", "w")
outputf.write(output_a)
outputf.close()

outputf = open("Stars.csv", "w")
outputf.write(output_s)
outputf.close()
