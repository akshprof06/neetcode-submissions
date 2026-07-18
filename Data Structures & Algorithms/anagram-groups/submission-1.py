class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       group = defaultdict(list)

       for s in strs:
            key = "".join(sorted(s))
            group[key].append(s)
       return list(group.values())

#Optimization over brute force solution each string is sorted and compared once so it's O(n . k logk)