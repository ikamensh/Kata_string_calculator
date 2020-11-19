import pytest

import str_calc


def test_add_zero_args():
    assert str_calc.add("") == 0


def test_add_one_arg():
    assert str_calc.add("123") == 123


def test_add_two_args():
    assert str_calc.add("123, 12") == 135
    assert str_calc.add("123,12") == 135


def test_newline():
    assert str_calc.add("123\n12") == 135
    assert str_calc.add("123\n12, 12") == 147


def test_custom_delim():
    assert str_calc.add("//;\n123;12") == 135

def test_negatives():
    with pytest.raises(Exception) as e:
        str_calc.add("-1")
    assert "negatives not allowed" in str(e)
    assert "-1" in str(e)

def test_many_negatives():
    with pytest.raises(Exception) as e:
        str_calc.add("-1, 13, -7")
    assert "negatives not allowed" in str(e)
    assert "-1" in str(e)
    assert "-7" in str(e)

try:
    a = "abc"
except Exception as e:
    print("SUCCESS")
else:
    print(a)
    assert False, "Expected to fail"


