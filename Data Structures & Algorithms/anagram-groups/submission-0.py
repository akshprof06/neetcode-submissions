class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used = [False] * len(strs)

        for i in range (len(strs)):

            if used[i]:
                continue
            group = [strs[i]]
            used[i] = True
            for j in range(i+1,len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    used[j] = True
            result.append(group)

        return result

#Brute force solution each string is sorted and compared so it's O(n^2 . k logk)