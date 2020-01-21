# KSP Exoplanet Data
Orbital information for real exoplanets, converted to KSP scale for use in Kopernicus.
Data sourced from the NASA Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/index.html

This repository contains two main tables in csv format: Planets.csv and Stars.csv
Planets.csv contains the following columns:

Column Name | Description
----------- | -----------
Reference Body|The planet's host star
Name|The planet's name
LAN|Longitude of Ascending Node, in degrees
AOP|Argument of Periapsis
SMA|Semi-Major Axis, in meters, 1/10th real scale
Inclination|Orbital Inclination, in degrees
Eccentricity|Eccentricity
Mass|The planet's mass, in kilograms
Radius|The planet's radius, in meters, 1/10th real scale

Stars.csv contains the following columns:

Column Name | Description
----------- | -----------
Name|The star's name
Distance|Distance of the star to the sun, in meters, 1/100th real scale
Temperature|The star's surface temperature, in Kelvin
Mass|The star's mass, in kilograms
Radius|The star's radius, in meters, 1/10th real scale

There's also Planets_All.csv, which is the unfiltered list of all over 4000 exoplanets, including all those with incomplete orbital or physical characteristics. It's structure is identical to Planets.csv.

# Notes
* Planets.csv only contains planets that have complete orbital information in the archive.
* The archive data does not contain LAN or AOP for any planet. The values in the Planets.csv table are randomly chosen and only present so that everyone who uses these tables works off of the same numbers.
* Note that the star distances in Stars.csv are in 1/100th scale, as opposed to KSP's 1/10th stock scale.

# Acknowledgements

This repository makes use of the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program.

This repository makes use of data from the first public release of the WASP data (Butters et al. 2010) as provided by the WASP consortium and services at the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program.

These data are made available to the community through the Exoplanet Archive on behalf of the KELT project team.
