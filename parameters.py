from logic import generate_points, delaunay, generate_start_point

NPOINTS = 20
X_MAX = 800
Y_MAX = 800
MIN_DISTANCE = 100
points = generate_points(NPOINTS, X_MAX, Y_MAX, MIN_DISTANCE)
#rooms = generate_rooms(points, MIN_DISTANCE)
rooms = []
triangulation = delaunay(points, X_MAX, Y_MAX)
start_point = generate_start_point(points, X_MAX, Y_MAX, MIN_DISTANCE)
#corridors = pathing(triangulation, start_point, end_point)
corridors = []
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
