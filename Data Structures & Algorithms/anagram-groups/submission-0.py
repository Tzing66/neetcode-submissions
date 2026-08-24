class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for w in strs:
            f = ''.join(sorted(w)) #returns a string, sorted only returns a list

            if f not in groups:
                groups[f] = []
            groups[f].append(w)
        

        return list(groups.values())





        
        

        

