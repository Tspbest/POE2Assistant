from config.config import Config

settings = Config.load()

print(settings)

print(settings["project_name"])
print(settings["version"])