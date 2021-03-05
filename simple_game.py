

#Game based on the code in example.py
#Import pygame library to use necessary game making functions
#Import random to generate random numbers for enemy and prize position later on 
import pygame 
import random 



#Initialize the pygame modules to get everything started
pygame.init() 



#Keep screen dimensions same as in example to keep things simple for myself
#Use pygame.display.set_mode() to create screen. Still copying example code at this point
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) 




#Create the hero character of the game for user as well as three enemies and the prize by bringing in images and declraing variables to respective images
#Used meme images to avoid copywriting issues
player = pygame.image.load("Player1.jpg")
enemy = pygame.image.load("villain.jpeg")
enemy2 = pygame.image.load("villain.jpeg")
enemy3 = pygame.image.load("villain.jpeg")
prize = pygame.image.load("prize1.jpg")




#Get the width and height of the images in order to do boundary detection
#Pretty much just copied example code again but added the dimensions for the extra images
image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()




#Store the positions of the player, enemies and prize as variables to be used in while loop that runs the game later on 
#Make the enemy and prize start at a random y position on far right of screen and player starting position on the far left
playerXPosition = 100
playerYPosition = 50

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

prizeXPosition =  750
prizeYPosition =  random.randint(0, screen_height - prize_height)




#Use booleans from example code to check if the directional keys are being pressed and set them by default to False
keyUp= False
keyDown = False
keyLeft = False
keyRight = False




#Use pre-approved while loop from example to run the game
#I mainly kept the while loop the same while modifying the code within this loop to meet task requirements
while 1:
    
    #Use .fill() to clear screen
    #Insert player, enemy and prize images on game screen with .blit() and player positional variables from earlier
    #Keep screen updated with pygame.display.flip()
    screen.fill(0) 
    
    screen.blit(player, (playerXPosition, playerYPosition))
    
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()
    
    
    
    
    #Use pre-approved for loop to loop through events in the game
    #I took out the option to quit the game because it runs for such a short period of time it would actually be easier for user to just lose on purpose to end the program
    #Create events to check which directional button player is pressing (if any)using K_UP, K_DOWN, K_LEFT, K_RIGHT
    #Change directional boolean values from earlier based on which button is down
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:  
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        #Event for no keys being pressed
        #If no key is being pressed, key(x) boolean value from earlier stays False        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
            
            
            
            
    
    #Write code that moves player accordingly when directional buttons are pressed and make sure that player cannot leave the screen
    #Again, mostly written for me already in example, I just had to add left and right directions
    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0 : 
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
            
            
    
    
    
    #Use example code with pygame.Rect(.get_rect()) to create bounding boxes around the images of the player, enemy and prize
    #If these bounding boxes collide then the player either wins or loses depending on which box they hit
    #variableBox. top/left keeps the image inside the box as it moves
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
      
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    
    
    
    
    #Now use various if statements from example code to determine what happens in the game should there be a collision
    #I removed the option of winning the game by having the enemy exit the screen
    #And added the option of winning by colliding with the prize
    #Once their is a collision the game ends and the user is notified of their victory or defeat
    if playerBox.colliderect(enemyBox):
        
        print("You lose!")       
        pygame.quit()
        exit(0)
        
    if playerBox.colliderect(enemy2Box): 
        
        print("You lose!") 
        pygame.quit()
        exit(0)
     
    
    if playerBox.colliderect(enemy3Box): 
        print("You lose!") 
        pygame.quit()
        exit(0)
        
    
    if playerBox.colliderect(prizeBox): 
        print("You win!") 
        pygame.quit()
        exit(0)
    
 




    
    # Make enemy approach the player with positional variable from earlier and -= to change x axis value to make enemy move leftwards
    #I couldn't figure out how to make the enemies start at different times so I just made them all move at different speeds, which I think turned out better in any case    
    enemyXPosition -= 0.30
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.05
    
 
  
