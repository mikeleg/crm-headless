import os


def get_env_key(key_name: str):
    try:
        return os.environ.get(key_name)
    except KeyError:
        print(f"{key_name} is not in enviroment")
