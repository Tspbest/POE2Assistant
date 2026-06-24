from models.build import Build
from services.comparator import Comparator


def test_comparator():

    build1 = Build(
        "BuildA",
        100,
        "Monk",
        90,
        80
    )

    build2 = Build(
        "BuildB",
        100,
        "Monk",
        95,
        75
    )

    result = Comparator.better(
        build1,
        build2
    )

    assert result.name == "BuildB"