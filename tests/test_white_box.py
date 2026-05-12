from src.linear_search import linear_search

def test_multiple():
    assert linear_search([1,2,2,3], 2) == 1

def test_single():
    assert linear_search([5], 5) == 0