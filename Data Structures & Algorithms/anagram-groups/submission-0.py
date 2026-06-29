class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = defaultdict(list)
        res = []
        for word in strs:
            key = ''.join(sorted(word))
            char_dict[key].append(word)
        print(char_dict)
        for val in char_dict.values():
            res.append(val)
        
        return res