# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        c = num1 + num2
        c.sort()
        b = len(c)
        if b % 2 == 0:
            mid1 = b // 2
            mid2 = b // 2 - 1
            answer = (c[mid1] + c[mid2]) / 2
        elif b%2!=0:
            A1 = b // 2
            answer = c[A1]
        return answer

# Create an instance of the Solution class
solution = Solution()
num1 = [2,1]
num2 = [3,4]
result = solution.findMedianSortedArrays(num1, num2)
print(result)  # Ensure the closing parenthesis is present




        