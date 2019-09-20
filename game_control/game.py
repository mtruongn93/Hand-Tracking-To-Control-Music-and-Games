import pygame
import time
import random
import cv2

# creating window
pygame.init()

black = (0,0,0)
red = (255,0,0)
display_width = 800
display_height = 600
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing Game")
clock = pygame.time.Clock()

cars = pygame.image.load("image/car0.png")
cars = pygame.transform.scale(cars,(56,125))
backgroundpic=pygame.image.load("image/background.png")
car_width = 56

hand_cascade = cv2.CascadeClassifier('../cascade5.xml')

def score_system(passed,score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed: " + str(passed), True, black)
    score = font.render("Score: " + str(score), True, red)
    gamedisplays.blit(text, (115,270))
    gamedisplays.blit(score, (115,290))

def obstacle(obs_startx, obs_starty, obs):
    obs_pic = pygame.image.load("image/car{}.png".format(obs))
    obs_pic = pygame.transform.scale(obs_pic,(56,125))
    obs_pic = pygame.transform.rotate(obs_pic, 180)
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))


def text_object(text,font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_object(text,largetext)
    textrect.center = (display_width/2, display_height/2)
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("Crashed !!!!")

def background():
    gamedisplays.blit(backgroundpic,(-10,0))


def car(x,y):
    gamedisplays.blit(cars,(x,y))

# The game runs here
def game_loop():
    x = display_width * 0.45
    y = display_height * 0.8
    x_change = 0


    passed = 0
    score = 0
    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200, (display_width - 200))
    obs_starty = -750
    obs_width = 54
    obs_height = 120
    side1 = 200
    side2 = 650 - car_width
    cap = cv2.VideoCapture(0)

    bumped = False
    while not bumped:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hands = hand_cascade.detectMultiScale(gray, 1.2, 5)

        for (x_video,y_video,w_video,h_video) in hands:
            cv2.rectangle(img,(x_video,y_video),
            (x_video+w_video,y_video+h_video),(255,0,0),2)
            # pyautogui.moveTo(1920 - x*4, 1080 - y*2, duration = 0.5)
            if len(hands) == 0:
                x_change = 0
            elif x_video < 510/4:
                x_change = 5
            elif x_video >= 510/4:
                x_change = -5



        x+=x_change



        background()

        obs_starty -= obstacle_speed/4
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed

        car(x,y)
        score_system(passed,score)

        if x > side2 or x < side1:
            crash()

        if x > display_width - (car_width + 100 ) or x < side1:
            crash()

        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(side1, side2)
            obs=random.randrange(0,6)
            passed = passed + 1
            score = passed * 10

        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()

        cv2.imshow('img',img)
        k = cv2.waitKey(1)
        if k == 27:
            break

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
