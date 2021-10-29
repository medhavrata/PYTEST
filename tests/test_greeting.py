import pytest

from greeting import my_name

@pytest.fixture
def bob():
    return "my name is: bob"

@pytest.fixture
def sally():
    return "my name is: sally"

def test_bob(bob):
    assert bob == my_name("bob")

def test_sally(sally):
    assert sally == my_name("sally")
    
