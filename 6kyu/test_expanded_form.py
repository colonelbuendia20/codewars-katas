from expanded_form import expanded_form


def test_single_digit():
    assert expanded_form(7) == "7"


def test_two_digits():
    assert expanded_form(42) == "40 + 2"


def test_three_digits():
    assert expanded_form(703) == "700 + 3"


def test_large_number():
    assert expanded_form(12034) == "10000 + 2000 + 30 + 4"


def test_with_zeros():
    assert expanded_form(5300) == "5000 + 300"
