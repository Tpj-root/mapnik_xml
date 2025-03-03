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











