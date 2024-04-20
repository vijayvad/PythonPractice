class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dict1={}
        dict2={}
        for c in s:
            if c in dict1:
                dict1[c] +=1
            else:
                dict1[c] =1
        for c in t:
            if c in dict2:
                dict2[c] +=1
            else:
                dict2[c] =1
        for k,v in dict1.items():
            if dict2.get(k) != v :
                return False
        return True
        # return dict1 == dict2

c=Solution()
print(c.isAnagram("anagram","nagaram"))