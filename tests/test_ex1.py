import pytest 

# def test_demo():
#     assert 1 == 1 

# @pytest.mark.skip
# @pytest.mark.xfail
# @pytest.mark.slow
# def test_demo1():
#     print("hello")
#     assert 2 == 2 

# @pytest.fixture
# def fix1():
#     print("fixture 01")
#     return 3 
# def test_fix1(fix1):
#     num = fix1
#     assert num == 3 


# @pytest.fixture(scope="session")
@pytest.fixture(scope="function")
def fix1():
    print("fixture 01")
    return 3 
def test_fix1(fix1):
    num = fix1
    assert num == 3 
def test_fix2(fix1):
    num = fix1 
    assert num == 3
