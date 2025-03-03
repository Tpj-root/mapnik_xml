#!/bin/bash

# Set the grid spacing (degrees)
SPACING=10  # Adjust to 1, 5, or 10 for different densities
OUTPUT="grid_lines.gpkg"
TEMP_FILE="grid_lines.geojson"

# Remove existing files
rm -f $OUTPUT $TEMP_FILE

# Create an empty GeoJSON file
echo '{ "type": "FeatureCollection", "features": [] }' > $TEMP_FILE

# Add vertical grid lines (Longitude)
for lon in $(seq -180 $SPACING 180); do
    echo "{ \"type\": \"Feature\", \"geometry\": { \"type\": \"LineString\", \"coordinates\": [[$lon, -85], [$lon, 85]] }, \"properties\": {} }," >> $TEMP_FILE
done

# Add horizontal grid lines (Latitude)
for lat in $(seq -80 $SPACING 80); do
    echo "{ \"type\": \"Feature\", \"geometry\": { \"type\": \"LineString\", \"coordinates\": [[-180, $lat], [180, $lat]] }, \"properties\": {} }," >> $TEMP_FILE
done

# Remove the last comma and close JSON
sed -i '$ s/,$//' $TEMP_FILE
echo "] }" >> $TEMP_FILE

# Convert GeoJSON to GeoPackage
ogr2ogr -f GPKG $OUTPUT $TEMP_FILE -nln grid_lines

echo "Grid lines saved in $OUTPUT"
