'''


An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].
'''
import unittest

def solution(A):
    # sum of arithmetic sequence
    # if there is one element missing, simply considering the length of complete array should be length of A plus 1
    n = len(A)+1
    result = n * (n + 1) // 2

    return result - sum(A)


class TestSkeleton(unittest.TestCase):
    
    def test(self):
        self.assertEqual(solution([2, 3, 1, 5]), 4)

    
    def test_empty(self):
        self.assertEqual(solution([]), 1)
        


if __name__ == '__main__':
    unittest.main()