from src.linear_search import linear_search

def test_found():
    assert linear_search([1, 2, 3], 2) == 1

def test_not_found():
    assert linear_search([1, 2, 3], 5) == -1

def test_empty():
    assert linear_search([], 1) == -1