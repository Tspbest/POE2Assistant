from fastapi import FastAPI
from services.item_query import ItemQuery

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "POE2 Assistant",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/build")
def build():
    return {
        "message": "Build API"
    }


@app.get("/league")
def league():
    return {
        "message": "League API"
    }


@app.get("/items")
def items():
    data = ItemQuery.all()

    return {
        "count": len(data),
        "items": data
    }


@app.get("/items/search")
def search_items(name: str):

    data = ItemQuery.search(name)

    return {
        "count": len(data),
        "items": data
    }


@app.get("/items/{item_id}")
def get_item(item_id: int):

    return ItemQuery.get(item_id)


@app.get("/items")
def items(limit: int = 20, offset: int = 0):

    data = ItemQuery.all()

    return {
        "count": len(data),
        "limit": limit,
        "offset": offset,
        "items": data[offset:offset + limit]
    }


@app.get("/leagues")
def leagues():
    import sqlite3

    conn = sqlite3.connect("poe2.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT league_id, name, realm
        FROM leagues
    """)

    rows = cursor.fetchall()
    conn.close()

    return {
        "count": len(rows),
        "leagues": rows
    }