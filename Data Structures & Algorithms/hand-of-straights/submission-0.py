class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        freq = Counter(hand)

        for card in sorted(hand):
            if freq[card] == 0:
                continue
            
            for i in range(card, card+groupSize):
                if freq[i] == 0:
                    return False
                freq[i] -= 1
        return True