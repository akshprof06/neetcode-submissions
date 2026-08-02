class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums): #this actually maps the values to it's indices
            complement = target - n
            if complement in seen:
                return [seen[complement],i]
            seen[n] = i
        
        return [0,0]
                    