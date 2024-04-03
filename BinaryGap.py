
'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is 
surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. 
The number 20 has binary representation 10100 and contains one binary gap of length 1. 
The number 15 has binary representation 1111 and has no binary gaps. 
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and 
so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary 
representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''
import unittest
import numpy as np

def solution_numpy(N):
    # Implement your solution here
    # when N<0, no gap
    if N < 0:
        return 0

    # binary representation
    binaryN = str("{0:b}".format(N))

    # list how many 1 found in binary representation
    ids = [i for i, letter in enumerate(binaryN) if letter == '1']
    
    if len(ids) == 1:
        return 0

    # length of gap(s)
    len_gaps = np.diff(ids) - 1

    return(len_gaps.max())


def solution(N):
    # Implement your solution here
    # when N<0, no gap
    if N < 0:
        return 0

    # binary representation
    binaryN = str("{0:b}".format(N))

    # list how many 1 found in binary representation
    ids = [i for i, letter in enumerate(binaryN) if letter == '1']
    
    if len(ids) == 1:
        return 0

    # length of gap(s)
    len_gaps = [ids[i] - ids[i-1] - 1 for i in range(1,len(ids))]

    return(max(len_gaps))


class TestSkeleton(unittest.TestCase):
    
    def test_negative(self):
        self.assertEqual(solution(-1), 0)

    def test_extreme_small(self):
        self.assertEqual(solution(0), 0)
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(5), 1)  

        
    def test_longest_binary_gap(self):
        self.assertEqual(solution(1041), 5)
        self.assertEqual(solution(42),1)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(19), 2)
                                             
    def test_no_binary_gap(self):
        self.assertEqual(solution(32), 0)

                  
    def test_extreme_large_binary_gap(self):
        self.assertEqual(solution(2147483647), 0)
        self.assertEqual(solution(3908253), 3)

if __name__ == '__main__':
    unittest.main()