class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        map = {}
        for word in strs:
            anagram_word = ''.join(sorted(word))
            res[anagram_word].append(word)


        return list(res.values())
