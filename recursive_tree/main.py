import pygame
import math

def draw_tree(surface, branchLen, x, y, dx, dy, angle):
    if branchLen > 0:
        pygame.draw.line(surface, (0, 0, 0), (x, y), (x + dx, y - dy),
            1 + branchLen // 8)
        x = x + dx
        y = y - dy
        dx = branchLen * math.sin(math.radians(angle))
        dy = branchLen * math.cos(math.radians(angle))
        draw_tree(surface, branchLen - 15, x, y, dx, dy, angle + 20)
        draw_tree(surface, branchLen - 15, x, y, -dx, dy, angle + 20)

def main():
    width = 600
    height = 600
    window = pygame.display.set_mode((width, height))
    window.fill((255, 255, 255))
    draw_tree(window, 75, width // 2, height, 0, 75, 20)

    running = True
    while running:
        pygame.time.wait(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

if __name__ == "__main__": main()
