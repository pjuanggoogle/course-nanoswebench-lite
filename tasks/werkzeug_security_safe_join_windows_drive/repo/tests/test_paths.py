from werkzeug_sec.paths import safe_join

def test_valid_and_parent_traversal():
    assert safe_join("/var/www", "static", "app.js") == "/var/www/static/app.js"
    assert safe_join("/var/www", "../etc/passwd") is None

def test_rejects_drive_and_backslash():
    assert safe_join("/var/www", "C:secret.txt") is None
    assert safe_join("/var/www", "sub\\file.txt") is None
