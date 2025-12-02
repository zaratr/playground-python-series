from session1 import first_name, age2, TOTAL
from session2 import Session2

session2 = Session2()


def test_session1_variables():
    assert first_name == "John"
    assert age2 == 22
    assert TOTAL == 100


def test_calculate_and_square():
    assert session2.calculate(2, 3) == (5, 6)
    assert session2.square(5) == 25


def test_welcome_print(capsys):
    # welcome prints to stdout
    session2.welcome("Tester")
    captured = capsys.readouterr()
    assert "Welcome Tester" in captured.out
