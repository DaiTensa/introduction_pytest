from basics.src.inverse import inverse
import pytest

def test_long_list():
    assert inverse(["a", "b", "c", "d", "e"]) == "edcba"

def test_four_element():
    assert inverse(["a", "b", "c", "d"]) == "cba"

def test_error_when_integer():
    with pytest.raises(ValueError):
        inverse(87) 

def test_lower_cases():
    assert inverse("hello") == "olleh"

def test_lower_cases_four_elements():
    assert inverse("hell") == "lleh"

    