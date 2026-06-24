from types import SimpleNamespace

from services.ranking import Ranking


def test_ranking():

    builds = [

        SimpleNamespace(score=50),

        SimpleNamespace(score=90),

        SimpleNamespace(score=70),

    ]

    result = Ranking.sort(builds)

    assert result[0].score == 90
    