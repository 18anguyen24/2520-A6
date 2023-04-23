# Imports
import pygame
import math
import random

# global variables(color RGB, size of game window, visibility, game title)
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
CK = (127, 33, 33)
SIZE = (800, 600)
TITLE = "Major League Soccer"
DARKNESS = pygame.Surface(SIZE)
SEE_THROUGH = pygame.Surface((800, 180))
SCREEN = pygame.display.set_mode(SIZE)
LIGHT_COLOR = YELLOW


#----------- drawing gaming objects -----------------
def draw_cloud(SEE_THROUGH, cloud_color, x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])

def draw_fence(sky_color, clouds, cloud_color, day):
    # fence
    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(SCREEN, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(SCREEN, NIGHT_GRAY, [x, y], [x, y + 15], 1)

    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(SCREEN, NIGHT_GRAY, [x, y], [x + 800, y], 1)

    if day:
        pygame.draw.ellipse(SCREEN, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(SCREEN, WHITE, [520, 50, 40, 40])
        pygame.draw.ellipse(SCREEN, sky_color, [530, 45, 40, 40])

    for c in clouds:
        draw_cloud(SEE_THROUGH, cloud_color, c[0], c[1])

def draw_stars(sky_color, day, stars):
    SCREEN.fill(sky_color)
    SEE_THROUGH.fill(CK)
    SEE_THROUGH.set_colorkey(CK)

    if not day:
        # stars
        for s in stars:
            pygame.draw.ellipse(SCREEN, WHITE, s)

def draw_field(field_color, stripe_color):
    pygame.draw.rect(SCREEN, field_color, [0, 180, 800, 420])
    pygame.draw.rect(SCREEN, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(SCREEN, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(SCREEN, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(SCREEN, stripe_color, [0, 492, 800, 82])
    
def draw_scoreboard_bounds():
    # out of bounds lines
    pygame.draw.line(SCREEN, WHITE, [0, 580], [800, 580], 5)
    # left
    pygame.draw.line(SCREEN, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(SCREEN, WHITE, [140, 220], [660, 220], 3)
    # right
    pygame.draw.line(SCREEN, WHITE, [660, 220], [800, 360], 5)

    # safety circle
    pygame.draw.ellipse(SCREEN, WHITE, [240, 500, 320, 160], 5)

    # score board pole
    pygame.draw.rect(SCREEN, GRAY, [390, 120, 20, 70])

    # score board
    pygame.draw.rect(SCREEN, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(SCREEN, WHITE, [302, 42, 198, 88], 2)
    
def draw_goal():
        pygame.draw.rect(SCREEN, WHITE, [320, 140, 160, 80], 5)
        pygame.draw.line(SCREEN, WHITE, [340, 200], [460, 200], 3)
        pygame.draw.line(SCREEN, WHITE, [320, 220], [340, 200], 3)
        pygame.draw.line(SCREEN, WHITE, [480, 220], [460, 200], 3)
        pygame.draw.line(SCREEN, WHITE, [320, 140], [340, 200], 3)
        pygame.draw.line(SCREEN, WHITE, [480, 140], [460, 200], 3)

        # 18 yard line goal box
        pygame.draw.line(SCREEN, WHITE, [260, 220], [180, 300], 5)
        pygame.draw.line(SCREEN, WHITE, [180, 300], [620, 300], 3)
        pygame.draw.line(SCREEN, WHITE, [620, 300], [540, 220], 5)

        # 6 yard line goal box
        pygame.draw.line(SCREEN, WHITE, [310, 220], [270, 270], 3)
        pygame.draw.line(SCREEN, WHITE, [270, 270], [530, 270], 2)
        pygame.draw.line(SCREEN, WHITE, [530, 270], [490, 220], 3)

        # arc at the top of the goal box
        pygame.draw.arc(SCREEN, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)
        
def draw_lights():
    # light pole 1
    pygame.draw.rect(SCREEN, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(SCREEN, GRAY, [150, 195, 20, 10])

    # light pole 2
    pygame.draw.rect(SCREEN, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(SCREEN, GRAY, [630, 195, 20, 10])

    # lights
    pygame.draw.line(SCREEN, GRAY, [110, 60], [210, 60], 2)
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [110, 40, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [130, 40, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [150, 40, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [170, 40, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [190, 40, 20, 20])
    pygame.draw.line(SCREEN, GRAY, [110, 40], [210, 40], 2)
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [110, 20, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [130, 20, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [150, 20, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [170, 20, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [190, 20, 20, 20])
    pygame.draw.line(SCREEN, GRAY, [110, 20], [210, 20], 2)

    pygame.draw.line(SCREEN, GRAY, [590, 60], [690, 60], 2)
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [590, 40, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [610, 40, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [630, 40, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [650, 40, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [670, 40, 20, 20])
    pygame.draw.line(SCREEN, GRAY, [590, 40], [690, 40], 2)
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [590, 20, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [610, 20, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [630, 20, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [650, 20, 20, 20])
    pygame.draw.ellipse(SCREEN, LIGHT_COLOR, [670, 20, 20, 20])
    pygame.draw.line(SCREEN, GRAY, [590, 20], [690, 20], 2)

def draw_net():
    pygame.draw.line(SCREEN, WHITE, [325, 140], [341, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [330, 140], [344, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [335, 140], [347, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [340, 140], [350, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [345, 140], [353, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [350, 140], [356, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [355, 140], [359, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [360, 140], [362, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [364, 140], [365, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [368, 140], [369, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [372, 140], [373, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [376, 140], [377, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [380, 140], [380, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [384, 140], [384, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [388, 140], [388, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [392, 140], [392, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [396, 140], [396, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [400, 140], [400, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [404, 140], [404, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [408, 140], [408, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [412, 140], [412, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [416, 140], [416, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [420, 140], [420, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [424, 140], [423, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [428, 140], [427, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [432, 140], [431, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [436, 140], [435, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [440, 140], [438, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [445, 140], [441, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [450, 140], [444, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [455, 140], [447, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [460, 140], [450, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [465, 140], [453, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [470, 140], [456, 200], 1)
    pygame.draw.line(SCREEN, WHITE, [475, 140], [459, 200], 1)

    # net part 2
    pygame.draw.line(SCREEN, WHITE, [320, 140], [324, 216], 1)
    pygame.draw.line(SCREEN, WHITE, [320, 140], [326, 214], 1)
    pygame.draw.line(SCREEN, WHITE, [320, 140], [328, 212], 1)
    pygame.draw.line(SCREEN, WHITE, [320, 140], [330, 210], 1)
    pygame.draw.line(SCREEN, WHITE, [320, 140], [332, 208], 1)
    pygame.draw.line(SCREEN, WHITE, [320, 140], [334, 206], 1)
    pygame.draw.line(SCREEN, WHITE, [320, 140], [336, 204], 1)
    pygame.draw.line(SCREEN, WHITE, [320, 140], [338, 202], 1)

    # net part 3
    pygame.draw.line(SCREEN, WHITE, [480, 140], [476, 216], 1)
    pygame.draw.line(SCREEN, WHITE, [480, 140], [474, 214], 1)
    pygame.draw.line(SCREEN, WHITE, [480, 140], [472, 212], 1)
    pygame.draw.line(SCREEN, WHITE, [480, 140], [470, 210], 1)
    pygame.draw.line(SCREEN, WHITE, [480, 140], [468, 208], 1)
    pygame.draw.line(SCREEN, WHITE, [480, 140], [466, 206], 1)
    pygame.draw.line(SCREEN, WHITE, [480, 140], [464, 204], 1)
    pygame.draw.line(SCREEN, WHITE, [480, 140], [462, 202], 1)

    # net part 4
    pygame.draw.line(SCREEN, WHITE, [324, 144], [476, 144], 1)
    pygame.draw.line(SCREEN, WHITE, [324, 148], [476, 148], 1)
    pygame.draw.line(SCREEN, WHITE, [324, 152], [476, 152], 1)
    pygame.draw.line(SCREEN, WHITE, [324, 156], [476, 156], 1)
    pygame.draw.line(SCREEN, WHITE, [324, 160], [476, 160], 1)
    pygame.draw.line(SCREEN, WHITE, [324, 164], [476, 164], 1)
    pygame.draw.line(SCREEN, WHITE, [324, 168], [476, 168], 1)
    pygame.draw.line(SCREEN, WHITE, [324, 172], [476, 172], 1)
    pygame.draw.line(SCREEN, WHITE, [324, 176], [476, 176], 1)
    pygame.draw.line(SCREEN, WHITE, [335, 180], [470, 180], 1)
    pygame.draw.line(SCREEN, WHITE, [335, 184], [465, 184], 1)
    pygame.draw.line(SCREEN, WHITE, [335, 188], [465, 188], 1)
    pygame.draw.line(SCREEN, WHITE, [335, 192], [465, 192], 1)
    pygame.draw.line(SCREEN, WHITE, [335, 196], [465, 196], 1)

def draw_flag():
    # stands right
    pygame.draw.polygon(SCREEN, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(SCREEN, WHITE, [[680, 180], [800, 100], [800, 290]])

    # stands left
    pygame.draw.polygon(SCREEN, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(SCREEN, WHITE, [[120, 180], [0, 100], [0, 290]])
    # people

    # corner flag right
    pygame.draw.line(SCREEN, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.polygon(SCREEN, RED, [[132, 190], [125, 196], [135, 205]])

    # corner flag left
    pygame.draw.line(SCREEN, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
    pygame.draw.polygon(SCREEN, RED, [[668, 190], [675, 196], [665, 205]])

#--------main-----------#
def main():
    # Initialize game engine
    pygame.init()

    # Window
    pygame.display.set_caption(TITLE)

    # Timer
    clock = pygame.time.Clock()
    refresh_rate = 60

    DARKNESS.set_alpha(200)
    DARKNESS.fill((0, 0, 0))

    SEE_THROUGH.set_alpha(150)
    SEE_THROUGH.fill((124, 118, 135))


    # lighting settings
    lights_on = True
    day = True

    #initialize stars and clouds
    stars = []
    for n in range(200):
        x = random.randrange(0, 800)
        y = random.randrange(0, 200)
        r = random.randrange(1, 2)
        stars.append([x, y, r, r])

    clouds = []
    for i in range(20):
        x = random.randrange(-100, 1600)
        y = random.randrange(0, 150)
        clouds.append([x, y])

    # Game loop
    done = False
    while not done:
        # Event processing (React to key presses, mouse clicks, etc.)
        # for now, we'll just check to see if the X is clicked
        for event in pygame.event.get():
            # EXIT LOOP
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:  #change between lighting settings
                    lights_on = not lights_on
                elif event.key == pygame.K_d:  #change between day settings
                    day = not day

        # ---Game logic (Check for collisions, update points, etc.)---

        #change lightbulb color based on user input L
        global LIGHT_COLOR
        if lights_on:
            LIGHT_COLOR = YELLOW
        else:
            LIGHT_COLOR = SILVER
        #change daytime color based on user input D
        if day:
            sky_color = BLUE
            field_color = GREEN
            stripe_color = DAY_GREEN
            cloud_color = WHITE
        else:
            sky_color = DARK_BLUE
            field_color = DARK_GREEN
            stripe_color = NIGHT_GREEN
            cloud_color = NIGHT_GRAY

        # DARKNESS
        if not day and not lights_on:
            SCREEN.blit(DARKNESS, (0, 0))

        for c in clouds:
            c[0] -= 0.5

            if c[0] < -100:
                c[0] = random.randrange(800, 1600)
                c[1] = random.randrange(0, 150)

        #draw stars if night
        draw_stars(sky_color, day, stars)

        #draw field
        draw_field(field_color, stripe_color)

        #fence
        draw_fence(sky_color, clouds, cloud_color, day)

        SCREEN.blit(SEE_THROUGH, (0, 0))

        #scoreboard
        draw_scoreboard_bounds()

        # goal
        draw_goal()

        # lights
        draw_lights()

        # net
        draw_net()

        # flag
        draw_flag()

        # Update SCREEN (Actually draw the picture in the window.)
        pygame.display.flip()

        # Limit refresh rate of game loop
        clock.tick(refresh_rate)

    # Close window and quit
    pygame.quit()

if __name__ == "__main__":
    main()