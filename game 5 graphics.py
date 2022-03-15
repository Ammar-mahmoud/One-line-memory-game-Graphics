from cgi import print_directory
from re import I
from tkinter import font
import pygame
from time import sleep
import random
from pygame import mixer
pygame.init()
surface = pygame.display.set_mode((1350 , 700))
pygame.display.set_caption("Graphics Game 5")

char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
nums_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # the players choose from it
list1 = [ ] # the random list with 20 char
temp_list = []
temp_list2 = []

for i in range(10):
          list1.append(random.choice(char_list)) # now list1 has 10 random char
list1 = list1 * 2 # become 20 each char is repeated at least twice
random.shuffle(list1) # to make ther order is random

white = (255,255,255) #RGB
black = (0,0,0)
red = (255,0,0)
color_rec_start = (10 , 210 , 250)
color_rec_start2 = (0 , 190 , 220)
color1 = (0,250,80)
color2 = (0,150,150)

def music():
          mixer.init() #for music
          pygame.mixer.music.load("videoplayback (14).wav") # the path of music
          mixer.music.play()
music()

def two_rec(first , sec):
          backG =  pygame.image.load("resize-16462576611896774611abstractgrungedecorativereliefnavybluestuccowalltexturewideangleroughcoloredbackground125828311.jpg") # the path of back ground
          surface.blit(backG, (0,0))
          font = pygame.font.Font('freesansbold.ttf', 70)
          text = font.render(first, True, black )   # to start the game you should click on the start rect                     
          pygame.draw.rect(surface, color_rec_start ,(525, 300 , 300 , 100))
          textRect = text.get_rect()
          textRect.center = (1350 // 2, 700 // 2)
          surface.blit(text, textRect)
          text = font.render("GAME 5" ,  True , red)
          surface.blit(text , (1350//2 -140 , 200 ))
          font = pygame.font.Font('freesansbold.ttf', 40)
          text = font.render(sec, True, black )
          pygame.draw.rect(surface, color_rec_start2 ,(575, 500 , 200 , 80))
          textRect = text.get_rect()
          textRect.center = (1350 // 2, 540)
          surface.blit(text, textRect)
          pygame.display.update()


def turn_win(n): # for determine the turn 
          font = pygame.font.Font('freesansbold.ttf', 70)
          pygame.draw.rect(surface, black ,(425, 175 , 500 , 80))
          text = font.render(n , True , red)
          textRect = text.get_rect()
          textRect.center = (675 , 215)
          surface.blit(text, textRect)
          pygame.display.update()

def game():
          turn = 0  # if turn is even number then player 1 play if odd number then player 2 play
          player_1 = 0  # score for player1
          player_2 = 0  # score for player2
          pygame.time.delay(60) 
          backG =  pygame.image.load("resize-16462576611896774611abstractgrungedecorativereliefnavybluestuccowalltexturewideangleroughcoloredbackground125828311.jpg") # the path of back ground
          surface.blit(backG, (0,0))
          for i in range(1,11): # drow the 20 cards
                    pygame.draw.rect(surface, color2 ,(50*i + 80 *(i-1), 300 , 80 , 120))
                    pygame.draw.rect(surface, color2 ,(50*i + 80 *(i-1), 500 , 80 , 120))
                    font = pygame.font.Font('freesansbold.ttf', 70)
                    text = font.render(str(i), True, black )
                    textRect = text.get_rect()
                    textRect.center = ((50*i + 80 *(i-1))+40, 360)
                    surface.blit(text, textRect)
                    text = font.render(str(i+10), True, black ) #cards numbering
                    textRect = text.get_rect()
                    textRect.center = ((50*i + 80 *(i-1))+40, 560)
                    surface.blit(text, textRect)
          text = font.render("player 1 score :        player 2 score :" , True , color1)
          surface.blit(text , (30,50))
          pygame.draw.rect(surface, black ,(580, 40 , 80 , 100))
          pygame.draw.rect(surface, black ,(1250, 40 , 80 , 100))
          turn_win("player 1 play") # we start by player 1
          pygame.display.update() # to update the screen
          while True :
                    
                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT: # to quit
                                                  quit()
                                        mx , my = pygame.mouse.get_pos() # x and y coordinates
                                        b1 , b2 , b3 = pygame.mouse.get_pressed() # b1 : right click , b2 : mouse wheel , b3 : lift click
                                        if b1 and my < 420 and my > 300 :
                                                  for i in range(1,11):
                                                            if  (50*i + 80*(i-1)) < mx and (50*i + 80*i) > mx and i in nums_list: # to determine which card is choosed
                                                                      pygame.draw.rect(surface, color2 ,(50*i + 80 *(i-1), 300 , 80 , 120))
                                                                      text = font.render(list1[i-1], True, black )
                                                                      surface.blit(text,((50*i + 80 *(i-1))+18, 330))
                                                                      pygame.display.update()
                                                                      temp_list.append(list1[i-1])
                                                                      temp_list2.append(i) 
                                                                      nums_list[i-1] = "*"
                                                                      
                                        if b1 and my < 620 and my > 500 : # to determine which card is choosed
                                                  for i in range(1,11):
                                                            if   (50*i + 80*(i-1)) < mx and (50*i + 80*i) > mx and (i+10) in nums_list :
                                                                      pygame.draw.rect(surface, color2 ,(50*i + 80 *(i-1), 500 , 80 , 120))
                                                                      text = font.render(list1[i+9], True, black )
                                                                      surface.blit(text,((50*i + 80 *(i-1))+18, 530))
                                                                      pygame.display.update()
                                                                      temp_list.append(list1[i+9])
                                                                      temp_list2.append(i+10)
                                                                      nums_list[i+9] = "*"

                                        if len(temp_list) == 2 : # when plarer 1 play and player 2 play
                                                  if turn % 2 == 1 :
                                                            turn_win("player 1 play")
                                                  if turn % 2 == 0 :
                                                            turn_win("player 2 play")
                                                  sleep(2)

                                                  if temp_list[0]==temp_list[1]: # If the two characters match, the player wins a point and these two characters are covered with * 
                                                            for i in (temp_list2):
                                                                      if i <= 10:
                                                                                pygame.draw.rect(surface, color2 ,(50*i + 80 *(i-1), 300 , 80 , 120))
                                                                                text = font.render("*", True, black )
                                                                                surface.blit(text,((50*i + 80 *(i-1))+10, 330))
                                                                                pygame.display.update()
                                                                                nums_list[i-1] = "*"


                                                                      else :
                                                                                pygame.draw.rect(surface, color2 ,(50*(i-10) + 80 *(i-11), 500 , 80 , 120))
                                                                                text = font.render("*", True, black )
                                                                                surface.blit(text,((50*(i-10) + 80 *(i-11))+18, 530))
                                                                                pygame.display.update()
                                                                                nums_list[i-1] = "*"
                                                                                pygame.display.update()

                                                                      if turn % 2 == 0 and i == temp_list2[1]:
                                                                                player_1 = player_1 + 1
                                                                                pygame.draw.rect(surface, black ,(580, 40 , 80 , 100))
                                                                                text = font.render(str(player_1), True, white )
                                                                                surface.blit(text,(600 , 60))
                                                                      elif turn % 2 == 1 and i == temp_list2[1] : 
                                                                                player_2 = player_2 + 1
                                                                                pygame.draw.rect(surface, black ,(1250, 40 , 80 , 100))
                                                                                text = font.render(str(player_2), True, white )
                                                                                surface.blit(text,(1270 , 60))
                                                                      pygame.display.update()
      
                                                  else :
                                                            for i in (temp_list2):
                                                                      if i <= 10:
                                                                                pygame.draw.rect(surface, color2 ,(50*i + 80 *(i-1), 300 , 80 , 120))
                                                                                text = font.render(str(i), True, black )
                                                                                surface.blit(text,((50*i + 80 *(i-1))+18, 330))
                                                                                pygame.display.update()
                                                                                nums_list[i-1] = i
                                                                                pygame.display.update()
                                                                                

                                                                      else :
                                                                                pygame.draw.rect(surface, color2 ,(50*(i-10) + 80 *(i-11), 500 , 80 , 120))
                                                                                text = font.render(str(i), True, black )
                                                                                surface.blit(text,((50*(i-10) + 80 *(i-11)), 530))
                                                                                pygame.display.update()
                                                                                nums_list[i-1] = i
                                                                                pygame.display.update()

                                                  turn = turn + 1
                                                  temp_list.clear()
                                                  temp_list2.clear()
                                        
                                        if player_1 == 5 and player_2 != 4 : # when player 1 win 
                                                  pygame.draw.rect(surface, black ,(425, 175 , 500 , 80))
                                                  text = font.render("player 1 win" , True , red)
                                                  textRect = text.get_rect()
                                                  textRect.center = (675 , 215)
                                                  surface.blit(text, textRect)
                                        if player_1 == 5 and player_2 != 4 :
                                                  turn_win("player 1 win") # to print player 1 win on screen
                                                  sleep(4)
                                                  again()
                                                  
                                        if player_2 == 5 and player_1 != 4 : # when player 2 win 
                                                  turn_win("player 2 win") # to print player 2 win on screen
                                                  sleep(4)
                                                  again()

                                        if (player_1 == 5 and player_2 == 4) or (player_2 == 5 and player_1 == 4) : # in the case of tie
                                                  turn_win("no one win")
                                                  sleep(4)
                                                  again()
                                                  
def again():
          two_rec('again' , 'quit')
          while True :
                    for event in pygame.event.get():
                              if event.type == pygame.MOUSEBUTTONDOWN:
                                        mx , my = pygame.mouse.get_pos()
                                        b1 , b2 , b3 = pygame.mouse.get_pressed() 
                                        if b1 and my > 300 and my < 400 and mx > 525 and mx < 825 :
                                                  music()
                                                  game()
                                        elif b1 and my > 500 and my < 580 and mx > 575 and mx < 775 : # so quit 
                                                  quit()
                                                                                             
def start_game(): # the game start from here
          
          backG =  pygame.image.load("resize-16462576611896774611abstractgrungedecorativereliefnavybluestuccowalltexturewideangleroughcoloredbackground125828311.jpg")
          surface.blit(backG, (0,0))
          two_rec('start' , 'quit')

          font = pygame.font.Font('freesansbold.ttf', 40)
          text = font.render("Name : Ammar Mahmoud AbdEl-hafez" , True , color1)
          surface.blit(text , (50,50))
          text = font.render("ID : 20210254 " ,  True , color1)
          surface.blit(text , (50,100))

          pygame.display.update()
          while True :
          
                    for event in pygame.event.get():
                              if event.type == pygame.MOUSEBUTTONDOWN:
                                        mx , my = pygame.mouse.get_pos()
                                        b1 , b2 , b3 = pygame.mouse.get_pressed() 
                                        if b1 and my > 300 and my < 400 and mx > 525 and mx < 825 : # so start the game
                                                  game()
                                        elif b1 and my > 500 and my < 580 and mx > 575 and mx < 775 : # so quit 
                                                  quit()
          
start_game()
