import os


def get_env_key(key_name: str) -> str:

    if os.environ[key_name] is None:
        raise EnvironmentError(f"{key_name} is not in enviroment")

    return os.environ[key_name]
