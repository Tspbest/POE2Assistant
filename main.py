from models.character import Character
from services.exporter import Exporter
from services.scorer import Scorer
from services.recommendation import Recommendation

character = Character(
    "MamaZang",
    100,
    "Monk",
    3500,
    1200,
    95,
    90
)

print(character.to_dict())

score = Scorer.calculate(character)

print("Build Score")
print(score)

print("Recommendation")
print(Recommendation.recommend(score))

from models.build import Build
from services.analyzer import Analyzer
from services.recommender import Recommender

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
    "output/build.json"
)

print("Build exported")

from services.importer import Importer

loaded = Importer.load(
    "output/build.json"
)

print()
print("Imported Build")
print(loaded.to_dict())

from services.csv_exporter import CSVExporter

builds = [

    build,

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

CSVExporter.export(
    builds,
    "output/builds.csv"
)

print("CSV Export Complete")