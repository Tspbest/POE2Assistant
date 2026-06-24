from models.character import Character
def show_title():
    print()
    print("=" * 50)
    print("          POE2 Assistant")
    print("=" * 50)


def create_character():
    name = input("Character Name : ")
    level = input("Level : ")
    job = input("Class : ")

    player = Character(name, level, job)

    player.show()
    player.save()

    name = input("mamaznag : ")
    level = input("100 : ")
    job = input("Monk : ")

    print()
    print("Character Created!")
    print("Name :", name)
    print("Level :", level)
    print("Class :", job)


while True:

    show_title()

    print("1. Create Character")
    print("2. Load Character")
    print("3. About")
    print("4. Exit")

    choice = input("Select : ")

    if choice == "1":
        create_character()

    elif choice == "2":

        player = Character.load()

        if player:
            player.show()

    elif choice == "3":
        print()
        print("About POE2 Assistant")
        print("Version 0.0.1")
        print("Created by : MaMaZang")

    elif choice == "4":
        print("Good Bye")
        break

    else:
        print("Invalid Menu")