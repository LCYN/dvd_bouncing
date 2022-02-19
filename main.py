import pygame 
import random

pygame.init()
sx = 1450
sy = 820
screen = pygame.display.set_mode((sx, sy))
pygame.display.set_caption("dvd bouncing")
dvd = pygame.image.load('dvd.png')
pygame.display.set_icon(dvd)
clock = pygame.time.Clock()
dvd = pygame.transform.scale(dvd, (dvd.get_width()*0.6, dvd.get_height()*0.6))
def change(a, b, c):
    tem = dvd.convert_alpha()
    tem_mask = pygame.mask.from_surface(tem)
    tmp = tem_mask.to_surface()
    tmp.set_colorkey((0, 0, 0))
    X, Y = tmp.get_size()
    for xx in range(X):
        for yy in range(Y):
            if tmp.get_at((xx, yy))[0] != 0:
                tmp.set_at((xx, yy), (a, b, c))
    return tmp
showdvd = []
s = []
ok = True
x = []
y = []
num = 0
while ok:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            ok = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            showdvd.append(change(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            x.append(i.pos[0])
            y.append(i.pos[1])
            s.append([5, 5])
            num += 1
    screen.fill((0, 0, 0))
    for i in range(num):
        screen.blit(showdvd[i], (x[i], y[i]))
        x[i] += s[i][0]
        y[i] += s[i][1]
        if x[i] < 0:
            s[i][0] = abs(s[i][0])
            showdvd[i] = change(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if x[i] + dvd.get_width() > sx:
            s[i][0] = -abs(s[i][0])
            showdvd[i] = change(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if y[i] < 0:
            s[i][1] = abs(s[i][1])
            showdvd[i] = change(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if y[i] + dvd.get_height() > sy:
            s[i][1] = -abs(s[i][1])
            showdvd[i] = change(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.display.update()
    clock.tick(60)


    
