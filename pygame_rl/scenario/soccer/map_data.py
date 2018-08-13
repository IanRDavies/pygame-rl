# Native modules
import math

# User-defined modules
import pygame_rl.renderer.pygame_renderer as pygame_renderer


class MapData(object):
    """The soccer map data as the geographical info.
    """
    # Tile positions
    spawn = []
    goals = []
    walkable = []

    def __init__(self, map_path):
        # Create a tile data and load
        tiled_data = pygame_renderer.TiledData(map_path)
        tiled_data.load()
        # Get the background tile positions
        tile_pos = tiled_data.get_tile_positions()
        # Build the tile positions
        self.spawn = tile_pos['spawn_area']
        self.goals = tile_pos['goal']
        self.walkable = tile_pos['ground']['WALKABLE']
