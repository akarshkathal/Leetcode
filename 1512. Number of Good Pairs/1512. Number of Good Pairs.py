class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]==nums[j]):
                    count+=1
        return count

obj = Solution()
obj.numIdenticalPairs([1,2,3,1,1,3])