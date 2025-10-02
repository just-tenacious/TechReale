import stringMethods as s

flag = True
text = input("Enter your string:")

while (flag):
    checkFlag = input("Do u want to operate on your string(y/n):")
    if (checkFlag.lower() == 'y' and flag):
        print("**********MENU*********")
        print("1. Capitalize 1st letter")
        print("2. To casefold")
        print("3. To center your text")
        print("4. To get index  of occurence of a value")
        print("5. Check if it ends with specific notation")
        print("6. To add to the string")
        print("7. If it is a combination of charcters and numbers")
        print("8. If it contains only characters")
        print("9. If it contains only numbers")
        print("10. If it is a decimal")
        print("11. Exit")
        choice = int(input("\nEnter choice(number):"))
        if (choice == 1):
            result = s.capitalizeString(text)
            print(result)
        elif(choice==2):
            result=s.caseFold(text)
            print(result)
        elif(choice==3):
            result=s.centerText(text)
            print(result)
        elif(choice==4):
            character=input("Enter the substring:")
            count=s.findOccurence(text, character)
            if(count==-1 or count==0):
                print("No occurence found!")
            else:
                print(f"Index of occurence:{count}")
        elif(choice==5):
            endText=input("Enter the text to chcek whether to end with or not:")
            if(s.endOfText(text, endText)):
                print("Yes it does!")
            else:
                print("No, it doesn't")
        elif(choice==6):
            newText=input("Enter the text to add:")
            text=s.addText(text, newText) 
            print(text)
        elif(choice==7):
            if(s.isCombo(text)):
                print("Yes,it is!")
            else:
                print("No,it doesn't")
        elif(choice==8):
            if(s.characters(text)):
                print("Yes,only characters are there.")
            else:
                print("No, other than alphabets are present")
        elif(choice==9):
            if(s.numbers(text)):
                print("Yes,only numbers are there.")
            else:
                print("No, other than numbers are present")
        elif(choice==10):
            if(s.decimals(text)):
                print("Yes,it is a decimal.")
            else:
                print("No, it is not a decimal")        
        elif(choice == 11):
            flag = False
            break
        else:
            print("Enter the choice from menu.")
    elif(checkFlag.lower() != 'y' and checkFlag !='n' and checkFlag):
        print("Enter either 'y' or 'n' as a choice.")
    else:
        print('Thank You!!')
        checkFlag = False
        break