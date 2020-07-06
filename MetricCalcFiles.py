#MetricCalcFiles.py

# Import arcpy module
import arcpy

filePath = "path\\to\\files"

#Conefor file creation:
# Set up a loop for each year
yearList = ["1985","1990","1995","2000","2005","2010"]
for year in yearList:
    #variables
    inRaster = filePath + "\\Cuba%s.tif" % (year)
    utmRaster = filePath + "\\Cuba%s_UTM17.tif" % (year)
    utm500Raster = filePath + "\\Cuba%s_500m_UTM17.tif" % (year)
    utm500SHP = filePath + "\\Cuba%s_500m_UTM17_SHP.shp" % (year)

    # Process: Project Raster
    arcpy.ProjectRaster_management(inRaster, utmRaster, "PROJCS['WGS_1984_UTM_Zone_17N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-81.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","MAJORITY", "29.6753583306385 29.6753583306384", "", "", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_VERTICAL")

    # Process: Resample
    arcpy.Resample_management(utmRaster, utm500Raster, "500 500", "MAJORITY")

    # Process: Raster to Polygon
    arcpy.RasterToPolygon_conversion(utm500Raster, utm500SHP, "NO_SIMPLIFY", "", "SINGLE_OUTER_PART", "")




