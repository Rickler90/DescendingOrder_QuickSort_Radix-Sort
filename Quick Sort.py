import random
numbers = []
count = 0
start = int(input("Input starting value: "))
end = int(input("Input ending value: "))

while count<10:
    num = random.randint(start,end)
    numbers.append(num)
    count+=1
print("Generated Random Numbers:",numbers)
first = numbers.copy()
last = numbers.copy()
mid = numbers.copy()

def partitionFirst(array, start, end):

    pivot = array[start]
    print("Pivot = ",pivot)
    low = start + 1
    high = end
    
    while True:
        while low <= high and array[high] <= pivot:
            high = high - 1
        print(array)    
        while low <= high and array[low] >= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high

def quickSort_First(array, start, end):
    if start >= end:
        return

    p = partitionFirst(array, start, end)
    quickSort_First(array, start, p-1)
    quickSort_First(array, p+1, end)

def quickSort_Mid(array, start, end):
    if start >= end:
        return

    p = partitionMid(array, start, end)
    quickSort_Mid(array, start, p-1)
    quickSort_Mid(array, p+1, end)


def partitionMid(array, start, end):
    mid = end//2
    pivot = array[mid]
    print("Pivot = ",pivot)
    low = start + 1
    high = end
    
    while True:
 
        while low <= high and array[low] >= pivot:
            low = low + 1
        print(array)   
        while low <= high and array[high] <= pivot:
            high = high - 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high

def partitionLast(array, start, end):
    pivot = array[end]
    print("Pivot = ",pivot)
    low = start
    high = end-1

    while True:
        while low <= high and array[low] >= pivot:
            low = low + 1
        print(array)  
        while low <= high and array[high] <= pivot:
            high = high - 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[end], array[low] = array[low], array[end]
    return high

def quickSort_Last(array, start, end):
    if start >= end:
        return

    p = partitionLast(array, start, end)
    quickSort_Last(array, p+1, end)
    quickSort_Last(array, start, p)

def sort(x):
    pivot = x
    a=[]
    while True:
        i = 0
        count = len(numbers)-1
        while i < len(numbers):
            p = numbers[numbers.index(pivot)]
            if p < numbers[count]:
                temp = numbers[count]
                numbers[count] = p
                numbers[numbers.index(pivot)] = temp
                print(numbers)
                break
            count = count-1
            i = i+1
            a=numbers
        if a==numbers:

            break

        i = 0
        count = 0   
        while i < len(numbers):
            p = numbers[numbers.index(pivot)]
            if p > numbers[count]:
                temp = numbers[count]
                numbers[numbers.index(pivot)] = temp
                numbers[count] = p
                print(numbers)
                break
            count = count+1
            i = i+1

def check(list1, val):
    count=0 
    for x in list1: 
        if val <+ x:
            count=count+1
    return count 

def quick():
    i=0
    while i<len(numbers):
        check(numbers[i:],numbers[i])
        if (check(numbers[i:],numbers[i])):
            for x in numbers:
                if numbers[i]<x:
                    print("pivot = ",numbers[i])
                    print(numbers)
                    sort(numbers[i])
                    break
        else :
            i=i+1




print("\nOptions:\n[1] Basic \n[2] First Pivot\n[3] Last Pivot\n[4] Middle pivot\n[5] Exit")
while True:
        try: 
                choice=int(input("Enter Choice: "))

                if choice == 1:
                    temp=numbers
                    print("Basic")
                    quick()
                    print("Sorted array is:")
                    for x in numbers:
                    	print(x,end=" ")
                    print()
                    numbers=temp



                elif choice ==2:
                    print("First Pivot")
                    quickSort_First(first, 0, len(numbers) - 1)
                    n = len(numbers)
                    print("Sorted array is:")
                    for i in range(n):
                        print(first[i], end = " ")
                    print()
                    
                elif choice ==3:
                    print("Last Pivot")                    
                    quickSort_Last(last, 0, len(numbers) - 1)
                    n = len(numbers)
                    print("Sorted array is:")
                    for i in range(n):
                        print(last[i], end = " ")
                    print()
                    
                elif choice ==4:
                    print("Middle Pivot")
                    quickSort_Mid(mid, 0, len(numbers) - 1)
                    n = len(numbers)
                    mid.sort(reverse=True)
                    print("Sorted array is:")
                    for i in range(n):
                        print(mid[i], end = " ")
                    print()
              
                elif choice ==5:
                        break
                else:
                    print("Invalid Choice!")

                while True:    
                    main = str(input("Press M/m  to return to main menu:"))
                    if main == "M" or main== "m":
                        print("\nOptions:\n[1] Basic \n[2] First Pivot\n[3] Last Pivot\n[4] Middle pivot\n[5] Exit\n")
                        break                       
                    else:
                        print ("Invalid Input!")
                        continue
                        
        except ValueError:
                print ("Invalid Input!")



