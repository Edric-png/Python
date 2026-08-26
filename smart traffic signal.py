import pygame
pygame.init()

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

CAR_EVENT = pygame.USEREVENT + 1

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(100, 250))
        self.velocity = 4

    def update(self):
        self.rect.x += self.velocity
        if self.rect.right >= 800 or self.rect.left <= 0:
            pygame.event.post(pygame.event.Event(CAR_EVENT))

car = Car()
cars = pygame.sprite.Group(car)
signal = (0, 255, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == CAR_EVENT:
            car.velocity *= -1
            car.image.fill((255, 0, 0) if signal == (0, 255, 0) else (0, 0, 255))
            signal = (255, 0, 0) if signal == (0, 255, 0) else (0, 255, 0)

    cars.update()
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (100, 100, 100), (0, 220, 800, 100))
    pygame.draw.circle(screen, signal, (700, 100), 30)
    cars.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
