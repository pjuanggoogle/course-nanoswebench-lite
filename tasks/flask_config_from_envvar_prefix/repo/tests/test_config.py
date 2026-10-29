from flask_config.config import load_prefixed_env

def test_json_typed_values():
    env = {"FLASK_DEBUG": "true", "FLASK_PORT": "8080", "OTHER_VAR": "1"}
    assert load_prefixed_env(env) == {"DEBUG": True, "PORT": 8080}

def test_unquoted_string_and_repeated_prefix_in_key():
    env = {"FLASK_MY_FLASK_HOST": "localhost", "FLASK_COUNTS": "[1, 2]"}
    assert load_prefixed_env(env) == {"MY_FLASK_HOST": "localhost", "COUNTS": [1, 2]}
