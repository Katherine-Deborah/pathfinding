import matplotlib.pyplot as plt
import numpy as np

# Define the map file path
map_file = "arena.map"  # Replace with your map file path

# Define a dictionary to map characters to colors for visualization
terrain_colors = {
    ".": "white",  # Passable terrain
    "G": "white",  # Passable terrain
    "@": "black",  # Out of bounds
    "O": "black",  # Out of bounds
    "T": "brown",  # Trees (unpassable)
    "S": "green",  # Swamp (passable from regular terrain)
    "W": "blue",   # Water (traversable, but not passable from terrain)
}

# Read the map file and store it as a 2D array
map_data = []
with open(map_file, "r") as file:
    for line in file:
        row = list(line.strip())
        map_data.append(row)

# Get map dimensions
height = len(map_data)
width = len(map_data[0])

# Create a figure and axis for visualization
fig, ax = plt.subplots()

# Create a colormap based on terrain_colors
cmap = plt.matplotlib.colors.ListedColormap([terrain_colors[c] for row in map_data[4:] for c in row])

# Display the map
ax.imshow([[1]], cmap=cmap, extent=(0, width, 0, height))

# Set axis limits and labels
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_xticks(range(width))
ax.set_yticks(range(height))
ax.set_xticklabels(range(width))
ax.set_yticklabels(range(height))
ax.set_aspect('equal')  # Equal aspect ratio to avoid stretching

# Create custom tick labels based on terrain_colors keys
unique_terrain_types = list(set(terrain_colors.keys()))
tick_positions = np.arange(len(unique_terrain_types))
ax.set_xticks(tick_positions)
ax.set_xticklabels(unique_terrain_types)

# Set axis labels
plt.xlabel("X")
plt.ylabel("Y")

# Show the visualization
plt.show()
