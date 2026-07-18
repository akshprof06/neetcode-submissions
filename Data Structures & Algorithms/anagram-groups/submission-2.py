class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')] +=1
            group[tuple(freq)].append(s)
        return list(group.values())

#Optimized O(m*n) as no sorting. For each of m strings one pass of length n to build freq array.