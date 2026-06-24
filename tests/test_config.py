from config.config import Config


def test_load_config():

    settings = Config.load()

    assert settings["project_name"] == "POE2 Assistant"