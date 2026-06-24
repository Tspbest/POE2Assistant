import os

from services.exporter import Exporter


def test_exporter():

    data = {

        "name": "MamaZang",

        "level": 100

    }

    filename = "output.json"

    assert Exporter.export(
        data,
        filename
    )

    assert os.path.exists(
        filename
    )

    os.remove(filename)