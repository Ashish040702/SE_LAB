import pytest
import sys
import os
from Source_code.calculator import add, substract
def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(0,0)==0
    
def test_substract():
    assert substract(5,2)==3
    assert substract(2,5)==3
    assert substract(1,1)==3
    
    