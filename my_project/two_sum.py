class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,v in enumerate(nums):
            next_num = i+1
            while next_num < len(nums):
                result = v+nums[next_num]
                if result == target:
                    return [i, next_num]                
                next_num += 1

if __name__ == '__main__':
    s = Solution()
    s.twoSum([1,2,4], 6)