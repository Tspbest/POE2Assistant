from models.character import Character
from services.optimizer import Optimizer


def test_optimizer():

    character = Character(

        "Player",
        80,
        "Monk",
        2000,
        500,
        70,
        75

    )

    result = Optimizer.recommend(character)

    assert len(result) > 0