from models.character import Character
from services.scorer import Scorer


def test_score():

    character = Character(

        "MamaZang",
        100,
        "Monk",
        3500,
        1200,
        95,
        90

    )

    score = Scorer.calculate(character)

    assert score > 0