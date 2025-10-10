import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers, including zeros and negatives."""
    assert longest_positive_streak([-1, -5, 0, -3]) == 0

def test_single_streak():
    """Test a simple case with a single streak of positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks_longest_is_last():
    """Test multiple streaks where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3

def test_multiple_streaks_longest_is_first():
    """Test multiple streaks where the longest streak is at the beginning."""
    assert longest_positive_streak([1, 2, 3, 4, -1, 5, 6]) == 4

def test_example_case():
    """Test the primary example case from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_ones():
    """Test a streak consisting of only the number 1."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_zero():
    """Test a list with a single zero."""
    assert longest_positive_streak([0]) == 0

def test_single_element_negative():
    """Test a list with a single negative number."""
    assert longest_positive_streak([-5]) == 0

def test_streak_ending_with_zero():
    """Test a streak that is immediately followed by a zero."""
    assert longest_positive_streak([1, 2, 3, 0]) == 3

def test_streak_ending_with_negative():
    """Test a streak that is immediately followed by a negative number."""
    assert longest_positive_streak([1, 2, 3, -1]) == 3

def test_interspersed_negatives_and_zeros():
    """Test a complex case with positive numbers, negatives, and zeros interspersed."""
    assert longest_positive_streak([1, 0, 2, 3, -4, 5, 6, 7, 8, 0, 9]) == 4