# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        # 1st step: sort num
        # 2nd step: binary search index
        index1 = 0
        self.index2 = 0
        len_n = len(num)

        key = lambda item:item[1]
        num = self.sortList(list(enumerate(num, 1)), key)

        while index1 < len_n - 1:
            temp = target - key(num[index1])
            if self.search(temp, num, index1 + 1, len_n - 1, key):
                break
            index1 += 1

        return min(num[index1][0], num[self.index2][0]), max(num[index1][0], num[self.index2][0])

    def search(self, target, l, lo, hi, key=lambda item:item):
        index = self.binarySearch(target, l, lo, hi, key)
        if index == -1:
            return False

        self.index2 = index
        return True

    def binarySearch(self, target, A, lo, hi, key=lambda item:item):
        if lo > hi:
            return -1
        elif lo == hi and key(A[lo]) == target:
            return lo
        else:
            mid = (lo + hi) / 2
            if key(A[mid]) == target:
                return mid
            elif key(A[mid]) > target:
                return self.binarySearch(target, A, lo, mid - 1, key)
            else:
                return self.binarySearch(target, A, mid + 1, hi, key)


    def sortList(self, l, key=lambda item:item):
        self.quicksort(l, 0, len(l) - 1, key)
        return l

    def quicksort(self, A, lo, hi, key=lambda item:item):
        if lo < hi:
            mid = self.partition(A, lo, hi, key)
            self.quicksort(A, lo, mid - 1, key)
            self.quicksort(A, mid + 1, hi, key)

    def partition(self, A, lo, hi, key):
        pivotIndex = self.choosePivot(A, lo, hi, key)
        pivotValue = key(A[pivotIndex])
        storeIndex = hi
        A[storeIndex], A[pivotIndex] = A[pivotIndex], A[storeIndex]
        hi -= 1

        while True:
            while key(A[lo]) < pivotValue:
                lo += 1
            while key(A[hi]) > pivotValue:
                hi -= 1
            if lo < hi:
                A[lo], A[hi] = A[hi], A[lo]
                lo += 1
                hi -= 1
            else:
                break

        A[lo], A[storeIndex] = A[storeIndex], A[lo]
        return lo

    def choosePivot(self, A, lo, hi, key):
        mid = (lo + hi) / 2
        l = [(key(A[lo]), lo), (key(A[mid]), mid), (key(A[hi]), hi)]
        l.sort(key=lambda item:item[0])
        return l[1][1]
