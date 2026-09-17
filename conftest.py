import pytest
from selenium import webdriver


@pytest.fixture()
def setup_test():
    print("Start test")
    yield

    print("Finish test")

@pytest.fixture(scope="module")
def set_group_test():
    print("Enter system")
    yield
    print("Exit system")