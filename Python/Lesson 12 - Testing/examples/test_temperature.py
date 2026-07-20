# test_temperature.py
import pytest
from temperature import celsius_to_fahrenheit


def test_freezing_point():
    """Water freezes at 0°C = 32°F"""
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point():
    """Water boils at 100°C = 212°F"""
    assert celsius_to_fahrenheit(100) == 212


def test_negative_temperature():
    """Test negative temperatures"""
    assert celsius_to_fahrenheit(-40) == -40  # -40 is the same in both scales!


def test_room_temperature():
    """Room temperature conversion"""
    assert celsius_to_fahrenheit(25) == 77


def test_below_absolute_zero():
    """Should raise ValueError for impossible temperatures"""
    with pytest.raises(ValueError, match="absolute zero"):
        celsius_to_fahrenheit(-300)
