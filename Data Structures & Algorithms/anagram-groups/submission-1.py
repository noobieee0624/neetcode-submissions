class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 26-element tuple that maps a certain frequency to a list of strings sharing those 
        # frequencies
        freq = {}
        answer = []
        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char)-ord('a')] = key[ord(char)-ord('a')] + 1
            freq.setdefault(tuple(key), []).append(s)
        
        for key, value in freq.items():
            answer.append(value)
        return answer

        