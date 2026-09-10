import sys

from toy_server.core.seppuku.memory import generate_footprint, M_SIZE, K_SIZE


def test_footprint_kb():
    N = 123
    output = generate_footprint(N, "KB")
    expected_size = 33 + (N * K_SIZE)

    assert sys.getsizeof(output) == expected_size


def test_footprint_mb():
    N = 23
    output = generate_footprint(N, "MB")
    expected_size = 33 + (N * M_SIZE)
    assert sys.getsizeof(output) == expected_size


def test_footprint_gb():
    N = 1
    output = generate_footprint(N, "GB")
    expected_size = 33 +  (N * M_SIZE * 1000)
    assert sys.getsizeof(output) == expected_size
