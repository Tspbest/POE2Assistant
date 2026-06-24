import json

from models.build import Build


class Importer:

    @staticmethod
    def load(filename):

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return Build(
            data["name"],
            data["level"],
            data["job"],
            data["life"],
            data["mana"],
            data["damage"],
            data["defense"]
        )