class Build:

    def __init__(
        self,
        name,
        level,
        job,
        damage,
        defense,
        life=0,
        mana=0
    ):
        self.name = name
        self.level = level
        self.job = job
        self.damage = damage
        self.defense = defense
        self.life = life
        self.mana = mana

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "job": self.job,
            "damage": self.damage,
            "defense": self.defense,
            "life": self.life,
            "mana": self.mana,
        }