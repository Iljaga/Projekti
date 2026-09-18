import pygame

pygame.init()

LEVEYS = 800
KORKEUS = 600

naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Lentokonepeli")

kello = pygame.time.Clock()

# Lentokoneen sijainti
x = 100
y = 300

kaynnissa = True

while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False

    nappaimet = pygame.key.get_pressed()

    if nappaimet[pygame.K_LEFT]:
        x -= 5

    if nappaimet[pygame.K_RIGHT]:
        x += 5

    if nappaimet[pygame.K_UP]:
        y -= 5

    if nappaimet[pygame.K_DOWN]:
        y += 5

    # Tausta
    naytto.fill((100, 180, 255))

    # Väliaikainen "lentokone"
    pygame.draw.polygon(
        naytto,
        (255, 255, 255),
        [
            (x, y),
            (x - 30, y + 15),
            (x - 20, y),
            (x - 30, y - 15)
        ]
    )

    pygame.display.flip()

    kello.tick(60)

pygame.quit()