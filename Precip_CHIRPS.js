//GOAL: Determine mean daily preciptation for Cuba from 1984-2011

//STEPS:
//Set date range, filter collection
//Loop through collection, export mean values

var CHIRPS = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY"),
    geometry = ee.Geometry.Polygon(
        [[[-85.21370784361741, 23.919903553616226],
          [-85.21370784361741, 19.66733193040363],
          [-73.94173518736741, 19.66733193040363],
          [-73.94173518736741, 23.919903553616226]]], null, false),
    cuba = ee.FeatureCollection("users/mfstuhlmacher/Cuba/Tables/CUB_adm0");

var dateRange = ee.DateRange("1984-01-01","2011-12-31");
var cubaRain = CHIRPS.filterDate(dateRange).filterBounds(geometry);
Map.addLayer(cubaRain.first(),{},'cuba rain');

var b1scale = cubaRain.first().select('precipitation').projection().nominalScale();
print(b1scale,'scale');

//Export mean daily values to make plot in R
Export.table.toDrive({
  collection: cubaRain.map(function(image) {
    return ee.Feature(null, image.reduceRegion({
      reducer: 'mean', 
      geometry: cuba, 
      scale: b1scale,
    }).set('time', image.get('system:time_start')));
  }), 
  description: 'CHIRPS_1984_2011_mean', 
  fileFormat: 'CSV'
});