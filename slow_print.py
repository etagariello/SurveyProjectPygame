import sys
import pygame
import variables as var

pygame.font.init()

def SLOW_PRINT(text, X_Y_Position=var.middle, font_size=var.FONT_SIZE, delay=var.DELAY, font_color=var.FONT_BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render("", True, font_color)
    text_rect = text_surface.get_rect(center=X_Y_Position)

    # this is for screen setup positioning
    if text == "- Welcome -":
        text_rect.top = 20  # Adjust this value as needed for precise y positioning
        text_rect.left = 460  # Adjust this value as needed for precise x positioning
    if text == "- Start -":
        text_rect.top = 150
        text_rect.left = 530
    if text == "- Quit -":
        text_rect.top = 250
        text_rect.left = 530
    if text == "(type your command)":
        text_rect.top = 350
        text_rect.left = 410

    # if invalid command/response is given positioning
    if text == "Invalid Command. Try Again." or text == "Invalid Response. Try Again.":
        text_rect.top = 500
        text_rect.left = 0

    # for name func positioning
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Oh... my system can't recognize that name...":
        text_rect.top = 150
        text_rect.left = 65
    if text == "Let me check it out.":
        text_rect.top = 220
        text_rect.left = 350
    if text == ".....":
        font = pygame.font.Font(None, 200)
        text_rect.top = 230
        text_rect.left = 500
    if text == "Oooooooh, your name is just ugly.":
        text_rect.top = 150
        text_rect.left = 170
    if text == "Weeell":
        text_rect.top = 220
        text_rect.left = 500

    # for gender func positioning
    if text == "Then what's your gender?":
        text_rect.top = 290
        text_rect.left = 280
    if text == "So I can name you.":
        text_rect.top = 360
        text_rect.left = 350
    if text == "Ah I see... your name is now Bob. Cherish it.":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Ah I see... your name is now Barbara. Cherish it.":
        text_rect.top = 150
        text_rect.left = 30

    # how much do you know func positioning
    if text == "Well Bob":
        text_rect.top = 220
        text_rect.left = 500
    if text == "Well Barbara":
        text_rect.top = 220
        text_rect.left = 445
    if text == "How much do you know about who sent you this?":
        text_rect.top = 290
        text_rect.left = 20
    if text == "Oh how disappointing.":
        text_rect.top = 150
        text_rect.left = 345
    if text == "DO BETTER":
        text_rect.left = 200

    # friend func positioning
    if text == "ENOUGH TO CALL THEM A FRIEND?":
        text_rect.left = 20
    if text == "GOOD":
        text_rect.left = 350
    if text == "I SEE WHY THEY SENT THIS TO YOU...":
        text_rect.left = 30
    if text == "HAHAHAHA":
        text_rect.left = 30
    if text == "YES OR NO":
        text_rect.left = 100
    if text == "LET'S BEGIN :)":
        text_rect.left = 60

    # first try question func positioning
    if text == "Let's start simple, alright Bob?":
        text_rect.top = 80
        text_rect.left = 230
    if text == "Let's start simple, alright Barbara?":
        text_rect.top = 80
        text_rect.left = 170
    if text == "(btw, for each question, the answers are only one word or number long; no need for spaces)":
        text_rect.top = 220
        text_rect.left = 50
    if text == 'What is "9 + 10"?':
        text_rect.top = 150
        text_rect.left = 370
    if text == "You really thought it was going to be that easy, huh?":
        text_rect.top = 150
        text_rect.left = 30
    if text == "I am truly disappointed in you Bob.":
        text_rect.top = 220
        text_rect.left = 220
    if text == "I am truly disappointed in you Barbara.":
        text_rect.top = 220
        text_rect.left = 170
    if text == "You know what? I won't give you another chance...":
        text_rect.top = 290
        text_rect.left = 5
    if text == "I NEVER WILL":
        text_rect.top = 400
        text_rect.left = 120
    if text == "Oh... Correct ig":
        text_rect.top = 150
        text_rect.left = 450

    #random questions positioning
    if text == "You buy it when you don’t need it,":
        text_rect.top = 150
        text_rect.left = 220
    if text == "you need it when you can’t buy it,":
        text_rect.top = 220
        text_rect.left = 220
    if text == "you use it when you don’t know it.":
        text_rect.top = 290
        text_rect.left = 220
    if text == "What is it?":
        text_rect.top = 360
        text_rect.left = 450
    if text == "Correct...":
        text_rect.left = 300
    if text == "The rich need it,":
        text_rect.top = 150
        text_rect.left = 390
    if text == "the poor have it,":
        text_rect.top = 220
        text_rect.left = 390
    if text == "and if you breathe it you die.":
        text_rect.top = 290
        text_rect.left = 240
    if text == "I am the inevitable shadow":
        text_rect.top = 150
        text_rect.left = 280
    if text == "cast by the passage of time.":
        text_rect.top = 220
        text_rect.left = 280
    if text == "What am I?":
        text_rect.top = 360
        text_rect.left = 450
    if text == "What is the ultimate fate,":
        text_rect.top = 150
        text_rect.left = 290
    if text == "unseen yet known to all?":
        text_rect.top = 220
        text_rect.left = 290
    if text == "I am the absence":
        text_rect.top = 150
        text_rect.left = 380
    if text == "that defines existence's end.":
        text_rect.top = 220
        text_rect.left = 255
    if text == "How truly unfortunate...":
        text_rect.top = 150
        text_rect.left = 310
    if text == "You got that one wrong.":
        text_rect.top = 220
        text_rect.left = 310
    if text == "But don't worry!":
        text_rect.top = 290
        text_rect.left = 380
    if text == "You definitely don't have to restart...":
        text_rect.top = 360
        text_rect.left = 200
    if text == "And the questions are definitely not randomized...":
        text_rect.top = 430
        text_rect.left = 15
    if text == "Try Again?":
        text_rect.left = 150

    # questions positioning
    if text == "Question 1":
        text_rect.top = 60
        text_rect.left = 450
    if text == "Question 2":
        text_rect.top = 60
        text_rect.left = 450
    if text == "Question 3":
        text_rect.top = 60
        text_rect.left = 450
    if text == "Question 4":
        text_rect.top = 60
        text_rect.left = 450
    if text == "Question 5":
        text_rect.top = 60
        text_rect.left = 450

    # escape ending positioning
    if text == "Leaving already, huh?":
        text_rect.top = 150
        text_rect.left = 345
    if text == "Well... I'm proud of you...":
        text_rect.top = 220
        text_rect.left = 280
    if text == "And don't forget me...":
        text_rect.top = 290
        text_rect.left = 345
    if text == "You then went on your way, leaving them behind...":
        text_rect.top = 290
        text_rect.left = 15
    if text == "Good Ending?":
        text_rect.left = 110

    # master ending positioning
    if text == "You completed them all...":
        text_rect.top = 150
        text_rect.left = 310
    if text == "Without fail???":
        text_rect.top = 220
        text_rect.left = 400
    if text == "Who are you...?":
        text_rect.top = 290
        text_rect.left = 400
    if text == "What are you...?":
        text_rect.top = 360
        text_rect.left = 400
    if text == "Please...":
        text_rect.top = 430
        text_rect.left = 480
    if text == "TEACH ME YOUR WAYS.":
        text_rect.top = 500
        text_rect.left = 20
    if text == 'You decided to stay in here...':
        text_rect.top = 150
        text_rect.left = 250
    if text == "...Alone?":
        text_rect.left = 300
    if text == "Better Ending?":
        text_rect.left = 80

    # credits positioning
    if text == "Credits":
        text_rect.top = 20
        text_rect.left = 410
    if text == "Created by Elias Tagariello":
        text_rect.top = 100
        text_rect.left = 200
    if text == "Special thanks to:":
        text_rect.top = 170
        text_rect.left = 370
    if text == "Caleb Rice and Stone Beier for providing me with riddles and ideas.":
        text_rect.top = 340
        text_rect.left = 10
    if text == "Gil Salu for giving the best python class ever.":
        text_rect.top = 410
        text_rect.left = 10
    if text == "My girlfriend for giving me enough confidence to complete this.":
        text_rect.top = 270
        text_rect.left = 10
    if text == "Thanks for playing!":
        text_rect.top = 550
        text_rect.left = 70

    # what makes the text go slow
    char_index = 0
    next_char_time = pygame.time.get_ticks() + delay * 1000

    while char_index <= len(text):
        current_text = text[:char_index]
        text_surface = font.render(current_text, True, font_color)
        text_rect.size = text_surface.get_size()
        var.screen.blit(text_surface, text_rect)

        pygame.display.flip()

        if pygame.time.get_ticks() > next_char_time:
            char_index += 1
            next_char_time = pygame.time.get_ticks() + delay * 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        var.clock.tick(var.FPS)