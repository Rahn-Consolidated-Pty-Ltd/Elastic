from elastic.main import add   # import from the package

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
