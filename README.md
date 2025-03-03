# mapnik_xml


**Projection (SRS)**


Your `<Map>` definition uses this projection:  

```xml
srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over"
```

### **Projection Type:**
- **Mercator Projection** (`+proj=merc`)
- **Also known as:** Web Mercator (EPSG:3857) or Spherical Mercator  

### **Projection Details:**
| Parameter  | Value  | Meaning |
|------------|--------|---------|
| `+proj=merc` | Mercator | Specifies the Mercator projection |
| `+a=6378137` | 6378137 meters | Semi-major axis (Earth’s radius) |
| `+b=6378137` | 6378137 meters | Semi-minor axis (spherical model) |
| `+lat_ts=0.0` | 0° | Latitude of true scale |
| `+lon_0=0.0` | 0° | Central meridian (Greenwich) |
| `+x_0=0.0` | 0 meters | False easting |
| `+y_0=0.0` | 0 meters | False northing |
| `+k=1.0` | 1 | Scale factor |
| `+units=m` | meters | Output coordinates in meters |
| `+nadgrids=@null` | No datum shift | No grid-based transformation |
| `+no_defs` | No default settings | Prevents loading default settings |
| `+over` | Allows longitude > 180° | Supports world wrapping |



### **Key Notes:**
- Uses **meters** instead of degrees.
- Great for **web maps** (Google Maps, OpenStreetMap, etc.).
- Distorts **area and shape** near the poles.  
- Good for **navigation but not for accurate land measurements**.  

If you need **WGS 84 (lat/lon, degrees)**, you should use:  
```xml
srs="+proj=longlat +datum=WGS84 +no_defs"
```

Let me know if you need a different projection! 🚀










Here's the full list of approximate scale denominator values for **zoom levels 1 to 18**:  

- **Zoom 1** ≈ **1:500,000,000**  
- **Zoom 2** ≈ **1:250,000,000**  
- **Zoom 3** ≈ **1:100,000,000**  
- **Zoom 4** ≈ **1:50,000,000**  
- **Zoom 5** ≈ **1:20,000,000**  
- **Zoom 6** ≈ **1:10,000,000**  
- **Zoom 7** ≈ **1:5,000,000**  
- **Zoom 8** ≈ **1:2,500,000**  
- **Zoom 9** ≈ **1:1,000,000**  
- **Zoom 10** ≈ **1:500,000**  
- **Zoom 11** ≈ **1:250,000**  
- **Zoom 12** ≈ **1:150,000**  
- **Zoom 13** ≈ **1:70,000**  
- **Zoom 14** ≈ **1:35,000**  
- **Zoom 15** ≈ **1:20,000**  
- **Zoom 16** ≈ **1:10,000**  
- **Zoom 17** ≈ **1:5,000**  
- **Zoom 18** ≈ **1:2,500**  


These values are approximations used in Mapnik and other mapping libraries.



**apply your style only from zoom level 5 to 18, use:**

```
<MinScaleDenominator>2500</MinScaleDenominator>  <!-- Zoom 18 -->
<MaxScaleDenominator>20000000</MaxScaleDenominator> <!-- Zoom 5 -->

```



The `<Parameter name="center">82.75,21,5</Parameter>` sets the **initial center** of the map when it loads.  

- **82.75** → Longitude (X)  
- **21** → Latitude (Y)  
- **5** → Zoom level  

Each time you open the map, it will be centered at **(82.75, 21)** with an initial zoom level of **5**.








**Notes:**


mapnik-config --fonts
/usr/share/fonts





**mapnik-config**



```
Usage: mapnik-config [OPTION]

Known values for OPTION are:

  -h --help         display this help and exit
  -v --version      version information (MAPNIK_VERSION_STRING)
  --version-number  version number (MAPNIK_VERSION) (new in 2.2.0)
  --git-revision    git hash from "git rev-list --max-count=1 HEAD"
  --git-describe    git decribe output (new in 2.2.0)
  --fonts           default fonts directory
  --input-plugins   default input plugins directory
  --defines         pre-processor defines for Mapnik build (new in 2.2.0)
  --prefix          Mapnik prefix [default /usr]
  --lib-name        Mapnik library name
  --libs            library linking information
  --dep-libs        library linking information for Mapnik dependencies
  --ldflags         library paths (-L) information
  --includes        include paths (-I) for Mapnik headers (new in 2.2.0)
  --dep-includes    include paths (-I) for Mapnik dependencies (new in 2.2.0)
  --cxxflags        c++ compiler flags and pre-processor defines (new in 2.2.0)
  --cflags          all include paths, compiler flags, and pre-processor defines (for back-compatibility)
  --cxx             c++ compiler used to build mapnik (new in 2.2.0)
  --all-flags       all compile and link flags (new in 2.2.0)
  --gdal-data       path to GDAL_DATA directory, if detected at build time (new in 3.0.16)
  --proj-lib        path to PROJ_LIB directory, if detected at build time (new in 3.0.16)
  --icu-data        path to ICU_DATA directory, if detected at build time (new in 3.0.16)

```






Files_Types



### Notes:
- **Shapefile (`shape`):** Ensure `world_borders.shp` exists.  
- **GeoJSON (`geojson`):** Use a `.json` file.  
- **Raster (`raster`):** For `.tif`, `.jpg`, `.png` images.  
- **PostGIS (`postgis`):** Requires a running PostgreSQL database with PostGIS.  
- **SQLite (`sqlite`):** Needs a spatially enabled SQLite database.  

Run:  
```bash
mapnik-render --xml map.xml --img output.png
```



If you're using .shp, ensure all required files (.shp, .shx, .dbf) exist.





http://postgis.net/documentation/

Learn


```
sudo apt update
sudo apt install postgis postgresql-15-postgis-3
sudo -u postgres psql
CREATE EXTENSION postgis;
SELECT postgis_full_version();

```


sudo -u postgres createdb mygisdb
sudo -u postgres psql -d mygisdb -c "CREATE EXTENSION postgis;"
sudo -u postgres psql
CREATE USER cnc WITH PASSWORD '123';
GRANT ALL PRIVILEGES ON DATABASE mygisdb TO cnc;


nik4 mapnik.xml output.png



```
sudo -u postgres psql -d mygisdb


CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    name TEXT,
    geom GEOMETRY(Point, 4326)
);


INSERT INTO places (name, geom) VALUES ('My Location', ST_GeomFromText('POINT(78.686 10.775)', 4326));


GRANT SELECT ON TABLE places TO cnc;
GRANT ALL ON TABLE places TO cnc;
GRANT ALL PRIVILEGES ON TABLE places TO cnc;


```

nik4 -b 78.5 10.7 78.9 10.8 -d 800 600 mapnik.xml output.png


nik4 -b 8738580.027271975 1198103.0405602609 8783107.823589286 1209433.8422168817 -d 800 600 mapnik.xml output.png



GOOD
```
cnc@debian:~/Documents/sample$ nik4 -b 78.5 10.7 78.9 10.8 -d 800 600 mapnik.xml output.png

http://postgis.net/documentation/training/
```



mapnic read 

```
ogrinfo -al -ro PG:"dbname=mygisdb user=cnc password=123" places
```


Import into PostGIS using:

shp2pgsql -I -s 4326 mydata.shp mytable | psql -d mygisdb




1. Coordinate System Mismatch

Your places layer is in EPSG:4326 (WGS 84), but Mapnik's default is EPSG:3857 (Web Mercator). Try transforming it in your mapnik.xml:





```

<Parameter name="table"><![CDATA[(SELECT id, name, ST_Transform(geom, 3857) AS geom FROM places) AS subquery]]></Parameter>
<Parameter name="srid"><![CDATA[3857]]></Parameter>

```


```

https://github.com/mapbox/osm-bright
```




SELECT id, name, ST_AsText(ST_Transform(geom, 3857)) FROM places;







login


sudo -u postgres psql
\c gis
\dt
SELECT * FROM planet_osm_polygon LIMIT 5;






**Export**

```
https://www.openstreetmap.org/export#map=19/10.796804/78.686680

```


```
https://github.com/mapnik/mapnik/wiki/XMLConfigReference
https://github.com/openstreetmap/mapnik-stylesheets/blob/master/osm.xml
https://github.com/mapnik/mapnik/wiki/StyleShare

```




