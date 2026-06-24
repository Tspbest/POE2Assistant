class Optimizer:

    @staticmethod
    def recommend(character):

        result = []

        if character.damage < 90:
            result.append("Increase Damage")

        if character.defense < 90:
            result.append("Increase Defense")

        if character.life < 3000:
            result.append("Increase Life")

        if character.mana < 1000:
            result.append("Increase Mana")

        return result
