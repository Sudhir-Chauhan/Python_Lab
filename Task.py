def add(a,b) :
    result = a+b
    print(result)

lst = []
Size = int(input("Enter the Size of List: "))
for i in range(Size):
    element = int(input("Enter the Element: "))
    lst.append(element)
    print(lst)

    for i in range(len(lst)):
        if i == len(lst) -1:
            break
        else:
            add(lst[i],lst[i+1])
