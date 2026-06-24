import json


class Exporter:

    @staticmethod
    def export(build, filename):

        if hasattr(build, "to_dict"):
            data = build.to_dict()
        else:
            data = build

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True