import random
one=[]
ten=[]
hun=[]
thou=[]

def oneplace(a):
    array= a
    i = 0
    c = 9
    while i<=9: 

        for x in array:
            if c==x%10:
                one.append(x)
        c = c - 1
        i= i +1

def tenplace(one):
    array= one
    tens = []
    i = 0
    c = 90
    for z in array:
        if 10 <= z :
            tens.append(z)
    for z in tens:
        array.remove(z)
            
    while i<=9: 
        for x in tens:
            if c<=x%100:
                ten.append(x)
                tens.remove(x)
        c = c - 10
        i= i +1
    for x in array:
        ten.append(x)

def hunplace(ten):
    array= ten
    hundred=[]
    i = 0
    c = 900
    for z in array:
        if 100 <= z :
            hundred.append(z)
    for z in hundred:
        array.remove(z)
    while i<=9: 
        for x in hundred:
            if c<=x%1000:
                hun.append(x)
                hundred.remove(x)
        c = c - 100
        i= i +1
    for x in array:
        hun.append(x)

def thouplace(hun):
    array= hun
    thousand=[]
    i = 0
    c = 9000
    for z in array:
        if 1000 <= z :
            thousand.append(z)
    for z in thousand:
        array.remove(z)
    while i<=9: 
        for x in thousand:
            if c<=x%10000:
                thou.append(x)
                thousand.remove(x)
        c = c - 1000
        i= i +1
    for x in array:
        thou.append(x)

start = int(input("Input initial value: "))
end = int(input("Input terminating value: "))

num = random.sample(range(start, end), 10)
print("Random numbers:",num)
print("\nChoices:\n[1] One's Place Value\n[2]  Ten's Place Value\n[3] Hundred's Place Value\n[4] Thousand's Place Value\n[5] Exit")
while True:
        try: 
                choice=int(input("Enter Choice: "))

                if choice == 1:
                    oneplace(num)
                    print("One's Place Value: ",one)
                    one.clear()
                    
                elif choice ==2:
                    oneplace(num)
                    tenplace(one)
                    print("Ten's Place Value: ", ten)
                    one.clear()
                    ten.clear()
                    
                elif choice ==3:
                    oneplace(num)
                    tenplace(one)
                    hunplace(ten)
                    print("Hundred's Place Value: ", hun)
                    one.clear()
                    ten.clear()
                    hun.clear()
                    
                elif choice ==4:
                    oneplace(num)
                    tenplace(one)
                    hunplace(ten)
                    thouplace(hun)
                    print("Thousand's Place Value: ", thou)   
                    one.clear()
                    ten.clear()
                    hun.clear()
                    thou.clear()
              
                elif choice ==5:
                        break
                else:
                    print("Invalid Choice!")

                while True:    
                    main = str(input("Press M/m  to return to main menu:"))
                    if main == "M" or main== "m":
                        print("\nChoices:\n[1] One's Place Value\n[2]  Ten's Place Value\n[3] Hundred's Place Value\n[4] Thousand's Place Value\n[5] Exit")
                        break                       
                    else:
                        print ("Invalid Input!")
                        continue
                        
        except ValueError:
                print ("Invalid Input!")
