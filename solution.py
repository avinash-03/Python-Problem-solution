class Solution:
    def __init__(self) -> None:
        pass
        
        
    def IsArmstrong(self,number):
        total=0
        for i in str(number):
            total+=(int(i))**3
        if total==int(number):
            return 'This is armstrong number'
        else:
            return 'this is not armstrong number'
