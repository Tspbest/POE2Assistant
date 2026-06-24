from models.character import Character


def test_character():

    character = Character(

        "MamaZang",
        100,
        "Monk",
        3500,
        1200,
        95,
        90

    )

    assert character.name == "MamaZang"

    assert character.level == 100