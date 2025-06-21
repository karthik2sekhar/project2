from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_hello():
    assert hello("karthik") == "Hello, karthik"


