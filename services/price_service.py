class PriceService:

    @staticmethod
    def average(items):

        if not items:
            return 0

        total = sum(item.price for item in items)

        return round(total / len(items), 2)