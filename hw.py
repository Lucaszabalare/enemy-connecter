import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "Susie connect enemy"

start_time = 0
total_time = 0
end_time = 0
number_of_enemies = 10
next_enemy = 0
current_enemy = 0

notcats = []
lines = []

def creat_notcats():
    global start_time
    for i in range(number_of_enemies):
        enemy = Actor("enemy")
        enemy.pos = randint(40,WIDTH - 50),randint(40,HEIGHT - 50)
        notcats.append(enemy)
    start_time = time()

def draw():
    global total_time
    screen.fill(color ="orange")

    num = 1
    for enemy in notcats:
        screen.draw.text(str(num),(enemy.pos[0],enemy.pos[1] + 30),color = "black")
        enemy.draw()
        num = num + 1

    for line in lines:
        r = randint(1,255)
        g = randint(1,255)
        b = randint(1,255)
        screen.draw.line(line[0],line[1],(r,g,b))
    
    if current_enemy < number_of_enemies:
        total_time = time() - start_time

        screen.draw.text(str(round(total_time,1)),(15,15),fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)),(15,15),fontsize = 30)
    

def update():
    pass

def on_mouse_down(pos):
    global current_enemy, lines
    if current_enemy < number_of_enemies:
        if notcats[current_enemy].collidepoint(pos):
            if current_enemy:
                lines.append((notcats[current_enemy - 1].pos , notcats[current_enemy].pos))
            current_enemy = current_enemy + 1
            
        else:
            lines = []
            current_enemy = 0
        


creat_notcats()
pgzrun.go()
        