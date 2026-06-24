from services.recommender import Recommender


def test_recommender():

    assert Recommender.recommend(950) == "S Tier"
    assert Recommender.recommend(850) == "A Tier"
    assert Recommender.recommend(750) == "B Tier"
    assert Recommender.recommend(600) == "Need Improvement"