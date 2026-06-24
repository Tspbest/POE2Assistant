from services.logger import Logger


def test_logger():

    Logger.info("Hello")

    Logger.error("Failed")

    assert True