class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        counter = {}
        for i in range(len(order)):
            counter[order[i]] = i
        print(counter)
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            
            for j in range(min(len(first),len(second))):
                if first[j] != second[j]:
                    if counter[first[j]] > counter[second[j]]:
                        return False
                    break
                    
            else:
                if len(first) > len(second):
                    return False
        return True