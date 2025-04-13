import pytest

@pytest.fixture
def yield_fixture():
    print("start test phase")
    yield 1 
    print("end test phase")

def test_example(yield_fixture):
    print("running the test")
    assert yield_fixture == 1