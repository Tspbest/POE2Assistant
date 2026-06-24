import json

class Config:

    @staticmethod
    def load():

        with open(
            "config/settings.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)