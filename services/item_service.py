from collector.poe2_trade import POE2TradeClient


class ItemService:

    def __init__(self):

        self.client = POE2TradeClient()

    def leagues(self):

        return self.client.fetch("leagues")