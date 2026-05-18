class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sumOverSixty = 0

        for n in details:
           if(int(n[11:13]) > 60):
            sumOverSixty+=1
        return sumOverSixty