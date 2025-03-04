#!/usr/bin/env python3
import mapnik
import os
import math

# Tile parameters
tile_size = 256  # Standard tile size
zoom_level = 3   # Change this for different zoom levels
output_dir = "tiles"  # Directory to store tiles

# Load map
m = mapnik.Map(tile_size, tile_size)
mapnik.load_map(m, "points.xml")  # Load style file

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define tile rendering function
def render_tile(zoom, x, y):
    """Renders a single tile at zoom level, x, y coordinates."""
    min_x = -180
    max_x = 180
    min_y = -85.0511  # Web Mercator bounds
    max_y = 85.0511

    # Convert tile coordinates to lat/lon bounds
    lon1 = min_x + (max_x - min_x) * (x / (2**zoom))
    lon2 = min_x + (max_x - min_x) * ((x + 1) / (2**zoom))
    lat1 = max_y - (max_y - min_y) * (y / (2**zoom))
    lat2 = max_y - (max_y - min_y) * ((y + 1) / (2**zoom))

    # Convert lat/lon to projection
    bbox = mapnik.Box2d(lon1, lat1, lon2, lat2)
    m.zoom_to_box(bbox)

    # Render tile
    filename = f"{output_dir}/{zoom}_{x}_{y}.png"
    mapnik.render_to_file(m, filename, "png")
    print(f"Tile saved: {filename}")

# Generate tiles for the zoom level
for x in range(2**zoom_level):
    for y in range(2**zoom_level):
        render_tile(zoom_level, x, y)
