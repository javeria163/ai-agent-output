# Solution

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Tests

def test_celsius_to_fahrenheit():
    assert round(celsius_to_fahrenheit(0), 2) == 32
    assert round(celsius_to_fahrenheit(100), 2) == 212
    assert round(celsius_to_fahrenheit(-40), 2) == -40