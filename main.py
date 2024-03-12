class RomanToInt:
    def __init__(self, s):
        self.s = s

    def getList(self):
        list = [i for i in self.s]
        print(list)
        return list

    def checkEdgeCases(self,currentChar,prevChar,convDict, num):
        if currentChar == 'I' and prevChar in ['V', 'X']:
            num = num -1
        elif currentChar == 'X' and prevChar in ['L','C']:
            num = num - 10
        elif currentChar == 'C' and prevChar in ['D', 'M']:
            num = num - 100
        else:
            num = num + convDict[currentChar]
        return num
    def romanToInt(self):
        """
        :param s: str
        :return: int
        """
        convDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        romanList = self.getList()
        num = 0
        for i in range(len(romanList)-1, -1, -1):
            if romanList[i] in ['I','X','C'] and i > 0 and i != len(romanList)-1:
                num = self.checkEdgeCases(romanList[i],romanList[i+1],convDict, num)
            else:
                num = num + convDict[romanList[i]]
        print(num)
        return num


if __name__ == '__main__':
    r = RomanToInt("MCMXCIV")
    r.romanToInt()
