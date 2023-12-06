import pygame
import functions_for_exam as func

pygame.init()

running = True
while running:
    # when user presses the X, the game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    func.setup_screen()
    print("complete")
    name = func.gender_name_finding()
    print("complete")
    func.how_much_do_you_know_about_them(name)
    print("complete")
    func.enough_to_call_them_a_friend()
    print("complete")

pygame.quit()
