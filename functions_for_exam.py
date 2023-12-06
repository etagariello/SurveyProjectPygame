import slow_print as slow
import input_box as inp
import sys
import loading_screen as load
import variables as var


def setup_screen():
    # START SCREEN
    slow.SLOW_PRINT("- Welcome -", font_color=var.FONT_WHITE)
    slow.SLOW_PRINT("- Start -", font_color=var.FONT_WHITE, font_size=55)
    slow.SLOW_PRINT("- Quit -", font_color=var.FONT_WHITE, font_size=55)

    command = inp.INPUT()

    # quit if player types quit
    if command.lower() == ">quit":
        sys.exit()

    # if they type start, load
    elif command.lower() == ">start":
        load.LOADING()
        name_interaction()

    # if they type the wrong thing, say invalid and they can try again
    while command.lower() != ">quit" and command.lower() != ">start":
        slow.SLOW_PRINT("Invalid Command. Try Again.", font_size=var.FONT_SIZE_INVALIDS, font_color=var.FONT_WHITE)
        command = inp.INPUT()

        # quit if player types quit
        if command.lower() == ">quit":
            sys.exit()

        # if they type start, turn screen black
        elif command.lower() == ">start":
            load.LOADING()
            name_interaction()


def name_interaction():
    # ask for name
    slow.SLOW_PRINT("Hello there! What's your name?")

    # they put their name once but shows error on purpose
    inp.INPUT()
    slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.FONT_COLOR_FOR_WARNINGS,
                    font_size=var.FONT_SIZE_INVALIDS)

    # then again
    inp.INPUT()
    slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.FONT_COLOR_FOR_WARNINGS,
                    font_size=var.FONT_SIZE_INVALIDS)

    # clear screen
    var.screen.fill(var.LIGHTERER_GREY)

    # tell them why it's not working
    slow.SLOW_PRINT("Oh... my test can't recognize that name...")
    slow.SLOW_PRINT("Let me check it out.")
    slow.SLOW_PRINT(".....", delay=1, font_size=100)

    var.screen.fill(var.LIGHTERER_GREY)

    # insult their name
    slow.SLOW_PRINT("Oooooooh, your name is just ugly.")
    slow.SLOW_PRINT("Weeell", delay=0.2)


def gender_name_finding():
    # ask for gender
    slow.SLOW_PRINT("Then what's your gender?")
    slow.SLOW_PRINT("So I can name you.")

    # this will change the name depending on the answer
    gender = inp.INPUT()
    if gender.lower() == ">male":
        name = "Bob"
    elif gender.lower() == ">female":
        name = "Barbara"
    while gender.lower() != ">male" and gender.lower() != ">female":
        slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=var.FONT_SIZE_INVALIDS)
        gender = inp.INPUT()
        if gender.lower() == ">male":
            name = "Bob"
        elif gender.lower() == ">female":
            name = "Barbara"

    var.screen.fill(var.LIGHTERER_GREY)

    slow.SLOW_PRINT(f"Ah I see... your name is now {name}. Cherish it.")
    return name


def how_much_do_you_know_about_them(name):
    slow.SLOW_PRINT(f"Well {name}")
    slow.SLOW_PRINT("How much do you know about who sent you this?")
    knowing = inp.INPUT()

    # clear screen here
    var.screen.fill(var.LIGHTERER_GREY)

    # if they say that they don't know enough about them, continue survey
    if knowing.lower() in var.no_knowledge_options:
        slow.SLOW_PRINT("Oh how disappointing.")

        # darken screen for drama
        load.LOADING(var.LIGHTERER_GREY, var.LIGHTER_GREY, var.LIGHT_GREY, var.GREY, var.BLACK, 0.1)
        slow.SLOW_PRINT("DO BETTER", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=200)
        var.screen.fill(var.BLACK)
        slow.SLOW_PRINT("LET'S BEGIN :)", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=220)
        sys.exit()

    # if they do, question them if they consider them friends
    elif knowing.lower() in var.knowledge_options:
        return

    while knowing.lower() not in var.no_knowledge_options and knowing.lower() not in var.knowledge_options:
        slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=var.FONT_SIZE_INVALIDS)
        knowing = inp.INPUT()

        # if they say that they don't know enough about them, continue survey
        if knowing.lower() in var.no_knowledge_options:
            slow.SLOW_PRINT("Oh how disappointing.")

            # darken screen for drama
            load.LOADING(var.LIGHTERER_GREY, var.LIGHTER_GREY, var.LIGHT_GREY, var.GREY, var.BLACK, 0.1)
            slow.SLOW_PRINT("DO BETTER", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=200)
            var.screen.fill(var.BLACK)
            slow.SLOW_PRINT("LET'S BEGIN", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=250)
            sys.exit()

        # if they do, question them if they consider them friends
        elif knowing.lower() in var.knowledge_options:
            return

def enough_to_call_them_a_friend():
    # darken screen for drama
    load.LOADING(var.LIGHTERER_GREY, var.LIGHTER_GREY, var.LIGHT_GREY, var.GREY, var.BLACK, 0.1)
    slow.SLOW_PRINT("ENOUGH TO CALL THEM A FRIEND?", delay=var.DELAY_FOR_WARNINGS,
                    font_color=var.FONT_COLOR_FOR_WARNINGS, font_size=95)
    friend = inp.INPUT()
    var.screen.fill(var.BLACK)

    # if they say yes, continue the survey
    if friend.lower() == ">yes":
        slow.SLOW_PRINT("GOOD", delay=var.DELAY_FOR_WARNINGS, font_size=250, font_color=var.FONT_COLOR_FOR_WARNINGS)
        var.screen.fill(var.BLACK)
        slow.SLOW_PRINT("LET'S BEGIN :)", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=220)
        sys.exit()

    # if they say no, quit
    elif friend.lower() == ">no":
        slow.SLOW_PRINT("I SEE WHY THEY SENT THIS TO YOU...", delay=var.DELAY_FOR_WARNINGS,
                        font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=90)
        var.screen.fill(var.BLACK)
        slow.SLOW_PRINT("HAHAHAHA", delay=0.03, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=270)
        var.screen.fill(var.BLACK)
        slow.SLOW_PRINT("LET'S BEGIN :)", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=220)
        sys.exit()

    # if they say anything else, make them try again
    while friend.lower() != ">yes" and friend.lower() != ">no":
        var.screen.fill(var.BLACK)
        slow.SLOW_PRINT("YES OR NO", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS, font_size=250)
        friend = inp.INPUT()
        var.screen.fill(var.BLACK)

        # if they say yes, continue the survey
        if friend.lower() == ">yes":
            slow.SLOW_PRINT("GOOD", delay=var.DELAY_FOR_WARNINGS, font_size=250, font_color=var.FONT_COLOR_FOR_WARNINGS)
            var.screen.fill(var.BLACK)
            slow.SLOW_PRINT("LET'S BEGIN :)", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=220)
            sys.exit()

        # if they say no
        elif friend == ">no":
            slow.SLOW_PRINT("I SEE WHY THEY SENT THIS TO YOU...", delay=var.DELAY_FOR_WARNINGS,
                            font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=90)
            var.screen.fill(var.BLACK)
            slow.SLOW_PRINT("HAHAHAHA", delay=0.03, font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=250)
            var.screen.fill(var.BLACK)
            slow.SLOW_PRINT("LET'S BEGIN :)", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=220)
            sys.exit()
