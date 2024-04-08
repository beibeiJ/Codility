'''
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].
'''

import unittest

def solution(A):
    # check if there is duplicate in A
    if len(set(A)) != len(A):
        return 0
    
    P = list(range(1, len(A)+1))

    if sum(P) == sum(A):
        return 1
    else:
        return 0
    



class TestSkeleton(unittest.TestCase):
    
    def test(self):
        self.assertEqual(solution([4, 1, 2, 3]), 1)

    def test_not(self):
        self.assertEqual(solution([4, 1, 3]), 0)

    def test_extreme(self):
        self.assertEqual(solution([2]), 0)

    def test_double(self):
        self.assertEqual(solution([3, 2]), 0)
    
    def test_duplicate(self):
        self.assertEqual(solution([1, 4, 1]), 0)



if __name__ == '__main__':
    unittest.main()