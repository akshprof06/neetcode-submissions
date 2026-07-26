class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempRange = [0] * len(temperatures)
        for i in range(0,len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if(temperatures[j]>temperatures[i]):
                    tempRange[i] = (j -i) + tempRange[i]
                    break
        return tempRange

#Brute force solution with O(n^2) complexity