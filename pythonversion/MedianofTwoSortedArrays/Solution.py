# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        total = len(A) + len(B)

        if (total & 1):
            return self.findKth(A, B, total / 2 + 1)
        else:
            return float((self.findKth(A, B, total / 2) + self.findKth(A, B, total / 2 + 1))) / 2


    # @param A: a list
    # @param B: a list
    # @param k: k-th number of smallest element in union of A and B
    # @return: k-th smallest element in union of A and B
    def findKth(self, A, B, k):
        m = len(A)
        n = len(B)

        if m > n:
            return self.findKth(B, A, k)

        if m == 0:
            return B[k - 1]

        if k == 1:
            return min(A[0], B[0])

        pa = min(k / 2, m)
        pb = k - pa

        if A[pa - 1] < B[pb - 1]:
            return self.findKth(A[pa:], B, k - pa)
        elif A[pa - 1] > B[pb - 1]:
            return self.findKth(A, B[pb:], k - pb)
        else:
            return A[pa - 1]
