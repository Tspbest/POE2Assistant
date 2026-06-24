import json

class Character:
    
    def __init__(self, name, level, job):

        self.name = name
        self.level = level
        self.job = job

    def show(self):

        print()
        print("Character Information")
        print("--------------------------")
        print("Name :", self.name)
        print("Level :", self.level)
        print("Class :", self.job)

    def save(self):

        data = {
            "Name": self.name,
            "Level": self.level,
            "Class": self.job
        }

        with open("database/character.json", "w") as file:

            json.dump(data, file, indent=4)

        print()
        print("Character Saved Successfully!")

    @staticmethod
    def load():

        try:

            with open("database/character.json", "r") as file:
                data = json.load(file)

            if "Name" not in data:
                print("No character data found.")
                return None

            player = Character(
            data["Name"],
            data["Level"],
            data["Class"]
        )

            return player

        except FileNotFoundError:
            print("character.json not found")
            return None
        