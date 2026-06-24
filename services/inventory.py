class Inventory:

    @staticmethod
    def total_price(items):

        return sum(item.price for item in items)

    @staticmethod
    def total_defense(items):

        return sum(item.defense for item in items)