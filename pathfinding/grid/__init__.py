import numpy as np

def generate(width=100, height=100, polygons=[]):
    grid = np.ones((height, width), dtype=np.uint8)

    # make border
    add_points(grid, generate_line((0, 0), (width - 1, 0)))
    add_points(grid, generate_line((width - 1, 0), (width - 1, height - 1)))
    add_points(grid, generate_line((width - 1, height - 1), (0, height - 1)))
    add_points(grid, generate_line((0, height - 1), (0, 0)))

    for polygon in polygons:
        for i, coord in enumerate(polygon):
            second_coord = polygon[(i + 1) % len(polygon)]
            add_points(grid, generate_line(coord, second_coord))

    return np.array(grid, dtype=np.uint8)

def add_points(grid, points):
    for coord in points:
        grid[coord[1]][coord[0]] = 0

def generate_line(p0, p1):
    x0, y0 = p0[0], p0[1]
    x1, y1 = p1[0], p1[1]
    dx, dy = abs(x1 - x0), abs(y1 - y0)
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
        x, y = x0, y0
        x_step = -1 if x0 > x1 else 1
        y_step = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                points.append((x, y))
                err -= dy
                if err < 0:
                    y += y_step
                    err += dx
                x += x_step
        else:
            err = dy / 2.0
            while y != y1:
                points.append((x, y))
                err -= dx
                if err < 0:
                    x += x_step
                    err += dy
                y += y_step      
        points.append((x, y))
    return points
