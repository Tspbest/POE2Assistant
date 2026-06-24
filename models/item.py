class Item:

    def __init__(
        self,
        name,
        item_type,
        value,
        defense=0,
        price=0
    ):
        self.name = name
        self.item_type = item_type
        self.value = value
        self.defense = defense

        # ถ้าเรียกแค่ 3 ตัว เช่น Item("A","Ring",5)
        # ให้ถือว่า value คือราคา
        if defense == 0 and price == 0:
            self.price = value
        else:
            self.price = price

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.item_type,
            "price": self.price,
            "value": self.value,
            "defense": self.defense,
        }