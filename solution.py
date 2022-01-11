class Solution:
    def __init__(self) -> None:
        pass
        
    @staticmethod   
    def IsArmstrong(number):
        total=0
        for i in str(number):
            total+=(int(i))**3
        if total==int(number):
            return 'This is armstrong number'
        else:
            return 'this is not armstrong number'

    @staticmethod
    def IsPalidromNum(List):
        for i in List:
            if str(i)==str(i)[::-1]:
                print(i,':this is palidrom number')
            else:
                print(i,":this is not polidrom number")

    @staticmethod
    def frequencySort(nums):
        nums.sort()
        list1= sorted(nums,key=nums.count,reverse=True)
        list2=[]
        for i in list1:
            if i not in list2:
                list2.append(i)

        return list2