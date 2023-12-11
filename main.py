import pygame
import functions_for_trial as func
import variables as var

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

    correct = func.first_try_questions(name)

    if correct == True:
        func.random_questions(background=var.LIGHTERER_GREY, font_color=var.FONT_BLACK)
    else:
        func.random_questions()


pygame.quit()
