import pytest
from prettyfind import findall, findsub


@pytest.fixture
def text():
    return "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"


@pytest.mark.parametrize('word, results', [("Peter", [1, 20, 75]), ("peter", [1, 20, 75]), ("pick",	[30, 58]),
                                           ("pi", [30, 37, 43, 51, 58]), ("z", []), ("Peterz", [])])
def test_findall(word, results, text):
    assert findall(text, word) == results


def test_findsub():
    assert findsub('peteredter', 'ter') == [2, 7]
