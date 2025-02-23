import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

class Planet:

    AU = 149.6e6 * 1000 #astronomical units (earth to sun)
    G = 6.67428e-11
    SCALE = 200 / AU # 1AU = 100 pixels
    TIME_STEP = 3600 * 24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, window):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        pygame.draw.circle(window, self.color, (x,y), self.radius)
    
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y**2)  # distance between planet self and planet other

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2  #Force between bodies(F)
        angle = math.atan2(distance_y, distance_x) 
        force_x = math.cos(angle) * force 
        force_y = math.sin(angle) * force 

        return force_x, force_y

def main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30 )
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0 , 16, BLUE, 5.9742 *10**24)
    mars = Planet(1.524 * Planet.AU, 0 , 12, RED, 0.639 *10**24)
    mercury = Planet(-0.387 * Planet.AU, 0 , 8, DARK_GREY, 0.33 *10**24)
    venus = Planet(0.723 * Planet.AU, 0 , 14, WHITE, 4.8685 * 10**24)

    planets = [sun, earth, mars ,mercury, venus]

    while run:
        clock.tick(FPS)

        # window.fill(WHITE)
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in planets:
            planet.draw(window)
        
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
