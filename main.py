import pygame
import functions_for_exam as func

pygame.init()

running = True
while running:
    # when user presses the X, the game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # starts setup
    func.setup_screen()

    # puts result of gender function in name for future use
    name = func.gender_name_finding()

    func.how_much_do_you_know_about_them(name)

    func.first_try_question1(name)

pygame.quit()
