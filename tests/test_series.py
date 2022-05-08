from math_series import __version__
from math_series.series import *

def test_1(): 
    expected = 34
    actual = fibonanci(9) 
    assert expected == actual 

def test_2(): 
    expected = 21
    actual = fibonanci(8)
    assert expected == actual

def test_3(): 
    expected = 1
    actual = fibonanci(1)
    assert expected == actual

def test_4(): 
    expected = 1
    actual = fibonanci(2)
    assert expected == actual 
def test_0(): 
    expected = 0
    actual = fibonanci(0)
    assert expected == actual







#  lucas test
def test_2_1(): 
    expected = 2
    actual = lucas_recursion(1) 
    assert expected == actual 

def test_2_2(): 
    expected = 3
    actual = lucas_recursion(2)
    assert expected == actual

def test_2_3(): 
    expected = 7
    actual = lucas_recursion(4)
    assert expected == actual

def test_2_4(): 
    expected = 11
    actual = lucas_recursion(5)
    assert expected == actual 


#  test for sum_series

def test_2_1(): 
    expected = 0
    actual = sum_series(1)
    assert expected == actual

def test_3_2(): 
    expected = 2
    actual = sum_series(1,2,1) 
    assert expected == actual 

def test_3_3(): 
    expected = 1
    actual = sum_series(2,4,1)
    assert expected == actual

def test_3_4(): 
    expected = 3
    actual = sum_series(1,3,3)
    assert expected == actual 

def test_3_6(): 
    expected = 12
    actual = sum_series(4,4,4)
    assert expected == actual 

def test_3_6(): 
    expected = 25
    actual = sum_series(5,5,5)
    assert expected == actual 

def test_3_6(): 
    expected = 19
    actual = sum_series(5,5,3)
    assert expected == actual 


def test_3_5(): 
    expected = 'plese the number must more than 0'
    actual = sum_series(0)
    assert expected == actual