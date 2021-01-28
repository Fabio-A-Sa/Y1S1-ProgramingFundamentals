# Created on January, 2021
# @author: Fábio Araújo de Sá

def intro():

    # Introduction
    print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.")

    # Possibilities
    print("A. Grab a nearby rock and throw it at the orc")
    print("B. Lie down and wait to be mauled")
    print("C. Run")

    answer_intro = str(input("Your choice: ")).strip()
    game_over = "Welp, that was quick. You died!"

    if answer_intro.upper() == "A":
        rock() 
    if answer_intro.upper() == "B":
        print(game_over)
    if answer_intro.upper() == "C":
        run()

def rock():

    # Introduction
    print("The orc is stunned, but regains control. He begins running towards you again.")

    # Possibilities
    print("A. Run")
    print("B. Throw another rock")
    print("C. Run towards a nearby cave")

    answer_rock = str(input("Your choice: ")).strip()
    game_over = "The rock flew well over the orcs head. You missed. You died!"

    if answer_rock.upper() == "A":
        run() 
    if answer_rock.upper() == "B":
        print(game_over)
    if answer_rock.upper() == "C":
        cave()

def run():

    # Introduction
    print("You run as quickly as possible.")

    # Possibilities
    print("A. Hide behind boulder")
    print("B. Trapped, so you fight")
    print("C. Run towards an abandoned town")

    run_answer = str(input("Your choice: ")).strip()

    if run_answer.upper() == "A":
        print("You're easily spotted. You died!")
    if run_answer.upper() == "B":
        print("You're no match for an orc. You died!")
    if run_answer.upper() == "C":
        town()

def cave():

    # Introduction
    print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")
    sword = str(input("Your choice: ")).strip()

    print("What do you do next?")
    # Possibilities
    print("A. Hide in silence")
    print("B. Fight")
    print("C. Run")

    cave_answer = str(input("Your choice: ")).strip()
    game_over1 = "I think orcs can see very well in the dark, right? You died!"
    game_over2 = "You're defenseless. You died!"

    if cave_answer.upper() == "A":
        print(game_over1)
    if cave_answer.upper() == "B":
        if sword.upper() == "Y":
            print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
        if sword.upper() == "N":
            print(game_over2)
    if cave_answer.upper() == "C":
        print("The orc turns around and sees you running.")
        run()

def town():

    # Introduction
    print("You notice a purple flower near your foot. Do you pick it up? Y/N")

    town_answer = str(input("Your choice: ")).strip()

    if town_answer.upper() == "Y":
        print("You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!")
    if town_answer.upper() == "N":
        print("Maybe you should have picked up the flower. You died!")

intro()
