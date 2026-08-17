import pygame
import entities.player as player
import entities.building as building


# 1. Initialize all imported pygame modules
pygame.init()

# Create a player
player = player.Player("My City", 1000)

# 2. Set up the drawing window (Width, Height)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#force cursor to be visible
pygame.mouse.set_visible(True)

# 3. Main Game Loop
while running:
    # Look for user input events (like clicking the 'X' button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = event.pos

                box = building.Building("Box", 100, "blue", 10, x, y)
                player.add_building(box)


    # Fill the screen with a solid color (clears the last frame)
    screen.fill("purple")

    # Render game elements here

    for box in player.buildings:
        pygame.draw.rect(screen, box.color, pygame.Rect(box.x, box.y, 50, 50))
        player.add_money(box.production / 60)  # Add production income to the player's money

    print(player)  # Print the player's money to the console for debugging   
    # Update the display to show your changes
    pygame.display.flip()

    # Maintain a steady 60 frames per second (FPS)
    clock.tick(60)

# 4. Cleanly close the window when the loop finishes
pygame.quit()
