from flask_config.env import load_prefixed_env

def test_string_env_values():
    assert load_prefixed_env({"FLASK_HOST": "localhost", "OTHER": "1"}) == {"HOST": "localhost"}

def test_json_typed_env_values():
    env = {"FLASK_DEBUG": "true", "FLASK_PORT": "8080", "FLASK_NAME": "myapp"}
    assert load_prefixed_env(env) == {"DEBUG": True, "PORT": 8080, "NAME": "myapp"}
