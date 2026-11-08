class Solution(object):
    def isValid(self, s):
        open_brack = ["(","[","{"]
        close_brack = [")","]","}"]
        list1 = []
        index1 = 0
        for i in s:
            if i in open_brack:
                list1.append(i)                
            else:
                if not list1:
                    return False
                index1 = close_brack.index(i)
                if open_brack.index(list1[-1]) == index1:
                    list1.pop()
                else:
                    return False
        return len(list1) == 0


        