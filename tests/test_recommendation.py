from services.recommendation import Recommendation


def test_recommendation():

    assert Recommendation.recommend(950) == "S Tier Build"
    assert Recommendation.recommend(850) == "A Tier Build"
    assert Recommendation.recommend(750) == "B Tier Build"
    assert Recommendation.recommend(600) == "Need Improvement"