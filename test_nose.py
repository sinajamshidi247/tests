import one


def test_add():
    assert one.add(3,4) == 7
    assert one.add(5,4) == 9
    assert one.add(-3,4) == 1
    assert one.add(-3,0) == -3

def test_zarb():
    assert one.zarb(2,3) == 6
    assert one.zarb(2,0) == 0
    assert one.zarb(-2,-3) == 6
    assert one.zarb(-2,3) == -6



