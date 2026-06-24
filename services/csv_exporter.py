import csv


class CSVExporter:

    @staticmethod
    def export(builds, filename):

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "name",
                "level",
                "job",
                "life",
                "mana",
                "damage",
                "defense"
            ])

            for build in builds:

                writer.writerow([
                    build.name,
                    build.level,
                    build.job,
                    build.life,
                    build.mana,
                    build.damage,
                    build.defense
                ])

        return True