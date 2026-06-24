class Recommendation:

    @staticmethod
    def recommend(score):

        if score >= 900:
            return "S Tier Build"

        if score >= 800:
            return "A Tier Build"

        if score >= 700:
            return "B Tier Build"

        return "Need Improvement"