import os

from models.build import Build
from services.csv_exporter import CSVExporter


def test_csv_exporter():

    builds = [

        Build(
            "MamaZang",
            100,
            "Monk",
            3500,
            1200,
            95,
            90
        ),

        Build(
            "Storm",
            98,
            "Sorceress",
            2800,
            2500,
            99,
            70
        )

    ]

    filename = "output/builds.csv"

    assert CSVExporter.export(
        builds,
        filename
    )

    assert os.path.exists(filename)

    os.remove(filename)