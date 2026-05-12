# test_random.py
import random
from src.linear_search import linear_search
from src.oracle import oracle_linear_search

def test_random_cases():
    random.seed(42)

    N = 500 

    for _ in range(N):
        v = [random.randint(-10, 10) for _ in range(5)]

        key = random.randint(-10, 10)

        expected = oracle_linear_search(v, key)
        result = linear_search(v, key)

        assert result == expected, f"Eroare pentru v={v}, key={key}"