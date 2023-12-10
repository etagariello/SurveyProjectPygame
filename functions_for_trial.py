import slow_print as slow
import input_box as inp
import sys
import loading_screen as load
import variables as var
import random


def setup_screen():
    # START SCREEN
    slow.SLOW_PRINT("- Welcome -", font_color=var.FONT_WHITE)
    slow.SLOW_PRINT("- Start -", font_color=var.FONT_WHITE, font_size=55)
    slow.SLOW_PRINT("- Quit -", font_color=var.FONT_WHITE, font_size=55)
    slow.SLOW_PRINT("(type your command)", font_color=var.FONT_WHITE, font_size=55)

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
    slow.SLOW_PRINT("Oh... my system can't recognize that name...")
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


    # if they say that they don't know enough about them, continue survey
    if knowing.lower() in var.no_knowledge_options:
        var.screen.fill(var.LIGHTERER_GREY)
        slow.SLOW_PRINT("Oh how disappointing.")

        # darken screen for drama
        load.LOADING(var.LIGHTERER_GREY, var.LIGHTER_GREY, var.LIGHT_GREY, var.GREY, var.BLACK, 0.1)
        slow.SLOW_PRINT("DO BETTER", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=200)
        var.screen.fill(var.BLACK)
        slow.SLOW_PRINT("LET'S BEGIN :)", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=220)
        return

        # if they do, question them if they consider them friends
    elif knowing.lower() in var.knowledge_options:
        return enough_to_call_them_a_friend()


    while knowing.lower() not in var.no_knowledge_options and knowing.lower() not in var.knowledge_options:
        slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=var.FONT_SIZE_INVALIDS)
        knowing = inp.INPUT()

        # if they say that they don't know enough about them, continue survey
        if knowing.lower() in var.no_knowledge_options:
            var.screen.fill(var.LIGHTERER_GREY)
            slow.SLOW_PRINT("Oh how disappointing.")

            # darken screen for drama
            load.LOADING(var.LIGHTERER_GREY, var.LIGHTER_GREY, var.LIGHT_GREY, var.GREY, var.BLACK, 0.1)
            slow.SLOW_PRINT("DO BETTER", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=200)
            var.screen.fill(var.BLACK)
            slow.SLOW_PRINT("LET'S BEGIN", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=250)
            return

        # if they do, question them if they consider them friends
        elif knowing.lower() in var.knowledge_options:
            return enough_to_call_them_a_friend()

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
        return

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
        return

        # if they say anything else, make them try again
    while friend.lower() != ">yes" and friend.lower() != ">no":
        var.screen.fill(var.BLACK)
        slow.SLOW_PRINT("YES OR NO", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=250)
        friend = inp.INPUT()
        var.screen.fill(var.BLACK)

        # if they say yes, continue the survey
        if friend.lower() == ">yes":
            slow.SLOW_PRINT("GOOD", delay=var.DELAY_FOR_WARNINGS, font_size=250,
                            font_color=var.FONT_COLOR_FOR_WARNINGS)
            var.screen.fill(var.BLACK)
            slow.SLOW_PRINT("LET'S BEGIN :)", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                            font_size=220)
            return

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
            return

def first_try_question1(name):
    load.LOADING()
    slow.SLOW_PRINT(f"Let's start simple, alright {name}?")
    slow.SLOW_PRINT('What is "9 + 10"?')
    slow.SLOW_PRINT("(btw, for each question, the answers are only one word or number long; no need for spaces)",
                    font_size=35)

    response = inp.INPUT()
    if response.lower() in var.valid_answers:
        var.screen.fill(var.LIGHTERER_GREY)
        slow.SLOW_PRINT("Oh... Correct ig")
        correct = True
        return correct


    elif response.lower() == ">19" or response.lower() == ">21":
        load.LOADING(var.LIGHTERER_GREY, var.LIGHTER_GREY, var.LIGHT_GREY, var.GREY, var.BLACK, 0.1)
        slow.SLOW_PRINT("You really thought it was going to be that easy, huh?",
                        font_color=var.FONT_COLOR_FOR_WARNINGS, font_size=65)
        slow.SLOW_PRINT(f"I am truly disappointed in you {name}.", delay=var.DELAY_FOR_WARNINGS,
                        font_color=var.FONT_COLOR_FOR_WARNINGS)

        slow.SLOW_PRINT("You know what? I won't give you a another chance...",
                        font_color=var.FONT_COLOR_FOR_WARNINGS)
        slow.SLOW_PRINT("I NEVER WILL", font_color=var.FONT_COLOR_FOR_WARNINGS, font_size=200,
                        delay=var.DELAY_FOR_WARNINGS)

        var.screen.fill(var.BLACK)
        correct = False
        return correct

    while response.lower() != ">19" and response.lower() != ">21" and response.lower() not in var.valid_answers:
        slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=var.FONT_SIZE_INVALIDS)
        response = inp.INPUT()

        if response.lower() in var.valid_answers:
            var.screen.fill(var.LIGHTERER_GREY)
            slow.SLOW_PRINT("Oh... Correct ig")
            correct = True
            return correct

        elif response.lower() == ">19" or response.lower() == ">21":
            load.LOADING(var.LIGHTERER_GREY, var.LIGHTER_GREY, var.LIGHT_GREY, var.GREY, var.BLACK, 0.1)
            slow.SLOW_PRINT("You really thought it was going to be that easy, huh?",
                            font_color=var.FONT_COLOR_FOR_WARNINGS, font_size=65)
            slow.SLOW_PRINT(f"I am truly disappointed in you {name}.", font_color=var.DELAY_FOR_WARNINGS)

            slow.SLOW_PRINT("You know what? I won't give you a another chance...",
                            font_color=var.FONT_COLOR_FOR_WARNINGS)
            slow.SLOW_PRINT("I NEVER WILL", font_color=var.FONT_COLOR_FOR_WARNINGS, font_size=200,
                            delay=var.DELAY_FOR_WARNINGS)

            var.screen.fill(var.BLACK)
            correct = False
            return correct

# lets the player know that they failed and they can try again if they want
def restart_message():
    slow.SLOW_PRINT("How truly unfortunate...", font_color=var.FONT_COLOR_FOR_WARNINGS)
    slow.SLOW_PRINT("You got that one wrong.", font_color=var.FONT_COLOR_FOR_WARNINGS)
    slow.SLOW_PRINT("But don't worry!", font_color=var.FONT_COLOR_FOR_WARNINGS)
    slow.SLOW_PRINT("You definitely don't have to restart...", font_color=var.FONT_COLOR_FOR_WARNINGS)
    slow.SLOW_PRINT("And the questions are definitely not randomized...", font_color=var.FONT_COLOR_FOR_WARNINGS)

    var.screen.fill(var.BLACK)
    slow.SLOW_PRINT("Try Again?", delay=var.DELAY_FOR_WARNINGS, font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=250)
    response = inp.INPUT()

    if response.lower() == ">yes":
        return random_questions()

    elif response.lower() == ">no":
        sys.exit()

    while response.lower() != ">yes" and response.lower() != ">no":
        slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.FONT_COLOR_FOR_WARNINGS,
                        font_size=var.FONT_SIZE_INVALIDS)
        response = inp.INPUT()

        if response.lower() == ">yes":
            return random_questions()

        elif response.lower() == ">no":
            sys.exit()

# using random module so that it picks a random question and removes it after so that it doesn't repeat
def random_questions():
    # coffin question
    def rand_question_1():
        slow.SLOW_PRINT("You buy it when you don’t need it,", font_color=var.FONT_WHITE )
        slow.SLOW_PRINT("you need it when you can’t buy it,", font_color=var.FONT_WHITE)
        slow.SLOW_PRINT("you use it when you don’t know it.", font_color=var.FONT_WHITE)

        slow.SLOW_PRINT("What is it?", font_color=var.FONT_WHITE)
        response = inp.INPUT()

        correct_response = [">a coffin", ">coffin"]

        if response.lower() in correct_response:
            slow.SLOW_PRINT("Correct...", font_color=var.FONT_WHITE)
            return

        elif response.lower() not in correct_response:
            return restart_message()

    # nothing question
    def rand_question_2():
        slow.SLOW_PRINT("The rich need it,", font_color=var.FONT_WHITE)
        slow.SLOW_PRINT("the poor have it,", font_color=var.FONT_WHITE)
        slow.SLOW_PRINT("and if you breathe it you die.", font_color=var.FONT_WHITE)

        slow.SLOW_PRINT("What is it?", font_color=var.FONT_WHITE)
        response = inp.INPUT()

        correct_response = [">nothing"]

        if response.lower() in correct_response:
            slow.SLOW_PRINT("Correct...", font_color=var.FONT_WHITE)
            return

        elif response.lower() not in correct_response:
            return restart_message()

    #mortality question
    def rand_question_3():
        slow.SLOW_PRINT("I am the inevitable shadow", font_color=var.FONT_WHITE)
        slow.SLOW_PRINT("cast by the passage of time.", font_color=var.FONT_WHITE)

        slow.SLOW_PRINT("What am I?", font_color=var.FONT_WHITE)
        response = inp.INPUT()

        correct_response = [">mortality"]

        if response.lower() in correct_response:
            slow.SLOW_PRINT("Correct...", font_color=var.FONT_WHITE)
            return

        elif response.lower() not in correct_response:
            return restart_message()

    # oblivion question
    def rand_question_4():
        slow.SLOW_PRINT("What is the ultimate fate,", font_color=var.FONT_WHITE)
        slow.SLOW_PRINT("unseen yet known to all?", font_color=var.FONT_WHITE)

        response = inp.INPUT()

        correct_response = [">oblivion"]

        if response.lower() in correct_response:
            slow.SLOW_PRINT("Correct...", font_color=var.FONT_WHITE)
            return

        elif response.lower() not in correct_response:
            return restart_message()

        # Void question
    def rand_question_5():
        slow.SLOW_PRINT("I am the absence", font_color=var.FONT_WHITE)
        slow.SLOW_PRINT("that defines existence's end.", font_color=var.FONT_WHITE)

        slow.SLOW_PRINT("What am I?", font_color=var.FONT_WHITE)
        response = inp.INPUT()

        correct_response = [">void", ">the void"]

        if response.lower() in correct_response:
            slow.SLOW_PRINT("Correct...", font_color=var.FONT_WHITE)
            return

        elif response.lower() not in correct_response:
            return restart_message()


    random_questions_list = [rand_question_1(), rand_question_2(), rand_question_3(), rand_question_4(),
                             rand_question_5()]
    num_queue = 0
    # this pulls a random question from the list and also removes it so it can't repeat
    for i in range(5):
        num_queue += 1
        var.screen.fill(var.BLACK)
        slow.SLOW_PRINT(f"Question {num_queue}")
        next_question = random.choice(random_questions_list)
        random_questions_list.remove(next_question)
