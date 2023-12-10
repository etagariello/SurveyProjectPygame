import pygame
import functions_for_trial as func

pygame.init()

running = True
while running:
    # when user presses the X, the game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # start
    func.setup_screen()

    name = func.gender_name_finding()

    func.how_much_do_you_know_about_them(name)

    correct = func.first_try_question1(name)

    if correct == False:
        func.random_questions()



pygame.quit()
