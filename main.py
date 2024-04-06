import random
import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

def distance(point1, point2):
    """ Returns:
        int: Etäisyys kahden pisteen välillä.
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def generate_points(n:int, x:int, y:int, min_distance:int):
    """Generoi satunnaisia pisteitä 2d-tasolle tietyn etäisyyden päähän reunoista ja toisistaan.

    Args:
        n (int): Generoitavien pisteiden määrä.
        x (int): Max x-koordinaatti.
        y (int): Max y-koordinaatti.
        min_distance (int): Pienin sallittu etäisyys pisteiden ja reunojen välillä.

    Returns:
        list: Lista generoituja pisteitä.
    """
    pointslist = []
    while len(pointslist) < n:
        randomx = random.randint(0+min_distance/2, x-min_distance/2)
        randomy = random.randint(0+min_distance/2, y-min_distance/2)
        randompoint = (randomx, randomy)
        if all(distance(randompoint, oldpoint) >= min_distance for oldpoint in pointslist):
            pointslist.append(randompoint)
    return pointslist

def add_super_triangle(max_x, max_y):
    """Muodostaa superkolmion joka kattaa koko 2d-alueen.

    Args:
        max_x (int): Max x-koordinaatti.
        max_y (int): Max y-koordinaatti.

    Returns:
        tuple: Kolme pistettä jotka muodostavat kolmion.
    """

    min_x = -1
    min_y = -1
    max_x *= 2
    max_y *= 2

    super_triangle = ((min_x, min_y), (max_x, min_y), (min_x, max_y))
    return super_triangle

def is_collinear(point1, point2, point3):
    """Tarkistaa ovatko pisteet samalla suoralla ja palauttaa totuusarvon.
    """
    return (point3[1] - point1[1]) * (point2[0] - point1[0]) == (point3[0] - point1[0]) * (point2[1] - point1[1])

def circumcircle(point1, point2, point3):
    """Muodostaa kolmion ympäri piirretyn ympyrän.

    Args:
        Kolmion kolme pistettä.

    Returns:
        Keskipiste ja ympyrän säde.
    """

    if is_collinear(point1, point2, point3):
        return None, None

    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    mid1 = ((x1 + x2) / 2, (y1 + y2) / 2)
    mid2 = ((x2 + x3) / 2, (y2 + y3) / 2)

    if y2 - y1 == 0:
        slope1 = None
    else:
        slope1 = -(x2 - x1) / (y2 - y1)

    if y3 - y2 == 0:
        slope2 = None
    else:
        slope2 = -(x3 - x2) / (y3 - y2)

    if slope1 is None:
        xc = mid1[0]
        yc = slope2 * (xc - mid2[0]) + mid2[1]
    elif slope2 is None:
        xc = mid2[0]
        yc = slope1 * (xc - mid1[0]) + mid1[1]
    else:
        xc = (slope1 * mid1[0] - slope2 * mid2[0] + mid2[1] - mid1[1]) / (slope1 - slope2)
        yc = slope1 * (xc - mid1[0]) + mid1[1]

    radius = ((x1 - xc) ** 2 + (y1 - yc) ** 2) ** 0.5

    return (xc, yc), radius

def inside_circumcircle(point, triangle):
    """Tarkistaa onko piste kolmion ympäri piirretyn ympyrän sisällä ja palauttaa totuusarvon.
    """
    center, radius = circumcircle(*triangle)
    if center is None or radius is None:
        return False
    return distance(point, center) <= radius

def get_edges(triangle):
    """Palauttaa kolmion sivut.
    """
    edges = ((triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0]))
    return edges

def shared_edge(edge, triangles):
    """Laskee kuinka monta kertaa sivu esiintyy listassa kolmioita ja palauttaa määrän."""
    tricount = 0
    for triangle in triangles:
        triangle_edges = get_edges(triangle)
        for tri_edge in triangle_edges:
            if edge == tri_edge:
                tricount += 1
            elif edge == tuple(reversed(tri_edge)):
                tricount += 1
    return tricount

def delaunay(points, x, y):
    """Suorittaa Delaunayn triangulaation annetuille pisteille.

    Args:
        points (list): Lista pisteitä.
        x (int): Max x-koordinaatti.
        y (int): Max y-koordinaatti.

    Returns:
        list: Lista kolmioita.
    """
    triangulation = []
    triangulation.append(add_super_triangle(x, y))

    for point in points:
        bad_triangles = set()
        for triangle in triangulation:
            if inside_circumcircle(point, triangle):
                bad_triangles.add(triangle)

        polygon = set()
        for triangle in bad_triangles:
            edges = get_edges(triangle)
            for edge in edges:
                if shared_edge(edge, bad_triangles) == 1:
                    polygon.add(edge)

        for triangle in bad_triangles:
            triangulation.remove(triangle)

        for edge in polygon:
            new_triangle = (edge[0], edge[1], point)
            triangulation.append(new_triangle)

    new_triangulation = []
    for triangle in triangulation:
        if not any(vertex in triangle for vertex in [(-1, -1), (x*2, -1), (-1, y*2)]):
            new_triangulation.append(triangle)
    return new_triangulation

def generate_rooms(pointlist:list, min_dist:int):
    """Luo pisteiden ympärille sen kokoisen huoneen ettei se voi törmätä muihin huoneisiin.

    Args:
        pointlist (list): Lista pisteistä.
        min_dist (int): Pienin sallittu etäisyys pisteiden välillä.

    Returns:
        list: Lista huoneita.
    """
    roomlist = []
    min_dist *= 0.5
    side_length = (2**0.5) * min_dist
    for pt in pointlist:
        x, y = pt
        square = pygame.Rect(x - side_length/2, y - side_length/2, side_length, side_length)
        roomlist.append(square)
        if RUNNING:
            pygame.draw.rect(window, blue, square, 5)
            pygame.time.wait(int(NPOINTS*2.5))
            pygame.display.update()
    return roomlist

# Parameters
NPOINTS = 20
X_MAX = 800
Y_MAX = 800
MIN_DISTANCE = 100
points = generate_points(NPOINTS, X_MAX, Y_MAX, MIN_DISTANCE)
#rooms = generate_rooms(points, MIN_DISTANCE)
rooms = []
#points = [(100, 100), (200, 300), (400, 200), (500, 500)]
#points = [(264, 592), (138, 495), (28, 376), (523, 491), (508, 374)]
print("List of points: ", points, len(points))

#print("Circumcircle: ", circumcircle((0, 0), (0, 4), (4, 4)))

triangulation = delaunay(points, X_MAX, Y_MAX)

print("Delaunay: ", triangulation)


# Visualization
pygame.init()
window_size = (X_MAX+10, Y_MAX+10)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Delaunay Triangulation")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
            elif event.key == pygame.K_r:
                points = generate_points(NPOINTS, X_MAX, Y_MAX, MIN_DISTANCE)
                #print("List of points: ", points, len(points))
                triangulation = delaunay(points, X_MAX, Y_MAX)
                #print("Delaunay: ", triangulation)
                rooms = []
            elif event.key == pygame.K_g:
                rooms = generate_rooms(points, MIN_DISTANCE)
    window.fill(black)

    for p in points:
        pygame.draw.circle(window, red, p, 2)

    for r in rooms:
        pygame.draw.rect(window, blue, r, 5)

    for t in triangulation:
        pygame.draw.polygon(window, white, t, 1)
        for vertex in t:
            pygame.draw.circle(window, red, vertex, 3)



    pygame.display.flip()

pygame.quit()
