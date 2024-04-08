'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
'''


import unittest


# complexity: O(N * N) 
# sum() complexity is O(N)
# loop beyond sum(), so complexity is O(N * N)
def solution_original(A):
    diff = []
    lenA = len(A)
    for p in range(1, lenA):
        diff.append(abs(sum(A[0:p]) - sum(A[p:lenA])))
    return min(diff)

# complexity: O(N) 
def solution(A):
    sumA = sum(A)
    # positive infinity
    minDiff = float('inf')
    sumLeft = 0
    for v in A[:-1]:
        sumLeft += v
        # sumRight = sumA - sumLeft
        # difference = sumLeft - sumRight
        # difference = sumLeft - (sumA - sumLeft) = 2*sumLeft -sumA
        minDiff = min(abs(2*sumLeft - sumA), minDiff)
    return minDiff



class TestSkeleton(unittest.TestCase):
    
    def test(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)

    
    # def test_empty(self):
    #     self.assertEqual(solution([]), 1)
        


if __name__ == '__main__':
    unittest.main()