class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True
        else:
            return False
#O(nlogn) as sorting is o( nlog n)