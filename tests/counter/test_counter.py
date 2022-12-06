from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():
    assert count_ocurrences("data/jobs.csv", "python") == 1639


def test_counter2():
    assert count_ocurrences("data/jobs.csv", "Java") == 676


def test_counter3():
    with pytest.raises(FileNotFoundError):
        count_ocurrences("data/jobs.json", "javascript")
