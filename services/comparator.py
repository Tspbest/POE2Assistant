class Comparator:

    @staticmethod
    def better(build1, build2):

        if build1.damage >= build2.damage:
            return build1

        return build2