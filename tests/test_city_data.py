from session2 import Session2
import pytest


def test_load_and_total_population():
    s2 = Session2()
    rows = s2.load_cities()
    assert len(rows) == 5
    assert s2.total_population(rows) == 136_669_851
    top_three = s2.top_cities(rows, n=3)
    assert top_three == ["Tokyo", "Delhi", "Shanghai"]


def test_average_population_and_empty_error():
    s2 = Session2()
    rows = s2.load_cities()
    avg = s2.average_population(rows)
    assert avg == pytest.approx(27_333_970.2)
    with pytest.raises(ValueError):
        s2.average_population([])
