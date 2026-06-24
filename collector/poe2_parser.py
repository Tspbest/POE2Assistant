class POE2Parser:

    @staticmethod
    def parse(data):

        return {
            "name": data.get("name"),
            "level": data.get("level"),
            "job": data.get("job"),
            "life": data.get("life"),
            "mana": data.get("mana"),
            "damage": data.get("damage"),
            "defense": data.get("defense")
        }