class Solution:
    def isValid(self, s: str) -> bool:
        sOpen = []
        pair = 0
        for i in range(len(s)):
            if ((s[i] == "(" )| (s[i] == "[") | (s[i] == "{")):
                sOpen.append(s[i])
            if (s[i] == ")")&(sOpen != []):
                if sOpen.pop() == "(":
                    pair+=1
                else:
                    return False
            elif(s[i] == "]")&(sOpen != []):
                if sOpen.pop() == "[":
                    pair+=1
                else:
                    return False
            elif(s[i] == "}")&(sOpen != []):
                if sOpen.pop() == "{":
                    pair+=1
                else:
                    return False
            elif(len(s)%2 != 0):
                return False
        if(sOpen != []):
            return False
        elif(pair*2 == len(s)):
            return True
