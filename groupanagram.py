from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        result=[]
        if len(strs) ==0: return [[""]]
        if len(strs) ==1: return [strs]
        for s in strs:
            temp = ''.join(sorted(s))
            print(temp)
            print(s)
            if temp in dict1:
                x = dict1[temp]
                x.append(s)
                dict1[temp] = x
            else:
                dict1[temp] = [s]
        for i,v in dict1.items():
            result.append(v)
        return result

c=Solution()
print(c.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(c.groupAnagrams(["a"]))
