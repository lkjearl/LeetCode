class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        aCounter = 0  # Counter for consecutive 'A's
        bCounter = 0    # Counter for consecutive 'B's

        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    aCounter += 1
                else:
                    bCounter += 1
        
        return aCounter > bCounter