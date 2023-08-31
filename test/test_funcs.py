import pytest

from code_bank.funcs import transformed_date
from code_bank.funcs import transformed_from
from code_bank.funcs import transformed_to

def test_transformeddate():
    assert transformed_date("2018-11-29T07:18:23.941293") == "29.11.2018"
    assert transformed_date("2018-11-29T07:18:23.941293") != "2018.11.29"

def test_transformedfrom():
    assert transformed_from("MasterCard 3152479541115065") == "MasterCard 3152 7** **** 5065"
    assert transformed_from("Счет 27248529432547658655") == "Счет 2724 5** **** **** 8655"
    assert transformed_from("MasterCard 3152479541115065") != "MasterCard 31527******5065"

def test_transformedto():
    assert transformed_to("Счет 43597928997568165086") == "Счет **5086"
    assert transformed_to("Visa Gold 9447344650495960") == "Visa Gold **5960"
    assert transformed_to("Visa Gold 9447344650495960") != "VisaGold **5960"