class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            elem = 1
            for j in range(0,len(nums)):
                if j == i :
                    continue
                    
                elem *= nums[j]

            result.append(elem)

        return result
                

        