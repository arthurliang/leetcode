# Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dic = {}
        for i in range(len(num)):
            if num[i] not in dic:
                dic[num[i]] = 1
            else:
                dic[num[i]] += 1
        l = sorted(dic.items(), key=lambda dic:dic[1], reverse = True)

        return l[0][0]