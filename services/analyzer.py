class Analyzer:

    @staticmethod
    def score(build):

        score = (
            build.damage * 0.6 +
            build.defense * 0.4
        )

        return int(score)