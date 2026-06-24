import json


class TradeParser:

    @staticmethod
    def load(path):

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)