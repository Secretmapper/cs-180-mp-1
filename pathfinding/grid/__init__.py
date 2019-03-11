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

def add_points(grid, points):
    for coord in points:
        grid[coord[1]][coord[0]] = 0

def generate_rectangle(width, height):
    rect = np.ones((height, width), dtype=np.uint8)
    rect[0] = np.zeros(width, dtype=np.uint8)
    rect[-1] = np.zeros(width, dtype=np.uint8)
    rect[..., 0] = np.zeros(height, dtype=np.uint8)
    rect[..., -1] = np.zeros(height, dtype=np.uint8)
    return rect

def generate_line(p0, p1):
    x0, y0 = p0[0], p0[1]
    x1, y1 = p1[0], p1[1]
    dx, dy = x1 - x0, y1 - y0
    points = []
    # handle horiz/vertical line manually
    if dx == 0 or dy == 0:
        if dy == 0 and dx == 0:
            pass
        elif dy == 0:
            points = [(x, y0) for x in range(min(x0, x1), max(x0, x1) + 1)]
        elif dx == 0:
            points = [(x0, y) for y in range(min(y0, y1), max(y0, y1) + 1)]
    else:
        d_err = abs(dy / float(dx))
        err = 0
        y = y0
        for x in range(x0, x1):
            points.append((x, y))
            err = err + d_err
            if err >= 0.5:
                y = y + np.sign(dy) * 1
                err = err - 1.0
    return points
