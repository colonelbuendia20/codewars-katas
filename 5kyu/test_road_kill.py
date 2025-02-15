from road_kill import road_kill


def test_basic_cases():
    assert road_kill("==========h===yyyyyy===eeee=n==a========") == "hyena"
    assert road_kill("=pe=nnnnnn===n=n=ng====u==iiii=iii==nn==n=") == "penguin"
    assert road_kill("=====r=rrr=rra=====eee======bb====b=======") == "bear"


def test_invalid_cases():
    assert road_kill("=====") == "??"
    assert road_kill("") == "??"
    assert road_kill(None) == "??"
    assert road_kill("===xyz===") == "??"


def test_reverse_cases():
    assert road_kill("==nn===iii=iii==u=g=n==n=n=ep===") == "penguin"
    assert road_kill("===rrr===a=a===a=e=eee=b=====") == "bear"


def test_giraffe_case():
    assert road_kill("====g===iii==rrr===aaa===fff==f====e===") == "giraffe"
    assert road_kill("====e===fff==f===aaa===rrr==iii===g===") == "giraffe"
    assert road_kill("===g==i==r==a==l==f==f==e===") == "??"
