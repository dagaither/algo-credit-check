from credit_check import credit_check
import pytest

def test_one_pass():
    assert credit_check('5541808923795240') == "The number is valid!"
def test_two_pass():
    assert credit_check('5541808923795240') == "The number is valid!"
def test_three_pass():
    assert credit_check("4024007136512380") == "The number is valid!"
def test_four_pass():
    assert credit_check("6011797668867828") == "The number is valid!"


def test_one_fail():
    assert credit_check("5541801923795240") == "The number is invalid!"
def test_two_fail():
    assert credit_check("4024007106512380") == "The number is invalid!"