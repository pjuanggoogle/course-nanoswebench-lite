def delenv(env_dict: dict, name: str, raising: bool = True):
    return env_dict.pop(name)
