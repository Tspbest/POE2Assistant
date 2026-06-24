class Recommender:

    @staticmethod
    def recommend(score):

        if score >= 900:
            return "S Tier"

        if score >= 800:
            return "A Tier"

        if score >= 700:
            return "B Tier"

        return "Need Improvement"