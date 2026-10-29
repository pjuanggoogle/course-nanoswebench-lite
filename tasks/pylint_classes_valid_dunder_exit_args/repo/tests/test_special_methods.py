from pylint_classes.special_methods import check_exit_signature

def test_standard_four_args():
    assert check_exit_signature(["self", "exc_type", "exc_val", "exc_tb"]) is True
    assert check_exit_signature(["self", "a"]) is False

def test_varargs_exit_signature():
    assert check_exit_signature(["self", "*args"]) is True
    assert check_exit_signature(["self", "exc_type", "*rest"]) is True
