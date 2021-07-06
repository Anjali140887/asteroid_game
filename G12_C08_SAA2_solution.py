# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:04:10 2021

@author: ANJALI SHARMA
"""

import pygame, sys, math, random

#initialize pygame to  use it's functions
pygame.init()
clock=pygame.time.Clock()

#create a window where game will Run
screen = pygame.display.set_mode((600,600))
#title 
pygame.display.set_caption("Astroid Shower")

#load images
background_image = pygame.image.load("bg2.jpg").convert()
enemy_image = pygame.image.load("e3.png").convert_alpha()
player_image = pygame.image.load("s4.png").convert_alpha()


#creating objects of game
player=pygame.Rect(200,200,30,30)
playerSpeed=20
angle=0
change=0
speed=5
forward=False

bullet=pygame.Rect(0,0,5,5)
bulletState="ready"

enemycount=10
enemies=[]
evlx=[]
evly=[]

for i in range(1,enemycount):
  enemies.append(pygame.Rect(random.randint(0,400),random.randint(0,600),20,20))
  evlx.append(random.randint(-3,3))
  evly.append(random.randint(-3,3))

enemySpeed=1

score=0
over=False
game_font=pygame.font.Font('freesansbold.ttf', 12)
game_over=pygame.font.Font('freesansbold.ttf', 30)

def fire():
  global bulletState
   

def newxy(oldx,oldy,speed,ang):
  ang=math.radians(ang-90)
  nx=oldx+(speed*math.cos(ang))
  ny=oldy+(speed*math.sin(ang))
  return nx,ny


#Game Loop
while True:
  
  screen.blit(background_image,[0,0])
  #event loop to check which key is print
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
        change= 0
      if event.key == pygame.K_UP:
        forward=False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        change =6
      if event.key ==pygame.K_RIGHT:
        change = -6
      if event.key == pygame.K_UP:
        forward=True;      
      if event.key == pygame.K_SPACE and bulletState=="ready":
          bulletState="fired"
        
  
  #move the bullet
  if bulletState == "ready":
      bullet.x=player.x+15
      bullet.y=player.y+15
 
      bangle=angle
    
  if bulletState=="fired":
    nx , bullet.y = newxy(bullet.x, bullet.y, 20 , bangle)
    
    xx = bullet.x - nx
    bullet.x= bullet.x + (xx)
  #change bullet state back to ready when it moves out
  
  if bullet.y<0 or bullet.x<0 or bullet.y>600 or bullet.x>400:
    bulletState="ready"
 
  i=0
  for enemy in enemies:
    enemy.x+=evlx[i]
    enemy.y+=evly[i]
    
    #Move enemy to center once hit the player and display game over
    if enemy.colliderect(player):
      over=True  
      player_image=enemy_image
    if over==True:
      gameovertext=game_over.render("GAME OVER!",False,(100,200,100))
      screen.blit(gameovertext,(100,250))
      
      
    #destroy the enemy
    if enemy.x < -250 or enemy.x > 650 or enemy.y < -250 or enemy.y > 850:  
      evlx[i] = -1*evlx[i]
      evly[i] = -1*evly[i]
    ##### The following code is for score update ####

    i+=1     
    if bullet.colliderect(enemy):
      enemy.y=random.choice([random.randint(-250,0),random.randint(600,840)])
      print(enemy.y)
      enemy.x=random.choice([random.randint(-250,0),random.randint(400,640)])
      print(enemy.x)
      score+=10
      
    screen.blit(enemy_image,enemy)
    #pygame.draw.rect(screen,(123,200,100),enemy)
 
  ###### Redefining player coordinates after the player exits the game window
  if forward:
      nx , player.y = newxy(player.x, player.y, speed , angle)
      xx=player.x-nx
      player.x= player.x + (xx)
  if player.x < 0 :
    player.x = 400
  elif player.x > 400 :
    player.x =0 
  elif player.y < 0 :
    player.y = 600
  elif player.y > 600 :
    player.y =0   
 ###### Redefining player coordinates after the player exits the game window
  angle += change
  angle=angle % 360
  newimg=pygame.transform.rotate(player_image,angle)
  screen.blit(newimg , player)
  
  # pygame.draw.rect(screen,(23,100,100),player)
  
  pygame.draw.rect(screen,(225,225,15),bullet)
  #### Below mentioned code is of game over and score display ######

  scoretext=game_font.render("Score : " + str(score),False,(200,200,200))
  screen.blit(scoretext,(10,10))
  
  pygame.display.flip()
  clock.tick(30)
  #################################################