from models.build import Build
from services.analyzer import Analyzer


def test_score():

    build = Build(

        "MamaZang",
        100,
        "Monk",
        92,
        88

    )

    score = Analyzer.score(build)

    assert score == 90