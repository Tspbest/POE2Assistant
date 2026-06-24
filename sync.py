from collector.poe2_trade import POE2TradeClient
from database.sync_database import SyncDatabase

client = POE2TradeClient()

items = client.fetch("items")

SyncDatabase.save_items(items)

print("Items synced")