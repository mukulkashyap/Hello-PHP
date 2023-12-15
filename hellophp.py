#find the max number in the array. A basic demonstration of parameter passing,for loop and function. 

def findMaxInArray(itemLs):
    min = -1
    for item in itemLs:
            if(item>min):
                min=item
    if(min==-1):
        return "empty list provided"    
    else:
         return min

iputarray=[1,6,5,3,4,2]
min = findMaxInArray(iputarray)
print(min)