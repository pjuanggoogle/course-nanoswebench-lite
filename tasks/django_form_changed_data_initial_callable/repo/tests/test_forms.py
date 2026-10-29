from django_forms.forms import Form

def test_static_initial_comparison():
    f = Form(data={"title": "Hello", "count": 5}, initial={"title": "Hello", "count": 3})
    assert f.changed_data == ["count"]

def test_callable_initial_unchanged():
    f = Form(
        data={"status": "draft", "author": "alice"},
        initial={"status": lambda: "draft", "author": lambda: "bob"},
    )
    assert f.changed_data == ["author"]
