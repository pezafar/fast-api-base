import pytest

from app.core.paginator import pagenation

"""
In order to test behavior of pagenation function
"""


def test_pagenation_400_initial_default():
    d = pagenation(list(range(400)), 1, 20)
    assert d["listings"] == list(range(0, 20))


def test_pagenation_400_10th_page():
    d = pagenation(list(range(400)), 10, 20)
    assert d["listings"] == list(range(180, 200))


def test_pagenation_400_start_0():
    d = pagenation(list(range(400)), 19, 20, start_page_as_1=False)
    assert d["listings"] == list(range(380, 400))


def test_pagenation_400_start_1():
    d = pagenation(list(range(400)), 20, 20)
    assert d["listings"] == list(range(380, 400))


def test_pagenation_400_set_start_1_equals_True_and_init_as_pagenumber_as_0():
    """Exception case"""
    with pytest.raises(Exception, match=r".* starts > 0. *"):
        pagenation(list(range(400)), 0, 20)
