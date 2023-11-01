import os, re

def showContacts(fileName):
    with open(fileName, "r",encoding="UTF-8") as files:
        data = (files.readlines())
        num = 1
        for line in data:
            print(num ,line)
            num +=1
    input("\n--- нажмите для продолжения Enter ---")


def addContact(fileName):
    with open(fileName, "a") as file:
        res = ""
        res += input("Введите фамилию контакта: ") + ","
        res += input("Введите имя контакта: ") + ","
        res += input("Введите номер телефона контакта: ")

        file.write(res + "\n")

    input("\nКонтакт был успешно добавлен!")




def deleteContact(fileName):
    num = 1
    with open(fileName, "r", errors='ignore') as file:
        data = sorted(file.readlines())
        for line in data:
            print(num, line)
            num += 1


        numberContact = int(
            input("Введите номер контакта для удаления или 0 для возврата в главное меню: ")
        )
        if numberContact != 0:
            print(f"Удаление записи: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- нажмите для продолжения Enter ---")




def merge (path = "phonebook.txt",path_2 ="phonebook_2.txt" ):
    with open(path, "r",encoding="UTF-8") as file:
        data = sorted(file.readlines())
        num = 1
        print("Телефонная книга №1")
        for line in data:
            print(num, line)
            num += 1

    with (open(path_2, "a",encoding="UTF-8") as file2):
        data2 = open("phonebook_2.txt", "r")

        numberContact = int(input(" Введите номер контакта который нужно скопировать :"))
        if numberContact != 0:
            print(f"Копирование контакта: {data[numberContact - 1].rstrip().split(',')}\n")

            file2.write(f"{data[numberContact - 1]}")



    input("")

def drawInterface():

    print(" [1] -- Показать контакты")
    print(" [2] -- Добавить контакты")
    print(" [3] -- Удалить контакт")
    print(" [4] -- Копирование контакта")
    print("\n [0] -- Выход")
def main(file_name):
    while True:
        drawInterface()
        userChoice = int(input("Введите число от 1 до 4 или 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            deleteContact(file_name)
        elif userChoice == 4:
            merge()
        elif userChoice == 0:
            print("Работа программы завершена")
            return


path = "phonebook.txt"
# path_2 = "phonebook_2.txt"
main(path)