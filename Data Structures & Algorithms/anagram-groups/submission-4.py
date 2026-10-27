class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for word in strs:
            arr=[0]*26
            for c in word:
                arr[ord(c)-ord('a')]+=1
            key=tuple(arr)
            if key not in s:
                s[key]=[]
            s[key].append(word)
        return list(s.values())        



        