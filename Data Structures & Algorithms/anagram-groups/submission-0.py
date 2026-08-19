from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list) # Automatically initializes missing keys with empty lists
        
        for s in strs:
            count = [0] * 26
            for ch in s:
                # Calculate index 0-25 and increment count safely
                count[ord(ch) - ord('a')] += 1
            
            # Convert list to tuple so it can be used as a dictionary key
            mp[tuple(count)].append(s)
            
        return list(mp.values())