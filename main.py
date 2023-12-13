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

    x, y = 0, 0
    pixel_color = var.screen.get_at((x, y))

    # if the screen is black, escape ending
    if pixel_color == (0, 0, 0, 255):
        func.escape_ending()

    # if the screen is light grey, master ending
    elif pixel_color == (200, 200, 200, 255):
        func.master_ending()

pygame.quit()
