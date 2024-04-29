from exrecices.src.fonction_simple import add, divide, add_integer, alea_uniform
import pytest

####### TEST  add ########

def test_add_int():
    assert add(4,9) == 13
    assert add(0,0) == 0
    assert add(-1,1) == 0
    assert add(-1,-1) == -2

def test_add_float():
    assert add(2.0, 2.0) == 4.0
    assert add(0.0, 0.0) == 0.0
    assert add(-1.0, -1.0) == -2.0
    assert add(-1.0, 1.0) == 0.0

def test_add_strings():
    assert add("a", "b") == "ab" 
    assert add("a", "") == "a" 
    assert add("", "") == "" 
    assert add ("", "a") == "a"


def test_add_error_mixed_type():
    with pytest.raises(TypeError):
        add("a", 1)

    with pytest.raises(TypeError):
        add(2, [1,2])

    with pytest.raises(TypeError):
        add("a", ["2", "3"])

########### TEST divide ###############

def test_div():
    assert divide(6,3) == 2
    assert divide(1,2) == 0.5
    assert divide(2.2, 2) == 1.1

    
def test_divide_zero():    
    with pytest.raises(ZeroDivisionError):
        divide(3,0)



######### TEST add_integer ################

def test_add_integer_ok():
    assert add_integer(1,2) == 3

def test_add_integer_typerror():
    with pytest.raises(TypeError):
        add_integer(1.2,2.6)


######## TEST alea_uniform #################

def test_alea_uniform():
    assert isinstance(alea_uniform(0,10), float)
    assert alea_uniform(0,10) <= 10
    assert alea_uniform(0,10) >= 0

# def test_add_integer():
#     if isinstance(a,int) and isinstance(b,int): 
#         pass

