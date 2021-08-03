import os
import sys
import json
import gettext


def load_json(path: str) -> dict:
    if not os.path.isfile(path):
        sys.exit(f"'{path}' not found! Please add it and try again.")
    else:
        with open(path) as file:
            return json.load(file)


def load_locale(domain: str, path: str, languages: list) -> str:
    language = gettext.translation(domain, localedir=path, languages=languages)
    language.install()
    return language.gettext


config = load_json("config.json")
_ = load_locale(
    config["locales_domain"], config["locales_path"], config["locales_languages"]
)
