from models.build import Build


def test_build_to_dict():

    build = Build(

        "MamaZang",
        100,
        "Monk",
        92,
        88

    )

    data = build.to_dict()

    assert data["name"] == "MamaZang"