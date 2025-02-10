from remove_url_anchor import remove_url_anchor


def test_remove_anchor_from_url():
    assert remove_url_anchor("www.example.com#about") == "www.example.com"
    assert remove_url_anchor("www.codewars.com#section1") == "www.codewars.com"


def test_url_without_anchor():
    assert remove_url_anchor("www.example.com") == "www.example.com"
    assert remove_url_anchor("https://openai.com") == "https://openai.com"


def test_empty_url():
    assert remove_url_anchor("") == ""
