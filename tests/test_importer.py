from services.exporter import Exporter
from services.importer import Importer
from models.build import Build


def test_importer():

    build = Build(
        "MamaZang",
        100,
        "Monk",
        3500,
        1200,
        95,
        90
    )

    Exporter.export(
        build,
        "output/test_build.json"
    )

    result = Importer.load(
        "output/test_build.json"
    )

    assert result.name == "MamaZang"
    assert result.level == 100
    assert result.damage == 95
