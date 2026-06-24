class Filter:

    @staticmethod
    def expensive(items):

        return [
            item
            for item in items
            if item.price >= 10
        ]
    