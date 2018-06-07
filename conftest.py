import pytest


def pytest_addoption(parser):
    parser.addoption('--rounding_index', action='store', default=10,
                     help='rounding index, default=10')


@pytest.fixture(scope='module')
def rounding_index(request):
    _rounding_index = request.config.getoption('--rounding_index')
    return int(_rounding_index)
