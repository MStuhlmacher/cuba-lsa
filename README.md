# Institutional Shifts and Landscape Change: A Land System Architecture Case Study from the Republic of Cuba during the Período Especial
Code for assessing the land system impacts of institutional shifts in Cuba that occurred after the fall of the Soviet Union and the subsequent economic crisis (Período Especial en Tiempos de Paz: 1991-2000).

### Methodology Diagram:

# Software Requirements:
R version 3.6.3

Google Earth Engine (JavaScript API)

Python 2.7.16/ArcMap 10.7.1 (arcpy)

# Data

### Accessed via Google Earth Engine 
USGS Landsat 5 TM Collection 1 Tier 1 Raw Scenes

DMSP OLS: Global Radiance-Calibrated Nighttime Lights Version 4, Defense Meteorological Program Operational Linescan System

SRTM Digital Elevation Data 30m

CHIRPS Daily: Climate Hazards Group InfraRed Precipitation with Station Data (version 2.0)

### Land Use/Land Cover Classification

# Analysis

### Research Question 1:
Land use/land cover (LULC) was classified for 1985, 1990, 1995, 2000, 2005, and 2010 using remotely sensed data. Each 30m pixel was classified as water, cropland, barren/grass/shrubland, forest or built-up. The classifications were used to calculate patch size, shape, connectivity and distance for each class. The change in these metrics over time was linked temporally to Cuban policies collected at the U.S. Library of Congress.

### Research Question 2:
Tasseled-cap transformation was used on Landsat 5 imagery to calculate environmental variables (brightness, greenness, and wetness) for each class over time. The change in brightness, greenness, and wetness over time was used to examine environmental quality within LULC classes.

# References
McGarigal, K., Cushman, S.A., Ene, E., (2012). FRAGSTATS v4: Spatial Pattern Analysis Program for Categorical and Continuous Maps. Comput. Softw. Program Prod. Authors Univ. Mass. Amherst. http://www.umass.edu/landeco/research/fragstats/fragstats.html

Farr, T.G., Rosen, P.A., Caro, E., Crippen, R., Duren, R., Hensley, S., Kobrick, M., Paller, M., Rodriguez, E., Roth, L., Seal, D., Shaffer, S., Shimada, J., Umland, J., Werner, M., Oskin, M., Burbank, D., and Alsdorf, D.E., (2007). The shuttle radar topography mission: Reviews of Geophysics, v. 45, no. 2, RG2004. doi.org/10.1029/2005RG000183.

Funk, Chris, Pete Peterson, Martin Landsfeld, Diego Pedreros, James Verdin, Shraddhanand Shukla, Gregory Husak, James Rowland, Laura Harrison, Andrew Hoell & Joel Michaelsen. (2015). "The climate hazards infrared precipitation with stations—a new environmental record for monitoring extremes". Scientific Data 2, 150066. doi:10.1038/sdata.2015.66

