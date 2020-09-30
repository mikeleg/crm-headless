import os

def get_env_key(key_name: str) -> str:
    try:
        return os.environ.get(key_name)
    except KeyError:
        raise EnvironmentError(f"{key_name} is not in enviroment")


    
