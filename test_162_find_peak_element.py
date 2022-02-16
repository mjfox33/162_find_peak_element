from re import L
from code_162_find_peak_element import Solution

def test_example_1():
    s = Solution()
    assert s.findPeakElement2([1,2,3,1]) == 2

def test_example_2():
    s = Solution()
    assert s.findPeakElement2([1,2,1,3,5,6,4]) == 5