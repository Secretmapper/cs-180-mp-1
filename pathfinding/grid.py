import numpy as np
from PIL import Image

def generate_grid_image(grid, start, end, path, displaySize=(1000, 500)):
    r = g = b = (grid * 255).astype(np.uint8)
    img_array = np.empty((grid.shape[0], grid.shape[1], 3), dtype=np.uint8)
    img_array[..., 0] = r
    img_array[..., 1] = g
    img_array[..., 2] = b
    if path:
        for coord in path:
            img_array[coord[1], coord[0]] = [254, 254, 59]
    # display start
    img_array[start[1], start[0]] = [0, 255, 0]
    # display end
    img_array[end[1], end[0]] = [255, 0, 0]
    return Image.fromarray(img_array, 'RGB').resize(displaySize)


def generate_grid(width=100, height=100):
    grid = np.ones((height, width), dtype=np.uint8)

    # make border
    add_polygon_to_grid(grid, generate_rectangle(width, height))

    rect = generate_rectangle(45, 45)
    add_polygon_to_grid(grid, rect, (5, 5))

    # pick start point
    sx, sy = (2, 2)

    # pick end point
    ex, ey = (width - 3, height - 3)

    return np.array(grid, dtype=np.uint8), (sx, sy), (ex, ey)

def add_polygon_to_grid(grid, polygon, pos=(0, 0)):
    x, y = pos
    grid[x:x + polygon.shape[0], y:y + polygon.shape[1]] = polygon

def generate_rectangle(width, height):
    rect = np.ones((height, width), dtype=np.uint8)
    rect[0] = np.zeros(width, dtype=np.uint8)
    rect[-1] = np.zeros(width, dtype=np.uint8)
    rect[..., 0] = np.zeros(height, dtype=np.uint8)
    rect[..., -1] = np.zeros(height, dtype=np.uint8)
    return rect
