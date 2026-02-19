from toy_server.core.sieve import prime_sieve


def test_sieve_small():
    res = prime_sieve(5)
    assert res == 11


def test_sieve_large():
    res = prime_sieve(10000)
    assert res == 104729


def test_sieve_invalid():
    res = prime_sieve(-10)
    assert res is None