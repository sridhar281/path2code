class Solution:
    def clearDigits(self, s: str) -> str:
        re=[]
        for i in s:
            if i.isdigit():
                if re:
                    re.pop()
            else:
                re.append(i)
        return "".join(re)

        