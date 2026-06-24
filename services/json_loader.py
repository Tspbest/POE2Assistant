import json


class JSONLoader:

    @staticmethod
    def load(filename):

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)