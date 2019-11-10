import pytest
from math_func import *


def test_add():
    assert add(4, 8) == 12


def test_multiply():
    assert multiply(6, 6) == 36
