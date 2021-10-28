from hello import more_hello, more_hii


def test_more_hello():
    assert "hi" == more_hello()


def test_more_hii():
    assert "hii" == more_hii()
