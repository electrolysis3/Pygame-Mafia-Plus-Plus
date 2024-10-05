import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup (increased screen size)
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Role Assignment Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.SysFont(None, 40)

# Roles and Cards
roles = ["Spy", "Corrupt Mayor", "Veteran", "Child", "Jester", "Businessman"]
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Game variables
num_players = 6
players = {}
round_num = 1
game_over = False
paused = True
voting = False
selected_player = None
eliminated_player = None

# Assign random roles to players
def assign_roles():
    random_roles = random.sample(roles, num_players)
    for i in range(1, num_players + 1):
        players[i] = {'role': random_roles[i-1], 'card': None, 'eliminated': False, 'rect': None}

# Deal a card to each player
def deal_cards():
    for player in players:
        if not players[player]['eliminated']:
            players[player]['card'] = random.choice(cards)

# Voting phase to eliminate a player
def start_voting():
    global voting
    voting = True

def eliminate_player(player_number):
    players[player_number]['eliminated'] = True
    return player_number

# Main game loop
def main():
    global round_num, game_over, paused, voting, selected_player, eliminated_player

    assign_roles()
    
    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press space to proceed to the next round
                    if not voting:
                        paused = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if voting:
                    mouse_pos = event.pos
                    # Check if a player was clicked
                    for player, info in players.items():
                        if not info['eliminated'] and info['rect'] and info['rect'].collidepoint(mouse_pos):
                            selected_player = player
                            eliminated_player = eliminate_player(player)
                            voting = False
                            paused = True  # Pause after voting

        screen.fill(WHITE)

        if round_num <= 10:
            # Show roles and cards
            y_pos = 50
            for player, info in players.items():
                if not info['eliminated']:
                    role_text = font.render(f"Player {player} - Role: {info['role']}", True, BLACK)
                    card_text = font.render(f"Card: {info['card']}" if info['card'] else "Card: None", True, BLACK)
                    rect = pygame.Rect(50, y_pos, 400, 40)  # Rect for clickable area
                    players[player]['rect'] = rect
                    pygame.draw.rect(screen, BLACK, rect, 2)
                    screen.blit(role_text, (50, y_pos))
                    screen.blit(card_text, (500, y_pos))
                else:
                    elim_text = font.render(f"Player {player} - Eliminated", True, RED)
                    screen.blit(elim_text, (50, y_pos))
                y_pos += 80  # Increase spacing to prevent overlap

            if paused and not voting:
                # Prompt to press space to continue
                prompt_text = font.render("Press SPACE to continue", True, BLACK)
                screen.blit(prompt_text, (WIDTH // 2 - 150, HEIGHT - 100))
            elif not paused:
                # Deal cards every round
                if round_num % 2 != 0:
                    deal_cards()
                else:
                    # Start voting phase
                    start_voting()
                
                round_num += 1
                paused = True  # Pause after each round
            
            if voting:
                vote_text = font.render("Click a player to vote them out!", True, BLACK)
                screen.blit(vote_text, (WIDTH // 2 - 200, HEIGHT - 100))
        else:
            game_over_text = font.render("Game Over!", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
