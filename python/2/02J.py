Требуется написать программу, которая считывает строки из стандартного ввода. 
Если считана строка "Stop!", программа печатает "Ок" (кириллицей) и останавливает работу. 
В ином случае она печатает "Каша" и считывает следующую строку.

_kas = input()
while _kas != "Stop!":
    print("Каша")
    _kas = input()
print("Ок")
