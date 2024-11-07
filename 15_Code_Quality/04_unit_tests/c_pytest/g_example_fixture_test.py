import pytest 


@pytest.fixture
def setup_logger():
    print('\n TEst Started')
    yield
    print('\n Test completed')


def test_example(setup_logger):
    print('Running test_example')
    assert 1 + 1 == 2


# Assignment - fixture for time taken for a test