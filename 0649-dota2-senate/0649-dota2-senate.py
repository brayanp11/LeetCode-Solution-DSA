from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        radiant, dire = deque(),  deque()

        for i, c in enumerate(senate):
            if c == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            rTurn, dTurn = radiant.popleft(), dire.popleft()
            if rTurn < dTurn:
                radiant.append(rTurn + len(senate))
            else:
                dire.append(dTurn + len(senate))

        return "Radiant" if radiant else "Dire"