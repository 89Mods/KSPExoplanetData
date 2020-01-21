#Planet Data:
#Inclination- 18
#Eccentricity- 14
#SMA- 10
#LAN- None
#AOP- None
#ReferenceBody- 0
#Name- 2
#Mass- 22
#Radius- 27

#Star Data:
#Name- 0
#Distance- 43
#Temperature- 58
#Mass- 62
#Radius- 66
from random import randint
from random import random
import urllib.request

#https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=csv
def random_float(min, max):
    return random() * (min - max) + max

#Download the data first
response = urllib.request.urlopen('https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=csv')
data = response.read()
f = open("Exoplanets.csv", "wb")
f.write(data);
f.close()

astronomical_unit = 1.496e+10 #AU, adjusted for KSP scale
jupiter_mass = 1.89813e27
jupiter_radius = 7.1492e6     #Rj, adjusted for KSP scale
parsec = 3.0857e14            #PC, adjusted for KSP scale
solar_mass = 1.98847e30
solar_radius = 6.957e7        #Rs, adjusted for KSP scale
f = open("Exoplanets.csv", "r")
output = "Reference Body,Name,LAN,AOP,SMA,Inclination,Eccentricity,Mass,Radius"
output_s = "Name,Distance,Temperature,Mass,Radius"
star_names = []
for line in f.readlines():
    if line.startswith("#"):
        continue
    if line.startswith("pl_hostname"):
        continue
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
    if values[18] == "":
        continue
    else:
        inc = values[18]
    if values[14] == "":
        continue
    else:
        ecc = values[14]
    if values[10] == "":
        continue
    else:
        sma = float(values[10]) * astronomical_unit
    if values[22] == "":
        continue
    else:
        mass = float(values[22]) * jupiter_mass
    if values[27] == "":
        continue
    else:
        rad = float(values[22]) * jupiter_radius
    name = values[2]
    rb = values[0]
    output += f"\n{rb},{name},{lan},{aop},{sma},{inc},{ecc},{mass},{rad}"

    name = values[0]
    if name not in star_names:
        star_names.append(name)
        if values[43] == "":
            continue
        else:
            lan = float(values[43]) * parsec
        if values[58] == "":
            continue
        else:
            rb = float(values[58])
        if values[62] == "":
            continue
        else:
            mass = float(values[62]) * solar_mass
        if values[66] == "":
            continue
        else:
            radius = float(values[66]) * solar_radius
        output_s += f"\n{name},{lan},{rb},{mass},{radius}"
outputf = open("Planets.csv", "w")
outputf.write(output)
f.close()
outputf.close()

outputf = open("Stars.csv", "w")
outputf.write(output_s)
outputf.close()
