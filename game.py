import pygame

# Initialize Pygame
pygame.init()

# SET UP GAME AND VARIABLES

screen = pygame.display.set_mode((1200, 800))
roleindex = 0
font = pygame.font.Font(None, 36)
currentrole = "Sheriff"
display_text = False
# LOAD AND INITIALIZE IMAGES

# two of spades
c2_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/2_of_spades.png")
c2 = pygame.transform.scale(c2_1, (c2_1.get_width() // 1.5, c2_1.get_height() // 1.5))
c2_rect = c2.get_rect()  # Get the Rect object for positioning
# three of spades
c3_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/3_of_spades.png")
c3 = pygame.transform.scale(c3_1, (c3_1.get_width() // 1.5, c3_1.get_height() // 1.5))
c3_rect = c3.get_rect() 
# four of spades
c4_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/4_of_spades.png")
c4 = pygame.transform.scale(c4_1, (c4_1.get_width() // 1.5, c4_1.get_height() // 1.5))
c4_rect = c4.get_rect() 
# five of spades
c5_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/5_of_spades.png")
c5 = pygame.transform.scale(c5_1, (c5_1.get_width() // 1.5, c5_1.get_height() // 1.5))
c5_rect = c5.get_rect() 
# six of spades
c6_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/6_of_spades.png")
c6 = pygame.transform.scale(c6_1, (c6_1.get_width() // 1.5, c6_1.get_height() // 1.5))
c6_rect = c6.get_rect() 
# seven of spades
c7_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/7_of_spades.png")
c7 = pygame.transform.scale(c7_1, (c7_1.get_width() // 1.5, c7_1.get_height() // 1.5))
c7_rect = c7.get_rect() 
# eight of spades
c8_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/8_of_spades.png")
c8 = pygame.transform.scale(c8_1, (c8_1.get_width() // 1.5, c8_1.get_height() // 1.5))
c8_rect = c8.get_rect() 
# nine of spades
c9_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/9_of_spades.png")
c9 = pygame.transform.scale(c9_1, (c9_1.get_width() // 1.5, c9_1.get_height() // 1.5))
c9_rect = c9.get_rect() 
# ten of spades
c10_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/10_of_spades.png")
c10 = pygame.transform.scale(c10_1, (c10_1.get_width() // 1.5, c10_1.get_height() // 1.5))
c10_rect = c10.get_rect() 
# jack
cj_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/jack_of_spades2.png")
cj = pygame.transform.scale(cj_1, (cj_1.get_width() // 1.5, cj_1.get_height() // 1.5))
cj_rect = cj.get_rect() 
# queen
cq_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/2_of_clubs.png")
cq = pygame.transform.scale(cq_1, (cq_1.get_width() // 1.5, cq_1.get_height() // 1.5))
cq_rect = cq.get_rect() 
# king
ck_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/king_of_spades2.png")
ck = pygame.transform.scale(ck_1, (ck_1.get_width() // 1.5, ck_1.get_height() // 1.5))
ck_rect = ck.get_rect() 
# ace of spades
ca_1 = pygame.image.load("D:/1_Jason\whattheleetcode\Playing Cards\Playing Cards\PNG-cards-1.3/ace_of_spades.png")
ca = pygame.transform.scale(ca_1, (ca_1.get_width() // 1.5, ca_1.get_height() // 1.5))
ca_rect = ca.get_rect()

# CARD POSITION

c2_rect.x = 450  # x position
c2_rect.y = 100  # y position

c3_rect.x = 450  # x position
c3_rect.y = 100  # y position

c4_rect.x = 450  # x position
c4_rect.y = 100  # y position

c5_rect.x = 450  # x position
c5_rect.y = 100  # y position

c6_rect.x = 450  # x position
c6_rect.y = 100  # y position

c7_rect.x = 450  # x position
c7_rect.y = 100  # y position

c8_rect.x = 450  # x position
c8_rect.y = 100  # y position

c9_rect.x = 450  # x position
c9_rect.y = 100  # y position

c10_rect.x = 450  # x position
c10_rect.y = 100  # y position

cj_rect.x = 450  # x position
cj_rect.y = 100  # y position

cq_rect.x = 450  # x position
cq_rect.y = 100  # y position

ck_rect.x = 450  # x position
ck_rect.y = 100  # y position

ca_rect.x = 450  # x position
ca_rect.y = 100  # y position


# TEXT STUFF

role_surface = font.render('Role: ' + currentrole, True, (0, 0, 0))

# Get the rectangle of the text
role_rect = role_surface.get_rect()
role_rect.center = (600, 600)  # Set text position to the center of the screen

# START START

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
title_surface = font.render('My Game', True, (0, 0, 0))
instruction_surface = small_font.render('Press any key to start', True, (0, 0, 0))

# Function for the start screen
def start_screen():
    while waiting:
        screen.fill(WHITE)
        
        # Draw the title and instruction text
        screen.blit(title_surface, (250, 200))
        screen.blit(instruction_surface, (250, 400))
        
        # Update the display
        pygame.display.flip()
        
        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False  # Exit the start screen and begin the game

# MAIN GAME
def main_screen():
    running = True
    while running:
        # Clear the screen
        screen.fill((255, 255, 255))  # fill with white
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for key press event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Space key pressed
                    display_text = True
        # Draw the image at the new position
        if display_text:
            screen.blit(ca, ca_rect)
        screen.blit(role_surface, role_rect)

        # Update the display
        pygame.display.flip()

# START GAME SEQUENCE
start_screen
main_screen
