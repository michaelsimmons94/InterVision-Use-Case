import pytest
import sys
import os

from .handler import determine_zodiac_sign

@pytest.mark.parametrize("date,expected", [
    ("1994-03-30","Aries"),
    ("1994-04-20","Taurus"),
    ("1994-05-21","Gemini"),
    ("1994-06-21","Cancer"),
    ("1994-07-23","Leo"),
    ("1994-08-23","Virgo"),
    ("1994-09-23","Libra"),
    ("1994-10-23","Scorpio"),
    ("1994-11-22","Sagittarius"),
    ("1994-12-22","Capricorn"),
    ("1994-01-20","Aquarius"),
    ("1994-02-19","Pisces"),
])
def test_determine_zodiac_sign(date, expected):
    assert determine_zodiac_sign(date) == expected