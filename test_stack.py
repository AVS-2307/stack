import unittest

import pytest
from Stack import Stack

fixture_for_test_isEmpty_good = [('[]', True)]


@pytest.mark.parametrize('list_, expected_result', fixture_for_test_isEmpty_good)
def test_isEmpty_good(list_, expected_result):
    s = Stack()
    assert s.isEmpty() == expected_result


fixture_for_test_push_good = [(1, [1]),
                              (2, [2])]


@pytest.mark.parametrize('item, expected_result', fixture_for_test_push_good)
def test_push_good(item, expected_result):
    s = Stack()
    assert s.push(item) == expected_result


# fixture_for_test_push_bad = [(AssertionError, 1, [5]),
#                              (AssertionError, 2, [8])]

# @pytest.mark.parametrize('expected_exception, item, expected_result', fixture_for_test_push_bad)
# def test_push_bad(expected_exception, item, expected_result):
#     with pytest.raises(expected_exception):
#         s = Stack()
#         assert s.push(item) == expected_result
#
# fixture_for_test_pop_good = [([1, 2, 5], 5),
#                               ([1, 2, 5, 17, 45], 45)]


@pytest.mark.parametrize('list_first, expected_result', fixture_for_test_pop_good)
def test_pop_good(list_first, expected_result):
    s = list_first
    assert s.pop() == expected_result
