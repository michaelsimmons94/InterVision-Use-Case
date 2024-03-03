import pytest

from .handler import generate_prompt

@pytest.mark.parametrize("question, zodiacSign, expected", [
    ("Should I change jobs?", "Aries", "Pretend you're an astrologer, I am a Aries. Give me a short horoscope without an introduction, answering the question \"Should I change jobs?\""),
])
def test_generate_prompt(question, zodiacSign, expected):
    assert generate_prompt(question, zodiacSign) == expected
