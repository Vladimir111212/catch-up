from pygame import *

x1 = 100
y1 = 300
x2 = 400
y2 = 300

win = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'), (700, 500))
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))


clock = time.Clock()
FPS = 60
speed = 6
 
game = True
while game:
    win.blit(background, (0, 0))
    win.blit(sprite1, (x1, y1))
    win.blit(sprite2, (x2, y2))

    keys_press = key.get_pressed()

    if keys_press[K_LEFT] and x1 > -5:
        x1 -= speed
    if keys_press[K_RIGHT] and x1 < 600:
        x1 += speed
    if keys_press[K_UP] and y1 > -2:
        y1 -= speed
    if keys_press[K_DOWN] and y1 < 400:
        y1 += speed

    if keys_press[K_a] and x2 > -5:
        x2 -= speed
    if keys_press[K_d] and x2 < 600:
        x2 += speed
    if keys_press[K_w] and y2 > -2:
        y2 -= speed
    if keys_press[K_s] and y2 < 400:
        y2 += speed


    for i in event.get():
        if i.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
    
#создай окно игры

#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»