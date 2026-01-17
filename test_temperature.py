from temperature import celsius_to_fahrenheit
def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32.0

def test_integer_celsius():
    assert round(celsius_to_fahrenheit(25), 2) == 77.00

def test_float_celsius():
    assert round(celsius_to_fahrenheit(37.5), 2) == 99.50
