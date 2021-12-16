'''
import random


def main():
    menu()
    levels()


def menu():
    print("*** We're Really Not Strangers ***")
    print("Level 1: Perception")
    print("Level 2: Connection")
    print("Level 3: Reflection")


def levels():
    choice = str(input("Pick one of the 3 levels(1,2,3) or f for final card: ")).strip()

    openFile(choice)


def openFile(choice):
    print("")
    if choice == "1":
        fileName = "perception.txt"
        # f = open("perception.txt", "r")
        printQuestion(fileName)

    elif choice == "2":
        # f = open("connection.txt", "r")
        fileName = "connection.txt"
        printQuestion(fileName)

    elif choice == "3":
        # f = open("reflection.txt", "r")
        fileName = "reflection.txt"
        printQuestion(fileName)

    elif choice == "f":
        fileName = "final.txt"
        finalCard(fileName)

    else:
        print("Enter 1,2, or 3")
        levels()


def printQuestion(fileName):
    flag = True
    while flag:
        f = open(fileName, 'r')
        print(random.choice(list(f)))
        again = str(input("Same level?(y/n) ")).strip()

        if again == 'n':
            f.close()
            flag = False
            levels()
        else:
            continue


def finalCard(fileName):
    f = open(fileName, 'r')
    print(random.choice(list(f)))
    f.close()


if "__main__":
    main()
'''