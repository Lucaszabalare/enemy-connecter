import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "Susie connect enemy"

start_time = 0
total_time = 0
end_time = 0
number_of_cats = 10
next_cat = 0

notcats = []
lines = []

def creat_notcats():
    global start_time
    for i in range(number_of_cats):
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

def update():
    pass



creat_notcats()
pgzrun.go()
        