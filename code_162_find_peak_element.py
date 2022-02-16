class Solution:
    # keep it simple
    def findPeakElement(self, nums: list[int]) -> int:
        max_num = max(nums)
        return nums.index(max_num)

    # now implement binary search returning the index
    def findPeakElement2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        pointer_left = 0
        pointer_right = n - 1

        while pointer_left != pointer_right:
            mid = (pointer_right + pointer_left -1) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                pointer_left = mid + 1
            else:
                pointer_right = mid - 1
        
        return pointer_left if nums[pointer_left] >= nums[pointer_right] else pointer_right