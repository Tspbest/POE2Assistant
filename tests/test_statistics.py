from services.statistics import Statistics


def test_statistics():

    values = [10, 20, 30]

    assert Statistics.average(values) == 20
    assert Statistics.maximum(values) == 30
    assert Statistics.minimum(values) == 10
    