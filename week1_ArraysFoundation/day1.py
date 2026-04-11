# Problem 1: Find Max / Min in Array
 
def twosum(number, target):
    store = {}
    for i in range(len(number)):
        num = number[i]
        result = target - num
        if result in store:
            return [store[result], i]

        store[num] = i

number = [3,2,4]
target = 6  
print(twosum(number, target))         