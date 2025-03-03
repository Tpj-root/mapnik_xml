# mapnik_xml



**Files_Types**


**Notes:**

- **Shapefile (`shape`):** Ensure `world_borders.shp` exists.  
- **GeoJSON (`geojson`):** Use a `.json` file.  
- **Raster (`raster`):** For `.tif`, `.jpg`, `.png` images.  
- **PostGIS (`postgis`):** Requires a running PostgreSQL database with PostGIS.  
- **SQLite (`sqlite`):** Needs a spatially enabled SQLite database.  





GeoPackage (GPKG) file containing simplified land polygons, 
commonly used in geographic information systems (GIS). 
It may include vector data representing landmasses with reduced detail for faster processing


**Check its contents:**

```
ogrinfo -al -so very_simplified_land_polygons.gpkg
```

**Convert it to another format:**

```
ogr2ogr -f "GeoJSON" output.json very_simplified_land_polygons.gpkg
```




### Explanation of `ogrinfo` Output:
1. **File Format**: `very_simplified_land_polygons.gpkg` is a **GeoPackage (GPKG)**.
2. **Layer Name**: `very_simplified_land_polygons`
3. **Geometry Type**: **Polygon** (It contains land area shapes).
4. **Feature Count**: **5,221** (Total number of polygons).
5. **Extent**: The bounding box covers almost the entire world:
   - Min: **(-20037500, -20037500)** (approximate lower-left corner)
   - Max: **(20037500, 18455700)** (approximate upper-right corner)
6. **Coordinate System**:  
   - **EPSG:3857 (Web Mercator)** – Commonly used in web mapping applications like OpenStreetMap, Google Maps.
7. **Attributes**:  
   - `area` and `aread`: **Integer64** fields, possibly representing land area.

---

### Filtering Polygons:
You can use **OGR SQL** with `ogr2ogr` or `ogrinfo` to filter polygons based on attributes.

#### 1. **Filter by Area (e.g., only large polygons)**
```bash
ogr2ogr -f "GPKG" filtered.gpkg very_simplified_land_polygons.gpkg -sql "SELECT * FROM very_simplified_land_polygons WHERE area > 1000000"
```
This creates `filtered.gpkg` containing only polygons with `area > 1,000,000`.

#### 2. **Filter and Export to GeoJSON**
```bash
ogr2ogr -f "GeoJSON" filtered.json very_simplified_land_polygons.gpkg -sql "SELECT * FROM very_simplified_land_polygons WHERE area < 500000"
```
This extracts small land polygons into a JSON file.

#### 3. **Filter by Spatial Extent (Bounding Box)**
To get polygons inside a specific region:
```bash
ogr2ogr -f "GPKG" region_filtered.gpkg very_simplified_land_polygons.gpkg -spat xmin ymin xmax ymax
```
Example (for a specific area):
```bash
ogr2ogr -f "GPKG" india_filtered.gpkg very_simplified_land_polygons.gpkg -spat 6000000 5000000 12000000 10000000
```

#### 4. **View Filtered Polygons in QGIS**
- Open **QGIS** → `Add Vector Layer` → Select `very_simplified_land_polygons.gpkg`
- Use **Attribute Table (F6)** → `Select by Expression` to filter.






EPSG:3857 (Web Mercator) Explained

EPSG:3857 (also called Web Mercator or Pseudo-Mercator) is a projected coordinate system used for web maps (e.g., Google Maps, OpenStreetMap). Instead of using latitude/longitude (EPSG:4326), it represents locations in meters.
Why Not Latitude/Longitude?

    Latitude/Longitude (EPSG:4326) is in degrees, which are not uniform in scale.
    Web Mercator (EPSG:3857) converts latitude/longitude into a Cartesian coordinate system (X, Y in meters).
    This makes it easier for mapping and zooming on web-based applications.

How Web Mercator Works

    Origin (0,0) → The equator and prime meridian intersection.
    X (Easting) → Measures distance east/west from the Prime Meridian (in meters).
    Y (Northing) → Measures distance north/south from the equator (in meters).
    Range:
        X (Easting): -20,037,500 to +20,037,500 meters (covers -180° to 180° longitude).
        Y (Northing): -20,037,500 to +18,455,700 meters (covers ~85.06°S to ~85.06°N latitude).

Why Use EPSG:3857?

✔ Fast for web maps (tile-based rendering).
✔ Straightforward zooming & panning in meters.
✔ Matches Google Maps, OpenStreetMap, Bing Maps.

But distorts polar regions (Greenland looks huge!).










Filter by Spatial Extent (Bounding Box)

```
ogr2ogr -f "GPKG" india_filtered.gpkg very_simplified_land_polygons.gpkg -spat 6000000 5000000 12000000 10000000
```




```
ogrinfo -sql "SELECT area, aread FROM very_simplified_land_polygons LIMIT 20" very_simplified_land_polygons.gpkg
ogrinfo -sql "SELECT * FROM very_simplified_land_polygons WHERE area > 1000000" very_simplified_land_polygons.gpkg
ogr2ogr -f GeoJSON filtered.json very_simplified_land_polygons.gpkg -sql "SELECT * FROM very_simplified_land_polygons WHERE area > 1000000"


find the smallest area value using this command:

ogrinfo -sql "SELECT MIN(area) FROM very_simplified_land_polygons" very_simplified_land_polygons.gpkg


ogrinfo -sql "SELECT * FROM very_simplified_land_polygons WHERE area = 10000086" very_simplified_land_polygons.gpkg

```


make the background transparent by removing the background-color attribute

```
<Map background-color="#afc6e9" srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over">

<Map srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over">
```




convert longitude (78.0) and latitude (22.0) into Spherical Mercator (EPSG:3857) coordinates using cs2cs from GDAL/PROJ:

```
echo "78.0 22.0" | cs2cs +proj=longlat +datum=WGS84 +to +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs
8682920.28  2511525.23 0.00

```


`cs2cs` is a command-line tool from the **PROJ** library used to convert coordinates between different coordinate reference systems (CRS).  

### **1. Install `cs2cs` (if not installed)**
On **Debian-based systems**:  
```sh
sudo apt update && sudo apt install proj-bin
```
  
### **2. Basic Usage**
Format:  
```sh
echo "longitude latitude" | cs2cs +proj=source_CRS +to +proj=target_CRS
```

#### **Example: Convert (78.0, 22.0) from WGS84 (EPSG:4326) to Mercator (EPSG:3857)**  
```sh
echo "78.0 22.0" | cs2cs +proj=longlat +datum=WGS84 +to +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs
```

#### **Output (X, Y in meters):**
```
8686442.82  2529863.64  0.00
```

### **3. Reverse Conversion (Mercator to WGS84)**
```sh
echo "8686442.82 2529863.64" | cs2cs +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +to +proj=longlat +datum=WGS84
```
**Output:**
```
78.0 22.0 0.00
```

### **4. Alternative Using EPSG Codes**
```sh
echo "78.0 22.0" | cs2cs +init=epsg:4326 +to +init=epsg:3857
```

Let me know if you need more details! 🚀


### **EPSG:4326 vs EPSG:3857 – Coordinate Reference Systems Explained**  

#### **1. EPSG:4326 (WGS 84 - Latitude/Longitude)**
- **Type:** Geographic Coordinate System (GCS)
- **Units:** Degrees (°)
- **Axis:** (longitude, latitude)
- **Usage:** Used in GPS, mapping applications (Google Maps, OpenStreetMap, etc.)
- **Example Coordinates:**
  ```
  78.0, 22.0  (longitude, latitude)
  ```
- **Issues:**  
  - Not uniform in scale (1 degree of latitude ≠ 1 degree of longitude in distance).
  - Hard to measure distances directly.

---

#### **2. EPSG:3857 (Web Mercator)**
- **Type:** Projected Coordinate System (PCS)
- **Units:** Meters (m)
- **Axis:** (X, Y) → (East, North)
- **Usage:** Used in web maps (Google Maps, OpenStreetMap, Bing Maps, etc.)
- **Example Converted Coordinates (for 78.0, 22.0):**
  ```
  8686442.82, 2529863.64  (X, Y in meters)
  ```
- **Benefits:**  
  - Allows for fast panning/zooming in web maps.
  - Uniform scale at all locations.

---

### **Conversion Example**
Convert `78.0, 22.0` from EPSG:4326 to EPSG:3857 using **cs2cs**:
```sh
echo "78.0 22.0" | cs2cs +init=epsg:4326 +to +init=epsg:3857
```
**Output (X, Y in meters):**
```
8686442.82 2529863.64 0.00
```

Would you like a Python script for this conversion? 🚀



Yes! The **Mercator projection (EPSG:3857)** works like a **graph sheet** where the world is divided into **four quadrants** based on the **equator (latitude 0°)** and **prime meridian (longitude 0°)**:

### **Mercator Coordinate System (EPSG:3857)**
- **Center (0,0):** Intersection of **Equator (0° latitude)** and **Prime Meridian (0° longitude)**.
- **Units:** Meters (instead of degrees).
- **Divides the world into 4 parts:**
  
  | Quadrant | Longitude (X) | Latitude (Y) |
  |----------|-------------|-------------|
  | **Top-Right (+X, +Y)** | **East of Prime Meridian** (Positive) | **North of Equator** (Positive) |
  | **Top-Left (-X, +Y)** | **West of Prime Meridian** (Negative) | **North of Equator** (Positive) |
  | **Bottom-Left (-X, -Y)** | **West of Prime Meridian** (Negative) | **South of Equator** (Negative) |
  | **Bottom-Right (+X, -Y)** | **East of Prime Meridian** (Positive) | **South of Equator** (Negative) |

---

### **Examples of X, Y values for different locations**  

| Location        | Longitude (°) | Latitude (°) | X (meters) | Y (meters) |
|----------------|--------------|-------------|------------|------------|
| **London**     | -0.1278       | 51.5074     | -14219.37  | 6711017.82 |
| **New York**   | -74.006       | 40.7128     | -8238310.23 | 4970071.57 |
| **India (Central)** | 78.0       | 22.0        | 8686442.82 | 2529863.64 |
| **Brazil**     | -47.92        | -15.78      | -5333902.71 | -1772851.92 |
| **Australia**  | 133.775       | -25.2744    | 14892824.76 | -2897740.99 |

---

### **Why Some Countries Have Negative X, Y?**
- **X is Negative (-X):** If a country is **west** of the Prime Meridian (e.g., USA, Brazil).
- **Y is Negative (-Y):** If a country is **south** of the Equator (e.g., Australia, Argentina).

This is why countries in the **Western & Southern Hemisphere** have **negative values** in Mercator projection.

---

### **Convert Any Coordinates Using `cs2cs`**
To check any location:
```sh
echo "<longitude> <latitude>" | cs2cs +init=epsg:4326 +to +init=epsg:3857
```
Example for **New York (-74.006, 40.7128)**:
```sh
echo "-74.006 40.7128" | cs2cs +init=epsg:4326 +to +init=epsg:3857
```
Output:
```
-8238310.23 4970071.57 0.00
```

Would you like a **visual representation** of this grid system? 🚀










Yes! If **longitude (lon) or latitude (lat) is negative**, the corresponding **X or Y in Mercator projection (EPSG:3857) will also be negative**.  

### **Rules for X, Y in EPSG:3857 (Mercator)**
| **Longitude (°)** | **Latitude (°)** | **X (meters)** | **Y (meters)** |
|------------------|----------------|---------------|---------------|
| **Positive (EAST)**  | **Positive (NORTH)**  | **+X** | **+Y** |
| **Negative (WEST)**  | **Positive (NORTH)**  | **-X** | **+Y** |
| **Negative (WEST)**  | **Negative (SOUTH)**  | **-X** | **-Y** |
| **Positive (EAST)**  | **Negative (SOUTH)**  | **+X** | **-Y** |

---

### **Example Calculations**  
Let's convert some real-world locations:

#### **1️⃣ India (Central) → (78.0, 22.0)**
```sh
echo "78.0 22.0" | cs2cs +init=epsg:4326 +to +init=epsg:3857
```
**Result:**  
```
8686442.82 2529863.64 0.00
```
✔️ **Positive X, Positive Y** (East of Prime Meridian, North of Equator).

---

#### **2️⃣ Brazil → (-47.92, -15.78)**
```sh
echo "-47.92 -15.78" | cs2cs +init=epsg:4326 +to +init=epsg:3857
```
**Result:**  
```
-5333902.71 -1772851.92 0.00
```
✔️ **Negative X, Negative Y** (West of Prime Meridian, South of Equator).

---

#### **3️⃣ New York → (-74.006, 40.7128)**
```sh
echo "-74.006 40.7128" | cs2cs +init=epsg:4326 +to +init=epsg:3857
```
**Result:**  
```
-8238310.23 4970071.57 0.00
```
✔️ **Negative X, Positive Y** (West of Prime Meridian, North of Equator).

---

### **Conclusion**  
- If **longitude is negative (WEST)** → **X is negative**.
- If **longitude is positive (EAST)** → **X is positive**.
- If **latitude is negative (SOUTH)** → **Y is negative**.
- If **latitude is positive (NORTH)** → **Y is positive**.

So, the Mercator grid **splits the Earth into four quadrants**, just like a graph! 🚀


**Study**


```
https://vikdhillon.staff.shef.ac.uk/teaching/phy105/celsphere/phy105_earth.html
```

