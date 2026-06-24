class Character:

    def __init__(
        self,
        name,
        level,
        job,
        life,
        mana,
        damage,
        defense
    ):

        self.name = name
        self.level = level
        self.job = job
        self.life = life
        self.mana = mana
        self.damage = damage
        self.defense = defense

    def to_dict(self):

        return {

            "name": self.name,
            "level": self.level,
            "job": self.job,
            "life": self.life,
            "mana": self.mana,
            "damage": self.damage,
            "defense": self.defense

        }