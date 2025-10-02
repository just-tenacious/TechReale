lst=[]
print("Created an empty list!")
flag=True

while(flag):
    checkFlag=input("Do you want to operate?(y/n): ").lower()
    if(checkFlag=='y' and flag):
        print("********MENU*********")
        print("@ To show list")
        print("1. Add an element")
        print("2. Add more than one element")
        print("3. Clear elements")
        print("4. Copy the list")
        print("5. Count the number of occurence in list of an element")
        print("6. Add at a specific index")
        print("7. Get index of 1st occurence of an element")
        print("8. Remove an element from a specific position")
        print("9. Remove an element of specific value")
        print("10. Sort the list")
        print("11. Reverse the order of list")
        print("12. EXIT")
        choice=input("Enter the choice to perform(number):")
        if(choice=='@'):
            print(lst)
        elif(choice=='1'):
            elt=input("Enter element:")
            lst.append(elt)
            print(lst)
        elif(choice=='2'):
            eltCount=int(input("Enter the number of elements to add:"))
            eltList=[]
            for e in range(eltCount):
                elt=input("Enter element: ")
                eltList.append(elt)
            lst.extend(eltList)
            print(lst)
        elif(choice=='3'):
            print(f"The old list: {lst}")
            lst.clear()
            print(f"The list after clearing: {lst}")
        elif(choice=='4'):
            newList=lst.copy()
            print("The list is copied")
        elif(choice=='5'):
            elt=input("Enter the element to count its occurence:")
            count=lst.count(elt)
            print(f"The number of occurence of {elt} is {count}")
        elif(choice=='6'):
            index=int(input("Enter the index position to add:"))
            elt=input("Enter element: ")
            lst.insert(index, elt)
            print(lst)
        elif(choice=='12'):
            print("Thank You")
            flag=False
            break
        else:
            print("Enter a valid choice")
    elif(checkFlag!='y' and checkFlag!='n' and flag):
        print("Enter 'y' for yes and 'n' for no")
    else:
        print("Thank you!!")
        flag=False
        break