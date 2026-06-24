class Scorer:

    @staticmethod
    def calculate(character):

        score = (

            character.damage * 0.4 +

            character.defense * 0.3 +

            character.life * 0.2 +

            character.mana * 0.1

        )

        return round(score, 2)