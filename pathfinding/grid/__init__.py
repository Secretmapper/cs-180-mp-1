import numpy as np

def generate(width=100, height=100):
    grid = np.ones((height, width), dtype=np.uint8)

    # make border
    add_polygon(grid, generate_rectangle(width, height))

    #  rect = generate_rectangle(45, 45)
    #  add_polygon(grid, rect, (1, 3))
    #  rect = generate_rectangle(45, 45)
    #  add_polygon(grid, rect, (30, 30))

    # pick start point
    sx, sy = (2, 2)

    # pick end point
    ex, ey = (width - 3, height - 3)

    return np.array(grid, dtype=np.uint8), (sx, sy), (ex, ey)

def add_polygon(grid, polygon, pos=(0, 0)):
    y, x = pos
    grid[x:x + polygon.shape[0], y:y + polygon.shape[1]] = polygon

def generate_rectangle(width, height):
    rect = np.ones((height, width), dtype=np.uint8)
    rect[0] = np.zeros(width, dtype=np.uint8)
    rect[-1] = np.zeros(width, dtype=np.uint8)
    rect[..., 0] = np.zeros(height, dtype=np.uint8)
    rect[..., -1] = np.zeros(height, dtype=np.uint8)
    return rect
