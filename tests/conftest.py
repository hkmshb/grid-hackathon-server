import pytest
from grid3_hackserver.service import clear_services


@pytest.fixture(autouse=True)
def run_around_tests():
    # clear service registry before running any tests
    clear_services()
