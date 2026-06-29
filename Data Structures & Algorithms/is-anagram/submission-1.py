class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ref_dict = defaultdict(int)
        if(len(s)!=len(t)):
            return False
            
        for char in s:
            ref_dict[char]+=1
        
        for char in t:
            if(ref_dict[char] > 0):
                ref_dict[char]-=1
            else:
                return False
        
        return True