from collector.trade_client import TradeClient


def test_trade_client():

    client = TradeClient()

    assert client.BASE_URL.startswith("https")