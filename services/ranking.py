class Ranking:

    @staticmethod
    def sort(builds):

        return sorted(
            builds,
            key=lambda build: build.score,
            reverse=True
        )
    