from logic import pygame, generate_points, delaunay, generate_start_point, generate_rooms, pathing

def visualize():
    from parameters import (
        NPOINTS, X_MAX, Y_MAX, MIN_DISTANCE, points, rooms, triangulation, start_point, corridors,
        white, black, red, blue, yellow, green
    )
    # Initialize Pygame
    pygame.init()
    window_size = (X_MAX+10, Y_MAX+10)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Delaunay Triangulation")

    def draw():
        window.fill(black)

        for p in points:
            pygame.draw.circle(window, red, p, 2)

        for r in rooms:
            pygame.draw.rect(window, yellow, r, 5)

        for t in triangulation:
            pygame.draw.polygon(window, white, t, 1)
            for vertex in t:
                pygame.draw.circle(window, red, vertex, 3)

        for i in range(len(corridors)-1):
            pygame.draw.line(window, white, corridors[i], corridors[i+1], 1)
            pygame.draw.circle(window, green, corridors[-1], 5)

        pygame.draw.circle(window, blue, start_point, 5)

        pygame.display.flip()


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    points = generate_points(NPOINTS, X_MAX, Y_MAX, MIN_DISTANCE)
                    triangulation = delaunay(points, X_MAX, Y_MAX)
                    start_point = generate_start_point(points, X_MAX, Y_MAX, MIN_DISTANCE)
                    rooms = []
                    corridors = []
                    pygame.display.set_caption("Delaunay Triangulation")
                elif event.key == pygame.K_g and not rooms:
                    rooms = generate_rooms(points, MIN_DISTANCE)
                    for r in rooms:
                        pygame.draw.rect(window, yellow, r, 5)
                        pygame.time.wait(int(NPOINTS*2.5))
                        pygame.display.update()
                elif event.key == pygame.K_c and not corridors:
                    corridors = pathing(triangulation, start_point)
                    triangulation = []
                    pygame.display.set_caption("Cave Generator")
                elif event.key == pygame.K_p:
                    print("Points: ", points, "\n", flush=True)
                    print("Delaunay triangulation: ", triangulation, "\n", flush=True)
                    print("Start point: ", start_point, "\n", flush=True)
                    if rooms:
                        print("Rooms: ", rooms, "\n", flush=True)
                    if corridors:
                        print("Corridors: ", corridors, "\n", flush=True)



        draw()

    pygame.quit()
