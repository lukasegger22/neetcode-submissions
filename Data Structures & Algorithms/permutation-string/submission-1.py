class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        count1 = {}
        count2={}
        for char in s1:
            count1[char] = count1.get(char,0)+1
        for index in range(len(s1)):
            count2[s2[index]] = count2.get(s2[index], 0) + 1
        if count1 == count2:
            return True
        for right in range(len(s1), len(s2)):
            left = right - len(s1)
            
            count2[s2[left]] -= 1
            if count2[s2[left]] == 0:
                del count2[s2[left]]
                
            count2[s2[right]] = count2.get(s2[right], 0) + 1
            
            if count1 == count2:
                return True
        return False
