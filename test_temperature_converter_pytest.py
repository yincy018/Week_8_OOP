import pytest
from temperature_converter import *



def test_fahrenheit_to_celsius():
    # Test freezing temperature
    assert f_to_c(32) == 0
    # Test boiling temperature
def test_equal():   
    assert f_to_c(212) == 100
    # Test float
def test_f_to_c_almost_equal():
    assert f_to_c(31.0) == pytest.approx(-0.5555555555)
    
    # Test errors
def test_error():
    with pytest.raises(TypeError):
        f_to_c('freezing')


def test_celsius_to_fahrenheit():
        # Test freezing temperature
    assert c_to_F(0) == 32
   
def test_equal():
    # Test boiling temperature
    assert c_to_F(100) == 212
        
def test_almost():
    # Test float
    assert c_to_F(-0.5555555555) == pytest.approx(31) 

def test_error():
    # Test errors
    with pytest.raises(TypeError):
        c_to_F('freezing')

pytest.main()