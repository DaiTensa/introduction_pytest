from exrecices.src.fonction_advanced import input_function_fois_deux, create_file, randomize
from unittest.mock import patch
import random


def test_input_function_fois_deux():
    with patch('builtins.input', return_value= '3'):
        assert input_function_fois_deux() == 6

def test_create_file(tmpdir):
    file_path = tmpdir.join("liste_apprennant.txt")
    create_file(file_path, "\nAlfred")
    with open(file_path, "r") as fichier:
        assert "\nAlfred" in fichier.read()

random.seed(42)

def test_randomize():
    assert randomize() == 0.6394267984578837